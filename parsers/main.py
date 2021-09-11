from serializers.jsonPC import JsonSerializerCreator
from serializers.picklePC import PickleSerializerCreator
from serializers.tomlPC import TomlSerializerCreator
from serializers.yamlPC import YamlSerializerCreator
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_serializer(self):
        pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "female"

    def set_name(self, name):
        self.name = name


a = 3
b = 4
c = 5


def hello(name):
    print(f"hello, {name} _ {c}!")


def create_serializer(creator: Creator):
    return creator.create_serializer()


def _main():
    serializer_1 = create_serializer(JsonSerializerCreator())
    person_1 = Person("Pavel", 19)
    person_dict_1 = serializer_1.dumps(person_1)
    print(person_dict_1)
    
    serializer_2 = create_serializer(PickleSerializerCreator())
    person_2 = Person("Artyom", 18)
    person_dict_2 = serializer_2.dumps(person_2)
    print(person_dict_2)

    serializer_3 = create_serializer(TomlSerializerCreator())
    person_3 = Person("Vecheslav", 20)
    person_dict_3 = serializer_3.dumps(person_3)
    print(person_dict_3)

    serializer_4 = create_serializer(YamlSerializerCreator())
    person_4 = Person("Daniil", 21)
    person_dict_4 = serializer_4.dumps(person_4)
    print(person_dict_4)


if __name__ == "__main__":
    _main()