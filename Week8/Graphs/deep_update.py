from collections import Iterable


def deep_update(data, key, val):
    if not isinstance(data, dict):
        raise AttributeError('Main data must be dictionary!')

    new_dict = {}
    for data_key, data_value in data.items():
        if isinstance(data_value, dict):
            result = deep_update(data_value, key, val)
            new_dict[data_key] = result
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            helping_list = []
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                result = deep_update(value, key, val)
                helping_list.append(result)
                if isinstance(data_value, list):
                    if data_key == key:
                        new_dict[val] = helping_list
                    else:
                        new_dict[data_key] = helping_list
                elif isinstance(data_value, tuple):
                    if data_key == key:
                        new_dict[val] = tuple(helping_list)
                    else:
                        new_dict[data_key] = tuple(helping_list)
        else:
            if data_key == key:
                new_dict[val] = data_value
            else:
                new_dict[data_key] = data_value
    return new_dict
