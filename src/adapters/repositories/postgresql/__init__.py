from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.exceptions.repository_exceptions import (
    FailToRetrieveInformationException,
    ExtensionConversionException,
    FailToInsertInformationException,
    RepositoryUnexpectedException,
)
from src.externals.infrastructures.postgre_sql.exceptions.postgresql_base_infrastructure_exception import (
    PostgresqlBaseInfrastructureException,
)


def repository_upsert_error_handler(function):
    async def wrap(*args, **kwargs):
        try:
            return await function(*args, **kwargs)

        except RepositoryBaseException as original_exception:
            raise original_exception

        except PostgresqlBaseInfrastructureException as original_exception:
            raise FailToInsertInformationException(
                message="Error trying to insert some data.",
                original_error=original_exception,
            ) from original_exception

        except ExtensionsBaseException as original_exception:
            raise ExtensionConversionException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception

        except Exception as original_exception:
            raise RepositoryUnexpectedException(
                message="Unexpected error when trying to insert some data.",
                original_error=original_exception,
            ) from original_exception

    wrap.__wrapped__ = function
    return wrap


def repository_retrieving_error_handler(function):
    async def wrap(*args, **kwargs):
        try:
            return await function(*args, **kwargs)

        except PostgresqlBaseInfrastructureException as original_exception:
            raise FailToRetrieveInformationException(
                message="Error trying to retrieving some data.",
                original_error=original_exception,
            ) from original_exception

        except ExtensionsBaseException as original_exception:
            raise ExtensionConversionException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception

        except Exception as original_exception:
            raise FailToRetrieveInformationException(
                message="Unexpected error when trying to retrieving some data.",
                original_error=original_exception,
            ) from original_exception

    wrap.__wrapped__ = function
    return wrap
