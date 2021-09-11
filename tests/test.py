import unittest
import sys
from parsers.serializers.jsonPC import JsonSerializerCreator
from parsers.serializers.picklePC import PickleSerializerCreator
from parsers.serializers.yamlPC import YamlSerializerCreator
from parsers.serializers.tomlPC import TomlSerializerCreator
from parsers.serializers.jsonP.jsonP import from_json, _json_to_dict, _json_to_list, _json_to_basic
from parsers.factory import SerializerFactory
from parsers.serializers.jsonPC import JsonSerializerCreator

factory = SerializerFactory()

def hello(name):
    print(f"hello, {name}!")


abc = 'World'

def hello_world(greeting):
    return f"{greeting}, {abc}!"

class TestJson(unittest.TestCase):
    parser = factory.get_serializer('json')
    serializer = 'json'

    def test_simple_lists_and_tuples(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, '2', 3, '4', 5]
        list3 = [None, 1, '2, 3', False, 98.04]
        tuple1 = (1, 4, 'format', 80, 'json')
        tuple2 = (None, None, 'temp', True, 'rocks')
        tuple3 = ()
        self.assertEqual(self.parser.loads(self.parser.dumps(list1)), list1)
        self.assertEqual(self.parser.loads(self.parser.dumps(list2)), list2)
        self.assertEqual(self.parser.loads(self.parser.dumps(list3)), list3)
        self.assertEqual(tuple(self.parser.loads(self.parser.dumps(tuple1))), tuple1)
        self.assertEqual(tuple(self.parser.loads(self.parser.dumps(tuple2))), tuple2)
        self.assertEqual(tuple(self.parser.loads(self.parser.dumps(tuple3))), tuple3)

    def test_simple_dictionaries(self):
        dict1 = {}
        dict2 = {'1': 'Mon', '2': 'Tue', '3': 'Wed', '4': 'Thu', '5': 'Fri', '6': 'Sat', '7': 'Sun'}
        dict3 = {'Pi': 3.1415, 'Exp': 1.71}
        dict4 = {'Table1': [1, 2, 4], 'Table2': [8, -2, 2.33]}
        self.assertEqual(self.parser.loads(self.parser.dumps(dict1)), dict1)
        self.assertEqual(self.parser.loads(self.parser.dumps(dict2)), dict2)
        self.assertEqual(self.parser.loads(self.parser.dumps(dict3)), dict3)
        self.assertEqual(self.parser.loads(self.parser.dumps(dict4)), dict4)


def hello(name):
    print(f"hello, {name}!")

abc = 'World'


def hello_world(greeting):
    return f"{greeting}, {abc}!"


class TestDump(unittest.TestCase):
    def setUp(self):
        self.serializers = [JsonSerializerCreator(), YamlSerializerCreator(),
                            TomlSerializerCreator(), PickleSerializerCreator()]

    def test_dict_dumps(self):
        self.results = ["{'name':'Sarah', 'age':12}", 'age: 12\nname: Sarah\n',
                        'name = "Sarah"\nage = 12\n', '(dp0\nVname\np1\nVSarah\np2\nsVage\np3\nI12\ns.']

        for item in zip(self.serializers, self.results):
            serializer = item[0].create_serializer()
            with self.subTest(case=serializer):
                self.assertEqual(serializer.dumps({'name': 'Sarah', 'age': 12}), item[1])

    def test_list_dumps(self):
        self.results = ["[ 'name', 'age', {'family':'Bob'}, [ 'car' ] ]", ['name', 'age', {'family': 'Bob'}, ['car']],
                        ['name', 'age', {'family': 'Bob'}, ['car']], ['name', 'age', {'family': 'Bob'}, ['car']]]

        for item in zip(self.serializers, self.results):
            serializer = item[0].create_serializer()
            with self.subTest(case=serializer):
                self.assertEqual(serializer.dumps(['name', 'age', {'family': 'Bob'}, ['car']]), item[1])

    def test_func_dumps(self):
        self.results = [
            """{'type':'function', 'name':'hello', 'code':'def hello(name):\n    print(f"hello, {name}!")\n\', \'globals\':{}}""",
            """code: "def hello(name):\\n    print(f\\"hello, {name}!\\")\\n"\nglobals: {}\nname: hello\ntype: function\n""",
            'type = "function"\nname = "hello"\ncode = "def hello(name):\\n    print(f\\"hello, {name}!\\")\\n"\n\n[globals]\n',
            '(dp0\nVtype\np1\nVfunction\np2\nsVname\np3\nVhello\np4\nsVcode\np5\nVdef hello(name):\\u000a    print(f"hello, {name}!")\\u000a\np6\nsVglobals\np7\n(dp8\ns.']

        for item in zip(self.serializers, self.results):
            serializer = item[0].create_serializer()
            with self.subTest(case=serializer):
                self.assertEqual(serializer.dumps(hello), item[1])

    def test_func_dump(self):
        self.results = [
            """{'type':'function', 'name':'hello', 'code':'def hello(name):\n    print(f"hello, {name}!")\n\', \'globals\':{}}""",
            """code: "def hello(name):\\n    print(f\\"hello, {name}!\\")\\n"\nglobals: {}\nname: hello\ntype: function\n""",
            'type = "function"\nname = "hello"\ncode = "def hello(name):\\n    print(f\\"hello, {name}!\\")\\n"\n\n[globals]\n',
            '(dp0\nVtype\np1\nVfunction\np2\nsVname\np3\nVhello\np4\nsVcode\np5\nVdef hello(name):\\u000a    print(f"hello, {name}!")\\u000a\np6\nsVglobals\np7\n(dp8\ns.']

        for item in zip(self.serializers, self.results):
            serializer = item[0].create_serializer()
            with self.subTest(case=serializer):
                self.assertEqual(serializer.dump(hello, 'file.txt'), item[1])

    def test_get_dict_from_text(self):
        self.results = [
            """{'type':'function', 'name':'hello', 'code':'def hello(name):\n    print(f"hello, {name}!")\n\', \'globals\':{}}""",
            """code: "def hello(name):\\n    print(f\\"hello, {name}!\\")\\n"\nglobals: {}\nname: hello\ntype: function\n""",
            'type = "function"\nname = "hello"\ncode = "def hello(name):\\n    print(f\\"hello, {name}!\\")\\n"\n\n[globals]\n',
            '(dp0\nVtype\np1\nVfunction\np2\nsVname\np3\nVhello\np4\nsVcode\np5\nVdef hello(name):\\u000a    print(f"hello, {name}!")\\u000a\np6\nsVglobals\np7\n(dp8\ns.']
        for item in zip(self.serializers, self.results):
            serializer = item[0].create_serializer()
            self.assertEqual(serializer.get_dict(item[1])['type'], 'function')


