OPEN_DICTIONARY_BRACE = '{'
OPEN_LIST_BRACE = '['
CLOSED_LIST_BRACE = ']'
CLOSED_DICTIONARY_BRACE = '}'
QUOTE = "\""


def from_json(text):
    result = None
    if not isinstance(text, str):
        raise TypeError()
    if text[0] == OPEN_DICTIONARY_BRACE:
        result = to_dict(text[1:-1])
    elif text[0] == OPEN_LIST_BRACE:
        result = to_array(text[1:-1])
    else:
        result = to_basic(text)
    return result


def to_basic(text):
    if text[0] == QUOTE:
        return str(text[1:-1])
    elif text == "true":
        return True
    elif text == "false":
        return False
    elif text == "null":
        return None
    else:
        return int(text)


def to_dict(text):
    result = {}
    i = 0
    j = 0
    value = None
    while i != len(text):
        while text[i] != ':':
            i += 1
            if i != len(text) and text[i] == OPEN_LIST_BRACE:
                raise TypeError()
        key = to_basic(text[j:i])
        j = i
        while j != (len(text)) and text[j] != ',':
            j += 1
            if j != (len(text)) and text[j] == OPEN_LIST_BRACE:
                k = j
                while text[k] != CLOSED_LIST_BRACE:
                    k += 1
                value = to_array(text[j + 1:k])
                j = k
        if value is None:
            value = to_basic(text[i + 2:j])  # тк ": " занимают 2 символа
        result[key] = value
        value = None
        i = j
        j += 2  # тк ", " занимают 2 символа
    return result


def to_array(text):
    result = []
    i = 0
    j = 0
    value = None
    while i < len(text):
        while i != len(text) and text[i] != ',':
            if i != (len(text)) and text[i] == OPEN_LIST_BRACE:
                k = i
                while text[k] != CLOSED_LIST_BRACE:
                    k += 1
                value = to_array(text[i + 1:k])
            if i != (len(text)) and text[i] == OPEN_DICTIONARY_BRACE:
                k = i
                while text[k] != CLOSED_DICTIONARY_BRACE:
                    k += 1
                value = to_dict(text[i + 1:k])
            i += 1
        value = to_basic(text[j:i])
        result.append(value)
        i += 2
        j = i
    return result

