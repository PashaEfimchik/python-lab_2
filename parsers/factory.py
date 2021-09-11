from parsers.serializers.jsonP.jsonP import JsonSerializer
from parsers.serializers.yamlP.yamlP import YamlSerializer
from parsers.serializers.tomlP.tomlP import TomlSerializer
from parsers.serializers.pickleP.pickleP import PickleSerializer


class SerializerFactory:
    def __init__(self):
        self.serializers = {}
        self.register_format('JSON', JsonSerializer)
        self.register_format('YAML', YamlSerializer)
        self.register_format('TOML', TomlSerializer)
        self.register_format('PICKLE', PickleSerializer)

    def register_format(self, format, serializer):
        if format.lower() in self.serializers:
            raise LookupError(f"{format} serializer already exists")
        self.serializers[format.lower()] = serializer

    def get_serializer(self, format):
        serializer = self.serializers.get(format.lower())
        if not serializer:
            raise ValueError(f"{format} format isn't supported")
        return serializer()