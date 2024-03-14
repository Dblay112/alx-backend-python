#!/usr/bin/env python3
"""
Import the necessary module.
"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function to sum elements in a list of integers and floats.

    Args:
        mxd_lst: list containing integers or floats

    Returns:
        The sum of all elements in the list (float)
    """
    total = 0.0
    for number in mxd_lst:
        total += number
    return total
