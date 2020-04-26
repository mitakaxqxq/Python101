from collections import Iterable


def deep_find_dfs(data, key):
    if not isinstance(data, dict):
        raise AttributeError('Main data must be dictionary!')

    for data_key, data_value in data.items():
        if data_key == key:
            return data_value

        if isinstance(data_value, dict):
            if deep_find_dfs(data_value, key) is not False:
                return deep_find_dfs(data_value, key)
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                if deep_find_dfs(value, key) is not False:
                    return deep_find_dfs(value, key)
    return False


def deep_find_bfs(data, key):
    if not isinstance(data, dict):
        raise AttributeError('Main data must be dictionary!')

    list_data = list(data.items())
    while list_data:
        data_key, data_value = list_data.pop(0)
        print(data_key, data_value)
        if data_key == key:
            return data_value

        if isinstance(data_value, dict):
            list_data.extend(data_value.items())
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                list_data.extend(value.items())
    return False
