#!/usr/bin/env python3
"""
Import the necessary module.
"""


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
        """Inner function that performs the multiplication.

        Args:
            number: The float to be multiplied by
            the outer multiplier

        Returns:
           number and the outer multiplier multiplied together
        """
        return number * multiplier

    return innerFunction