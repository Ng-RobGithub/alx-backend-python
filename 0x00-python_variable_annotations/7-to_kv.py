#!/usr/bin/env python3

"""Module-level documentation."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing a string and the square of an int or float.
    """
    return (k, v ** 2)
