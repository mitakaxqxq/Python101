from collections import Iterable
from types import FunctionType


def my_func(x):
    if not isinstance(x, int):
        raise ValueError('Wrong value - x must be int!')
    return x + 2


def deep_apply(func, data):
    if not isinstance(func, FunctionType):
        raise AttributeError('Func must be of type function!')
    if not isinstance(data, dict):
        raise AttributeError('Main data must be dictionary!')

    new_dict = {}
    for data_key, data_value in data.items():
        if isinstance(data_value, dict):
            result = deep_apply(func, data_value)
            new_dict[func(data_key)] = result
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            helping_list = []
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                result = deep_apply(func, value)
                helping_list.append(result)
            if isinstance(data_value, list):
                new_dict[func(data_key)] = helping_list
            elif isinstance(data_value, tuple):
                new_dict[func(data_key)] = tuple(helping_list)
        else:
            new_dict[func(data_key)] = data_value
    return new_dict
