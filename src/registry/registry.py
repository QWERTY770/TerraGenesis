from src.core.logs import logger
from src.buildings.faci import BaseFaci
from src.world.map import HeightMap, SurfaceMap


class RegistyType:
    def __init__(self, registry_id: int, cls: type):
        self.id = registry_id
        self.cls = cls


FACI_REGISTRY = RegistyType(0, BaseFaci)

HEIGHT_MAP_REGISTRY = RegistyType(1001, HeightMap)
SURFACE_MAP_REGISTRY = RegistyType(1002, SurfaceMap)


class Registry:
    def __init__(self, registry_type: RegistyType, namespace: str):
        super().__init__()
        self.type = registry_type
        self.registry_list = []
        self.namespace = namespace

    def register(self, obj):
        if not isinstance(obj, self.type.cls):
            logger.error(f"Wrong registry object: expected {self.type.cls} object, found {type(obj)}")
        else:
            obj.namespace = self.namespace
            self.registry_list.append(obj)
        return obj
