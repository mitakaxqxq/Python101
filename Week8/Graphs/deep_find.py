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
        if data_key == key:
            return data_value

        if isinstance(data_value, dict):
            for value in list(data_value.items()):
                list_data.append(value)
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                for elem in list(value.items()):
                    list_data.append(elem)
    return False


print(deep_find_bfs({1: [{3: 4, 5: 6}, {7: 229}], 2: 1}, 7))
