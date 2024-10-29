from abc import ABC, abstractmethod


class ILogsConfigInfrastructure(ABC):
    @classmethod
    @abstractmethod
    def set_logger_config(cls):
        pass
