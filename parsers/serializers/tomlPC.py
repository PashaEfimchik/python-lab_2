from parsers.serializers import Serializer
from parsers.serializers.tomlP.tomlP import TomlSerializer
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_serializer(self):
        pass


class TomlSerializerCreator(Creator):
    def create_serializer(self) -> Serializer:
        return TomlSerializer()