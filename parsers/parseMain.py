import inspect
from collections import namedtuple
from types import FuncType, CodeType
import builtins

class Parser:
    def dump(self, obj, file_path):
        with open(file_path, 'w') as file:
            file.write(self.dumps(obj))

    def dumps(self, obj):
        if inspect.isfunc(obj):
            return func_dict(self, obj)
        else:
            return obj_dict(self, obj)

    def load(self, file_path):
        with open(file_path, 'r') as file:
            object = self.loads(file.read())

        return object

    def loads(self, obj_dict):
        if 'code' in obj_dict:
            return dict_func(self, obj_dict)
        else:
            return dict_obj(self, obj_dict)

def isbase(obj):
    return type(obj) in [int, float, str, bool, type(None)]

def obj_dict(self, obj):
    if isbase(obj):
        return obj
    elif isinstance(obj, list):
        lst = list()
        for item in obj:
            lst.append(self.object_to_dict(item))
        return lst
    elif isinstance(obj, dict):
        return self_dict(self, obj)
    else:
        return self_dict(self, obj.__dict__)

def self_dict(self, dict_obj):
    obj_dict = dict()
    for (key, value) in dict_obj.items():
        if isbase(value):
            obj_dict[key] = value
        else:
            obj_dict[key] = self.object_to_dict(value)

    return obj_dict

def dict_obj(self, dict_obj):
    if isbase(dict_obj):
        return dict_obj
    elif isinstance(dict_obj, list):
        lst = list()
        for item in dict_obj:
            lst.append(self.dict_to_object(item))
        return lst

    else:
        temp = dict()
        for (key, value) in dict_obj.items():
            if not isbase(value):
                temp[key] = self.dict_to_object(value)
            else:
                temp[key] = value

        return namedtuple('object', temp.keys())(*temp.values())

def func_dict(self, func_obj):
    func = dict()

    func_code = dict()
    code_pairs = inspect.getmembers(func_obj.__code__)
    for (key, value) in code_pairs:
        if str(key).startswith('co_'):
            if isinstance(value, bytes):
                value = (list(value))
            func_code[key] = value
    func['code'] = func_code
    func_gl = dict()
    name = func['code']['co_name']
    func_gl[name] = name + '<func>'
    global_pairs = func_obj.__globals__.items()
    for (key, value) in global_pairs:
        if isbase(value):
            func_gl[key] = value
    func['globals'] = func_gl

    return func

def dict_func(self, dict_func):
    func_gl = dict_func['globals']
    func_gl['__builtins__'] = builtins
    code_args = dict_func['code']

    func_code = CodeType(code_args['co_argcount'],
                             code_args['co_posonlyargcount'],
                             code_args['co_kwonlyargcount'],
                             code_args['co_nlocals'],
                             code_args['co_stacksize'],
                             code_args['co_flags'],
                             bytes(code_args['co_code']),
                             tuple(code_args['co_consts']),
                             tuple(code_args['co_names']),
                             tuple(code_args['co_varnames']),
                             code_args['co_filename'],
                             code_args['co_name'],
                             code_args['co_firstlineno'],
                             bytes(code_args['co_lnotab']),
                             tuple(code_args['co_freevars']),
                             tuple(code_args['co_cellvars']))

    temp = FuncType(func_code, func_gl, code_args['co_name'])
    name = code_args['co_name']
    func_gl[name] = temp
    return FuncType(func_code, func_gl, name)