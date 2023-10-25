from typing import Any


def is_iterable(obj: Any) -> bool:
    return '__iter__' in dir(obj)
