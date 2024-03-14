#!/usr/bin/env python3
"""
Import the necessary module.
"""
import math


def floor(n: float) -> int:
    """Return floor of a floating-point number.

    Args:
        n: floating-point number to round down (float).

    Returns:
        largest integer less than or equal to n (int).
    """
    return int(math.floor(n))
