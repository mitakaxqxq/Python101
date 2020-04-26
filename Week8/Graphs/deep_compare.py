from collections import Iterable


def deep_compare(obj1, obj2):
    if not isinstance(obj1, dict) and not isinstance(obj2, dict):
        if isinstance(obj1, tuple) and isinstance(obj2, tuple):
            return obj1 == obj2
        if isinstance(obj1, Iterable) and isinstance(obj2, Iterable):
            if isinstance(obj1, type(obj2)):
                if not isinstance(obj1, str) and not isinstance(obj2, str):
                    for elem1 in obj1:
                        for elem2 in obj2:
                            deep_compare(elem1, elem2)
                elif isinstance(obj1, str) and isinstance(obj2, str):
                    return obj1 == obj2
                else:
                    return False
    else:
        for data_key in obj1.keys():
            if data_key not in obj2.keys():
                return False
            else:
                if isinstance(obj1[data_key], dict) and isinstance(obj2[data_key], dict):
                    deep_compare(obj1[data_key], obj2[data_key])
                elif isinstance(obj1[data_key], Iterable) and isinstance(obj2[data_key], Iterable):
                    if isinstance(obj1[data_key], type(obj2[data_key])):
                        if not isinstance(obj1[data_key], str) and not isinstance(obj2[data_key], str):
                            for elem1 in obj1[data_key]:
                                for elem2 in obj2[data_key]:
                                    deep_compare(elem1, elem2)
                        elif isinstance(obj1[data_key], str) and isinstance(obj2[data_key], str):
                            return obj1 == obj2
                        else:
                            return False
                    else:
                        return False
    return True
