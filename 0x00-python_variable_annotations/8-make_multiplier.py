#!/usr/bin/env python3
"""
Import the necessary module.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that creates a new function that
    multiplies a float by the given multiplier.

    Args:
    multiplier: The float value to be used as
    the multiplier

    Returns:
    a function
    """
    

    def innerFunction(number: float) -> float:
        """Inner function that performs the multiplication"""
        return number * multiplier
    return innerFunction
