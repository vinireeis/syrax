from decouple import config
from psycopg import AsyncCursor
from psycopg.rows import dict_row
from pydantic import UUID4
from witch_doctor import WitchDoctor
from psycopg.sql import SQL

from src.adapters.ports.infrastructures.postgresql.i_postgresql_connection_pool import (
    IPostgresqlConnectionPool,
)
from src.adapters.ports.infrastructures.postgresql.i_postgresql_infrastructure import (
    IPostgresqlInfrastructure,
)
from src.adapters.repositories.exceptions.repository_exceptions import (
    FailToInsertInformationException,
    InvalidOperationInsufficientBalanceException,
)
from src.adapters.repositories.postgresql import (
    repository_upsert_error_handler,
    repository_retrieving_error_handler,
)
from src.adapters.repositories.postgresql.queries import (
    insert_one_transaction_query,
    list_all_accounts_query,
    insert_new_account_query,
    get_transactions_by_account_query,
    balance_query_lock,
    amount_deposit_query_update,
    cash_out_query_update,
    target_account_balance_query_lock,
)
from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.models.bank_account_model import BankAccountModel
from src.domain.models.transaction_model import TransactionModel
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)
from src.use_cases.ports.extensions.bank_accounts.i_transactions_extension import (
    ITransactionsExtension,
)
from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)


