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
            for value in list(data_value.items()):
                list_data.append(value)
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                if not isinstance(value, dict):
                    raise AttributeError("Type of iterable objects's values must be dictionaries!")
                for elem in list(value.items()):
                    list_data.append(elem)
    return result_of_bfs


print(deep_find_all_bfs({1: 2, 3: 4, 5: [{4: 2, 5: 8}, {4: 229, 7: 89}], 4: 98}, 4))
