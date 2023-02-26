from typing import TypeVar, Generic, List


class HasID:
    """Registry objects need to extend this"""

    def __init__(self, obj_id):
        self.id = obj_id


T = TypeVar("T", bound=HasID)


class Registry(Generic[T]):
    def __init__(self, namespace: str):
        super().__init__()
        self.registry_list = []  # type: List[T]
        self.namespace = namespace

    def register(self, obj: T):
        obj.namespace = self.namespace
        self.registry_list.append(obj)
        return obj

    def get_obj_by_id(self, obj_id):
        for i in self.registry_list:
            if i.id == obj_id:
                return i
        return -1
