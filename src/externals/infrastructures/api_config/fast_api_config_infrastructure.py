from fastapi import FastAPI

from src.externals.ports.infrastructures.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (
    IIocContainerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)


class FastAPIConfigInfrastructure(IApiConfigInfrastructure):
    def __init__(
        self,
        http_server_config: IHttpServerConfigInfrastructure,
        ioc_container_config: IIocContainerConfigInfrastructure,
        logs_config: ILogsConfigInfrastructure,
    ):
        self.__http_server_config = http_server_config
        self.__ioc_container_config = ioc_container_config
        self.__logs_config = logs_config

    def set_configs(self) -> FastAPI:
        app = self.__http_server_config.set_http_server_config()
        self.__ioc_container_config.build_ioc_container()
        self.__logs_config.set_logger_config()

        return app
