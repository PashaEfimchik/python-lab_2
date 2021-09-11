from parsers.serializers import Serializer
from parsers.serializers.yamlP.yamlP import YamlSerializer
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_serializer(self):
        pass


class YamlSerializerCreator(Creator):
    def create_serializer(self) -> Serializer:
        return YamlSerializer()