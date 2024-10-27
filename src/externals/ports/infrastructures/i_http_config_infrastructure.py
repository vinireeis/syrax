from abc import ABC, abstractmethod

from fastapi import FastAPI


class IHttpServerConfigStructure(ABC):
    @abstractmethod
    def set_http_server_config(self) -> FastAPI:
        pass
