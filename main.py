import uvicorn
from decouple import config
from fastapi import FastAPI
from pyfiglet import print_figlet

from src.externals.infrastructures.api_config.fast_api_config_infrastructure import (
    FastAPIConfigInfrastructure,
)
from src.externals.infrastructures.http_config.fast_api_http_server_config_infrastructure import (
    FastApiHttpServerConfigInfrastructure,
)
from src.externals.infrastructures.ioc_container_config.witch_doctor_container_config_infrastructure import (
    WitchDoctorContainerConfigInfrastructure,
)
from src.externals.infrastructures.logs.loglifos_config_infrastructure import (
    LoguruConfigInfrastructure,
)


def config_application() -> FastAPI:
    http_server_config = FastApiHttpServerConfigInfrastructure()
    ioc_container_config = WitchDoctorContainerConfigInfrastructure()
    logs_config = LoguruConfigInfrastructure()

    fast_api_config = FastAPIConfigInfrastructure(
        http_server_config=http_server_config,
        ioc_container_config=ioc_container_config,
        logs_config=logs_config,
    )

    return fast_api_config.set_configs()


if __name__ == "__main__":
    host = config("SERVER_HOST")
    root_path = config("ROOT_PATH")
    port = int(config("SERVER_PORT"))
    app = config_application()

    print(f"Server is ready at URL {host}:{str(port) + root_path}")
    print_figlet(text="syrax-bank-api", colors="0;78;225", width=200)

    uvicorn.run(app, host=host, port=port)
