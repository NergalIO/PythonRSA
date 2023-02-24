def StringIsEmpty(string: str) -> bool:
    return len(string) == 0

def StringIsEmptyOrWhitespace(string: str) -> bool:
    string = string.replace(' ', '')
    return len(string) == 0

def GetKeyFromDictWithValue(dict: dict[str, any], value: any) -> any:
    for key, value in dict.items():
        if value == value:
            return key

def AnyStrToInt(obj: str | list):
    if type(obj) == list:
        result = []
        for item in obj:
            result.append(int(item))
        return result
    elif type(obj) == str:
        return int(obj)
