from witch_doctor import WitchDoctor, InjectionType

from src.adapters.extensions.bank_accounts.bank_accounts_extension import (
    BankAccountsExtension,
)
from src.adapters.extensions.bank_accounts.create_new_account_extension import (
    CreateNewAccountExtension,
)
from src.adapters.extensions.bank_accounts.movement_cash_extension import (
    MovementCashExtension,
)
from src.adapters.extensions.bank_accounts.transactions_extension import (
    TransactionsExtension,
)
from src.adapters.ports.infrastructures.postgresql.i_postgresql_infrastructure import (
    IPostgresqlInfrastructure,
)
from src.adapters.repositories.postgresql.bank_accounts_repository import (
    BankAccountsRepository,
)
from src.externals.infrastructures.postgre_sql.postgresql_infrastructure import (
    PostgresqlInfrastructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (
    IIocContainerConfigInfrastructure,
)
from src.use_cases.account_deposit_use_case import AccountDepositUseCase
from src.use_cases.account_withdraw_use_case import AccountWithdrawUseCase
from src.use_cases.create_new_account_use_case import (
    CreateNewAccountUseCase,
)
from src.use_cases.list_accounts_use_case import ListAccountsUseCase
from src.use_cases.list_transactions_by_account_use_case import (
    ListTransactionsByAccountUseCase,
)
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)
from src.use_cases.ports.extensions.bank_accounts.i_create_new_account_extension import (
    ICreateNewAccountExtension,
)
from src.use_cases.ports.extensions.bank_accounts.i_movement_cash_extension import (
    IMovementCashExtension,
)
from src.use_cases.ports.extensions.bank_accounts.i_transactions_extension import (
    ITransactionsExtension,
)
from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)
from src.use_cases.ports.use_cases.i_account_deposit_use_case import (
    IAccountDepositUseCase,
)
from src.use_cases.ports.use_cases.i_account_withdraw_use_case import (
    IAccountWithdrawUseCase,
)
from src.use_cases.ports.use_cases.i_create_new_account_use_case import (
    ICreateNewAccountUseCase,
)
from src.use_cases.ports.use_cases.i_list_accounts_use_case import (
    IListAccountsUseCase,
)
from src.use_cases.ports.use_cases.i_list_transactions_by_account_use_case import (
    IListTransactionsByAccountUseCase,
)


class WitchDoctorContainerConfigInfrastructure(IIocContainerConfigInfrastructure):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container("use_cases")

        use_cases_container(
            ICreateNewAccountUseCase, CreateNewAccountUseCase, InjectionType.SINGLETON
        )
        use_cases_container(
            IListAccountsUseCase, ListAccountsUseCase, InjectionType.SINGLETON
        )
        use_cases_container(
            IListTransactionsByAccountUseCase,
            ListTransactionsByAccountUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            IAccountDepositUseCase, AccountDepositUseCase, InjectionType.SINGLETON
        )
        use_cases_container(
            IAccountWithdrawUseCase, AccountWithdrawUseCase, InjectionType.SINGLETON
        )

        return use_cases_container

    @classmethod
    def __create_infrastructures_container(cls):
        infrastructures_container = WitchDoctor.container("infrastructures")

        infrastructures_container(
            IPostgresqlInfrastructure, PostgresqlInfrastructure, InjectionType.SINGLETON
        )

        return infrastructures_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container("repositories")

        repositories_container(
            IBankAccountsRepository, BankAccountsRepository, InjectionType.SINGLETON
        )

        return repositories_container

    @classmethod
    def __create_extensions_container(cls):
        extensions_container = WitchDoctor.container("extensions")

        extensions_container(
            IBankAccountsExtension, BankAccountsExtension, InjectionType.SINGLETON
        )
        extensions_container(
            ICreateNewAccountExtension,
            CreateNewAccountExtension,
            InjectionType.SINGLETON,
        )
        extensions_container(
            ITransactionsExtension,
            TransactionsExtension,
            InjectionType.SINGLETON,
        )
        extensions_container(
            IMovementCashExtension,
            MovementCashExtension,
            InjectionType.SINGLETON,
        )

        return extensions_container

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_repositories_container()
        cls.__create_extensions_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container("use_cases")
        WitchDoctor.load_container("infrastructures")
        WitchDoctor.load_container("repositories")
        WitchDoctor.load_container("extensions")

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
