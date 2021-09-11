from parsers.serializers import Serializer
from parsers.serializers.pickleP.pickleP import PickleSerializer
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_serializer(self):
        pass


class PickleSerializerCreator(Creator):
    def create_serializer(self) -> Serializer:
        return PickleSerializer()