class TestLoad(unittest.TestCase):
    def setUp(self):
        self.serializers = [JsonSerializerCreator(), YamlSerializerCreator(),
                            TomlSerializerCreator(), PickleSerializerCreator()]

    def test_lambda_loads(self):
        for item in self.serializers:
            serializer = item.create_serializer()
            with self.subTest(case=serializer):
                _lambda = lambda x: x * x
                lambda_dict = serializer.dumps(_lambda)
                serializer.dump(_lambda, 'lambda.txt')
                self.assertEqual(serializer.loads(lambda_dict)(5), _lambda(5))
                self.assertEqual(serializer.load('lambda.txt')(5), _lambda(5))

    def test_dict_loads(self):
        for item in self.serializers:
            serializer = item.create_serializer()
            with self.subTest(case=serializer):
                test_dict = {'name': 'Sarah', 'age': 12}
                dct = serializer.dumps(test_dict)
                result = serializer.loads(dct)
                self.assertDictEqual(result, test_dict)

    def test_func_loads(self):
        for item in self.serializers:
            serializer = item.create_serializer()
            with self.subTest(case=serializer):
                func_dict = serializer.dumps(hello_world)
                self.assertEqual(serializer.loads(func_dict)('Hello'), 'Hello, World!')

class TestExJsonSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = JsonSerializerCreator()
        self.test_cases_from_json = ["    {'name':'Sarah', 'age':11}", "('name':'Sarah', 'age':11}",
                                     "!{'name':'Sarah', 'age':11}", "trash{'name':'Sarah', 'age':11}"]
        self.test_cases_to_dist = ["{'name':'Sarah', 'age':11", "('name:'Sarah', 'age':11}"]

    def test_from_json_throws_ex(self):
        for case in self.test_cases_from_json:
            with self.subTest(case=case):
                self.assertRaises(IOError, lambda: from_json(case))

    def test_to_dict_returns_none(self):
        for case in self.test_cases_to_dist:
            with self.subTest(case=case):
                self.assertEqual(None, _json_to_dict(case, 0))

    def test_to_dict_throws_ex(self):
        for case in self.test_cases_to_dist:
            with self.subTest(case=case):
                self.assertRaises(IOError, lambda: _json_to_dict(case, 100))

    def test_to_list_throws_ex(self):
        for case in self.test_cases_to_dist:
            with self.subTest(case=case):
                self.assertRaises(IOError, lambda: _json_to_list(case, 100))

    def test_to_basic_throws_ex(self):
        for case in self.test_cases_to_dist:
            with self.subTest(case=case):
                self.assertRaises(IOError, lambda: _json_to_basic(case, 100))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestJson('test_simple_lists_and_tuples'))
    suite.addTest(TestJson('test_simple_dictionaries'))
    suite.addTest(TestDump('test_dict_dumps'))
    suite.addTest(TestDump('test_func_dumps'))
    suite.addTest(TestDump('test_get_dict_from_text'))
    suite.addTest(TestDump('test_list_dumps'))
    suite.addTest(TestLoad('test_dict_loads'))
    suite.addTest(TestLoad('test_lambda_loads'))
    suite.addTest(TestLoad('test_func_loads'))
    suite.addTest(TestLoad('test_load'))
    suite.addTest(TestExJsonSerializer('test_from_json_throws_ex'))
    suite.addTest(TestExJsonSerializer('test_to_dict_returns_none'))
    suite.addTest(TestExJsonSerializer('test_to_dict_throws_ex'))
    suite.addTest(TestExJsonSerializer('test_to_basic_throws_ex'))
    return suite


def run_tests():
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    runner.run(test_suite())