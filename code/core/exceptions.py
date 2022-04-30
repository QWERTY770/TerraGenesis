from .logs import logger


class DatapackReadError(Exception):
    def __init__(self, message):
        super().__init__(message)
        logger.error(message)


class BuildingCountError(Exception):
    def __init__(self, message):
        super().__init__(message)
        logger.error(message)
