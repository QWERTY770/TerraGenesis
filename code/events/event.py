from typing import Optional, Dict
from types import FunctionType

from effect import Effect
from code.buildings.city import City
from random import sample, randint
from code.core.exceptions import *


class Event:
    def __init__(self, name: str, event_id: str, description: str, choices_and_effects: Dict[str, FunctionType]):
        self.name = name
        self.id = event_id
        self.description = description
        self.choices_and_effects = choices_and_effects
    

def json_to_event(src: dict):
    # TODO
    try:
        if src["choices_and_effects"] == "pass":
            return Event(src["name"], src["id"], src["description"], {""})
    except Exception as e:
        pass
