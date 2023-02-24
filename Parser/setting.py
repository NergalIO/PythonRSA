from Errors.parser import *
from Environment.env import *

def ParseSettings() -> dict[str, any]:
    with open("settings", "r") as setting_file:
        return setting_file.readlines()

def GetSettingsDict() -> dict[str, any]:
    settings = {}
    data = ParseSettings()
    for line in data:
        line = line.split("#")[0]
        if StringIsEmptyOrWhitespace(line): continue
        setting, value = line.split('=')
        value = [v.strip('[]()\n') for v in value.split(',')] if value != '' else None
        settings[setting] = value
    return settings
    

def ValidateSettings(settings: dict[set, any]) -> tuple[bool, Exception]:
    available_settings = ["resolution", "keylength"]
    for setting, value in settings.items():
        if not setting in available_settings: 
            return (InvalidSetting(f"{setting} is not available option!"), False) 
        if value is None:
            return (InvalidSettingValue(f"{setting} can't have value {value}!"), False)
    return (None, True)
        

def Parse() -> dict[str, any]:
    settings = GetSettingsDict()
    validate_result = ValidateSettings(settings)
    if not validate_result[1]:
        raise validate_result[1]
    return settings