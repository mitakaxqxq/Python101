from collections import Iterable


def deep_find_all_dfs(data, key):
    result_of_dfs = []

    def helper(data, key):
        if not isinstance(data, dict):
            raise AttributeError('Main data must be dictionary!')

        for data_key, data_value in data.items():
            if data_key == key:
                result_of_dfs.append(data_value)

            if isinstance(data_value, dict):
                helper(data_value, key)
            elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
                for elem in data_value:
                    if not isinstance(elem, dict):
                        raise AttributeError("Type of iterable objects's values must be dictionaries!")
                    helper(elem, key)
        return result_of_dfs
    return helper(data, key)


def deep_find_all_bfs(data, key):
    result_of_bfs = []
    if not isinstance(data, dict):
        raise AttributeError('Main data must be dictionary!')
    list_data = list(data.items())
    while list_data:
        data_key, data_value = list_data.pop(0)
        if data_key == key:
            result_of_bfs.append(data_value)

        if isinstance(data_value, dict):
            list_data.extend(data_value.items())
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                list_data.extend(value.items())
    return result_of_bfs
