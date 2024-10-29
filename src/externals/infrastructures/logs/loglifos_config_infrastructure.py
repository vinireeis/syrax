import loguru
import sys
from decouple import config

from src.externals.ports.infrastructures.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)


class LoguruConfigInfrastructure(ILogsConfigInfrastructure):
    @classmethod
    def set_logger_config(cls):
        log_level = int(config("LOG_LEVEL"))
        loguru.logger.add(sys.stderr, level=log_level)
