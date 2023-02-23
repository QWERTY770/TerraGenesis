from typing import TypeVar, Generic, List


T = TypeVar("T")


class Registry(Generic[T]):
    def __init__(self, namespace: str):
        super().__init__()
        self.registry_list = []  # type: List[T]
        self.namespace = namespace

    def register(self, obj: T):
        obj.namespace = self.namespace
        self.registry_list.append(obj)
        return obj
