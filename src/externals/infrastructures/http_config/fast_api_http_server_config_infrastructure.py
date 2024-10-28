from decouple import config
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.routers.syrax_bank_router import SyraxBankRouter


class FastApiHttpServerConfigInfrastructure(IHttpServerConfigInfrastructure):
    def __init__(self):
        self.__root = config("ROOT_PATH")
        self.__app = FastAPI(
            title="Syrax Bank",
            description="Accounts and financial transactions",
            docs_url=self.__root + "/docs",
            openapi_url=self.__root + "/openapi.json",
        )

    def __apply_cors_rules(self):
        cors_allowed_origins_str = config("CORS_ALLOWED_ORIGINS")
        cors_allowed_origins = cors_allowed_origins_str.split(",")
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __register_router(self):
        syrax_bank_routers = SyraxBankRouter.get_routers()

        [
            self.__app.include_router(router, prefix=self.__root)
            for router in syrax_bank_routers
        ]

    def set_http_server_config(self) -> FastAPI:
        self.__apply_cors_rules()
        self.__register_router()
        return self.__app
