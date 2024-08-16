#https://www.tryexponent.com/practice/prepare/flatten-a-dictionary
from typing import Dict, Union

DeepNestedDict = Dict[str, Union[str, 'DeepNestedDict']]

def flatten_dictionary(dictionary: DeepNestedDict) -> Dict[str, str]:
    flatDict = {}

    flatDictionaryHelper("", dictionary, flatDict)
    return flatDict

def flatDictionaryHelper(currentKey, valDict, flatDict):
    for key, value in valDict.items():
        # Compute the new key with current prefix
        newKey = f"{currentKey}.{key}" if currentKey and key else currentKey or key
        if isinstance(value, dict):
            # Recurse into nested dictionary
            flatDictionaryHelper(newKey, value, flatDict)
        else:
            # Assign value to the flattened dictionary
            flatDict[newKey] = value
  
# debug your code below
dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

print(flatten_dictionary(dict_input))
