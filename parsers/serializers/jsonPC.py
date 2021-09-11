from .Serializer import Serializer
from .jsonP.jsonP import JsonSerializer
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_serializer(self):
        pass

class JsonSerializerCreator(Creator):
    def create_serializer(self) -> Serializer:
        return JsonSerializer()