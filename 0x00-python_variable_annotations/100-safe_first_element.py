#!/usr/bin/env python3

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Returns the first element of lst if it exists, otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None