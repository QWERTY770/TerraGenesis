import os


class ResourceLocation:
    def __init__(self, ns: str, resource_type: str, path: str, filename_suffix=".json"):
        self.namespace = ns
        self.type = resource_type
        self.path = path
        self.filename_suffix = filename_suffix

    def __str__(self):
        return f"ResourceLocation[{self.namespace}, {self.path}]"

    @classmethod
    def from_string(cls, string: str):
        t = string.split(":")
        return cls(t[0], t[1])

    def get_path(self) -> str:
        return os.path.join(os.getcwd(), "data", self.namespace, self.type, self.path) + self.filename_suffix

    def read(self):
        return open(self.get_path()).read()