class BankAccountsRepository(IBankAccountsRepository):
    __postgresql_infrastructure: IPostgresqlInfrastructure
    __postgresql_connection_pool: IPostgresqlConnectionPool
    __bank_accounts_extension: IBankAccountsExtension
    __transactions_extension: ITransactionsExtension

    @WitchDoctor.injection
    def __init__(
        self,
        postgresql_infrastructure: IPostgresqlInfrastructure,
        bank_accounts_extension: IBankAccountsExtension,
        transactions_extension: ITransactionsExtension,
    ):
        BankAccountsRepository.__postgresql_infrastructure = postgresql_infrastructure
        BankAccountsRepository.__postgresql_connection_pool = (
            BankAccountsRepository.__postgresql_infrastructure.get_pool(
                uri=config("POSTGRES_STRING_CONNECTION"),
                database=config("POSTGRES_DB"),
            )
        )
        BankAccountsRepository.__bank_accounts_extension = bank_accounts_extension
        BankAccountsRepository.__transactions_extension = transactions_extension

    @classmethod
    @repository_upsert_error_handler
    async def insert_new_account(cls, bank_account_entity: BankAccountEntity):
        new_account_document = bank_account_entity.new_account_document()

        async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
            row_factory=dict_row
        ) as cursor:
            cursor: AsyncCursor

            prepared_statement = await cursor.execute(
                query=insert_new_account_query,
                params=new_account_document,
                prepare=True,
            )

            if not prepared_statement.rowcount:
                raise FailToInsertInformationException(
                    message="Fail to insert new account.",
                )

    @classmethod
    @repository_retrieving_error_handler
    async def list_accounts(cls) -> list[BankAccountModel]:
        async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
            row_factory=dict_row
        ) as cursor:
            cursor: AsyncCursor

            prepared_statement = await cursor.execute(
                query=list_all_accounts_query, prepare=True
            )
            result_list = await prepared_statement.fetchall()
            bank_account_models = (
                cls.__bank_accounts_extension.from_database_result_list_to_model_list(
                    result_list=result_list
                )
            )

            return bank_account_models

    @classmethod
    @repository_upsert_error_handler
    async def insert_new_transaction(cls, transaction_entity: TransactionEntity):
        transaction_document = transaction_entity._transaction_document()

        async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
            row_factory=dict_row
        ) as cursor:
            cursor: AsyncCursor

            prepared_statement = await cursor.execute(
                query=insert_one_transaction_query,
                params=transaction_document,
                prepare=True,
            )

            if not prepared_statement.rowcount:
                raise FailToInsertInformationException(
                    message="Fail to insert new transaction.",
                )

    @classmethod
    @repository_upsert_error_handler
    async def insert_transaction_between_accounts(
        cls, transaction_entity: TransactionEntity
    ):
        async with cls.__postgresql_connection_pool.get_connection() as connection:
            cash_out_document = transaction_entity._transaction_document()
            cash_in_document = (
                transaction_entity._transaction_document_to_target_account()
            )

            async with connection.transaction():
                async with connection.cursor(row_factory=dict_row) as cursor:
                    cursor: AsyncCursor

                    f_prepared_statement = await cursor.execute(
                        query=insert_one_transaction_query,
                        params=cash_out_document,
                        prepare=True,
                    )
                    s_prepared_statement = await cursor.execute(
                        query=insert_one_transaction_query,
                        params=cash_in_document,
                        prepare=True,
                    )

                    if (
                        not f_prepared_statement.rowcount
                        and not s_prepared_statement.rowcount
                    ):
                        raise FailToInsertInformationException(
                            message="Fail to insert new transaction.",
                        )

    @classmethod
    @repository_retrieving_error_handler
    async def get_transactions_by_account_id(
        cls, account_id: UUID4
    ) -> list[TransactionModel]:
        async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
            row_factory=dict_row
        ) as cursor:
            cursor: AsyncCursor

            prepared_statement = await cursor.execute(
                query=get_transactions_by_account_query,
                params=dict(account_id=account_id),
                prepare=True,
            )

            result_list = await prepared_statement.fetchall()
            transaction_models = (
                cls.__transactions_extension.from_database_result_list_to_model_list(
                    result_list=result_list
                )
            )

            return transaction_models

    @classmethod
    @repository_retrieving_error_handler
    async def deposit_amount_by_account_id(cls, transaction_entity: TransactionEntity):
        amount_to_insert = transaction_entity._amount_document()

        async with cls.__postgresql_connection_pool.get_connection() as connection:
            async with connection.transaction():
                async with connection.cursor() as cursor:

                    await cursor.execute(
                        query=balance_query_lock,
                        params=dict(account_id=transaction_entity.account_id),
                        prepare=True,
                    )
                    update_prepared_statement = await cursor.execute(
                        query=amount_deposit_query_update,
                        params=amount_to_insert,
                        prepare=True,
                    )

                    if not update_prepared_statement.rowcount:
                        raise FailToInsertInformationException(
                            message="Fail to deposit amount.",
                        )

    @classmethod
    @repository_upsert_error_handler
    async def withdraw_amount_by_account_id(cls, transaction_entity: TransactionEntity):
        amount_to_insert = transaction_entity._amount_document()

        async with cls.__postgresql_connection_pool.get_connection() as connection:
            async with connection.transaction():
                async with connection.cursor() as cursor:

                    await cursor.execute(
                        query=balance_query_lock,
                        params=dict(account_id=transaction_entity.account_id),
                        prepare=True,
                    )
                    update_prepared_statement = await cursor.execute(
                        query=cash_out_query_update,
                        params=amount_to_insert,
                        prepare=True,
                    )

                    if not update_prepared_statement.rowcount:
                        raise InvalidOperationInsufficientBalanceException(
                            message="Operation not permitted, insufficient balance."
                        )

    @classmethod
    @repository_upsert_error_handler
    async def update_amount_balance_between_accounts(
        cls, transaction_entity: TransactionEntity
    ):
        async with cls.__postgresql_connection_pool.get_connection() as connection:
            async with connection.transaction():
                async with connection.cursor() as cursor:

                    # cashout
                    await cursor.execute(
                        query=balance_query_lock,
                        params=dict(account_id=transaction_entity.account_id),
                        prepare=True,
                    )
                    default_amount_document = transaction_entity._amount_document()
                    f_update_prepared_statement = await cursor.execute(
                        query=cash_out_query_update,
                        params=default_amount_document,
                        prepare=True,
                    )

                    # cashin
                    target_account_amount_document = (
                        transaction_entity._amount_document_to_target_account()
                    )
                    await cursor.execute(
                        query=target_account_balance_query_lock,
                        params=dict(account_id=transaction_entity.target_account_id),
                        prepare=True,
                    )
                    s_update_prepared_statement = await cursor.execute(
                        query=amount_deposit_query_update,
                        params=target_account_amount_document,
                        prepare=True,
                    )

                    if not f_update_prepared_statement.rowcount:
                        raise InvalidOperationInsufficientBalanceException(
                            message="Operation not permitted, insufficient balance."
                        )
                    if not s_update_prepared_statement.rowcount:
                        raise FailToInsertInformationException(
                            message="Fail to deposit amount.",
                        )
