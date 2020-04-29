def equalize_list(my_list):
    result = []

    def helper(my_list):
        for elem in my_list:
            if isinstance(elem, list):
                helper(elem)
            else:
                result.append(elem)
        return result

    return helper(my_list)


def equalize_dict(my_dict):
    result = []

    def helper(my_dict):
        for key, value in my_dict.items():
            result.append(key)
            if isinstance(value, dict):
                helper(value)
        return result

    return helper(my_dict)


def schema_validator(schema, data):
    if not isinstance(schema, list):
        raise TypeError('Schema must be list!')

    if not isinstance(data, dict):
        raise TypeError('Data must be dictionary!')

    equalized_schema = equalize_list(schema)
    equalized_data = equalize_dict(data)

    equalized_schema.sort()
    equalized_data.sort()

    if equalized_data == equalized_schema:
        return True
    else:
        return False
