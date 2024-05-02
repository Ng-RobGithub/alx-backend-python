#!/usr/bin/env python3

from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements from lst and their lengths."""
    return [(i, len(i)) for i in lst]