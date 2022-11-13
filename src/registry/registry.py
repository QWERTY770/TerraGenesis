from src.core.logs import logger
from src.buildings.faci import BaseFaci


class RegistyType:
    def __init__(self, registry_id: int, cls: type):
        self.id = registry_id
        self.cls = cls


FACI_REGISTRY = RegistyType(0, BaseFaci)


class Registry:
    def __init__(self, registry_type: RegistyType):
        super().__init__()
        self.type = registry_type
        self.registry_list = []

    def register(self, obj):
        if not isinstance(obj, self.type.cls):
            logger.error(f"Wrong registry object: expected {self.type.cls} object, found {type(obj)}")
        else:
            self.registry_list.append(obj)
        return obj
