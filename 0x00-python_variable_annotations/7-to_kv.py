#!/usr/bin/env python3
"""
Import the necessary module.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from a string key and an
    integer/float value, returning the squared value.

    Args:
        k: The string key (str).
        v: The integer or float value (Union[int, float]).

    Returns:
    A tuple containing the string key and the
    square of the value as a float (Tuple[str, float]).
    """
    return k, v**2
