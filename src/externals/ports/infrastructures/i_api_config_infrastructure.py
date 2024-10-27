from abc import ABC, abstractmethod

from fastapi import FastAPI


class IApiConfigInfrastructure(ABC):
    @abstractmethod
    def set_configs(self) -> FastAPI:
        pass
