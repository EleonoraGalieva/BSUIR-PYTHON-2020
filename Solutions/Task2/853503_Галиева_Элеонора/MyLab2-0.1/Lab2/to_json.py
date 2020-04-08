from Lab2_folder import decorator


@decorator.Memoized
def to_json(obj):
    result = ""
    if isinstance(obj, str):
        result += "\"{}\"".format(str(obj))
    elif isinstance(obj, bool):
        result += "{}".format(str(obj).lower())
    elif isinstance(obj, dict):
        result = to_object_in_json(obj)
    elif isinstance(obj, (int, float)):
        result = "{}".format(str(obj))
    elif isinstance(obj, (list, tuple)):
        result = to_array_in_json(obj)
    elif isinstance(obj, type(None)):
        result = "null"
    else:
        raise TypeError("Received object is not JSON serializable.")
    return result


def to_object_in_json(obj):
    braces = '{}'
    result = braces[0]
    for key, value in obj.items():
        if isinstance(key, list):
            raise TypeError("Unhashable type.")
        elif isinstance(key, tuple):
            raise TypeError("Keys must be str, int, float, bool or None, not tuple")
        elif isinstance(key, (str, int, float)):
            key = "\"{}\"".format(key)
        if isinstance(value, (list, tuple)):
            value = to_array_in_json(value)
        elif isinstance(value, str):
            value = "\"{}\"".format(value)
        else:
            value = str(value)
        result += '{}: '.format(key) + value + ', '
    result = result[:-2]
    result += braces[1]
    return result


def to_array_in_json(obj):
    braces = '[]'
    result = braces[0]
    for value in obj:
        if isinstance(value, str):
            result += "\"{}\"".format(str(value)) + ", "
        elif isinstance(value, bool):
            value = str(value).lower()
            result += "{}".format(str(value)) + ", "
        else:
            result += "{}".format(str(value)) + ", "
    result = result[:-2]
    result += braces[1]
    return result
