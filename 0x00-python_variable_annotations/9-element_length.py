#!/usr/bin/env python3
"""
Import the necessary module.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples,
    """
    return [(i, len(i)) for i in lst]
