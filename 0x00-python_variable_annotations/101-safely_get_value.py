#!/usr/bin/env python3

from typing import Mapping, Any, TypeVar, Union

# Define a type variable for the value type
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """Returns the value associated with the given key in the dictionary.
    If the key is not present, returns the default value."""
    if key in dct:
        return dct[key]
    else:
        return default