from decouple import config
from psycopg import AsyncCursor
from psycopg.rows import dict_row
from witch_doctor import WitchDoctor
from psycopg.sql import SQL

from src.adapters.ports.infrastructures.postgresql.i_postgresql_connection_pool import (
    IPostgresqlConnectionPool,
)
from src.adapters.ports.infrastructures.postgresql.i_postgresql_infrastructure import (
    IPostgresqlInfrastructure,
)
from src.adapters.repositories.postgresql import repository_insertion_error_handler
from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.models.bank_account_model import BankAccountModel
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)
from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)


class BankAccountsRepository(IBankAccountsRepository):
    __postgresql_infrastructure: IPostgresqlInfrastructure
    __postgresql_connection_pool: IPostgresqlConnectionPool
    __bank_accounts_extension: IBankAccountsExtension

    @WitchDoctor.injection
    def __init__(
        self,
        postgresql_infrastructure: IPostgresqlInfrastructure,
        bank_accounts_extension: IBankAccountsExtension,
    ):
        BankAccountsRepository.__postgresql_infrastructure = postgresql_infrastructure
        BankAccountsRepository.__postgresql_connection_pool = (
            BankAccountsRepository.__postgresql_infrastructure.get_pool(
                uri=config("POSTGRESQL_STRING_CONNECTION"),
                database=config("POSTGRESQL_DATABASE"),
            )
        )
        BankAccountsRepository.__bank_accounts_extension = bank_accounts_extension

    @classmethod
    @repository_insertion_error_handler
    async def insert_new_account(cls, bank_account_entity: BankAccountEntity):

        async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
            row_factory=dict_row
        ) as cursor:
            cursor: AsyncCursor
            query = SQL(
                obj="""
                INSERT INTO Accounts (account_id) VALUES %(account_id)s
                    """
            )

            prepared_statement = await cursor.execute(
                query=query,
                params=dict(account_id=bank_account_entity.account_id),
                prepare=True,
            )

            print(prepared_statement)

            return True

    @classmethod
    @repository_insertion_error_handler
    async def list_accounts(cls) -> list[BankAccountModel]:
        async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
            row_factory=dict_row
        ) as cursor:
            cursor: AsyncCursor

            query = SQL(
                obj="""
                        SELECT * FROM Accounts
                                """
            )

            prepared_statement = await cursor.execute(query=query, prepare=True)

            if result_list := await prepared_statement.fetchone():
                bank_account_models = cls.__bank_accounts_extension.from_database_result_list_to_model_list(
                    result_list=result_list
                )

                return bank_account_models
