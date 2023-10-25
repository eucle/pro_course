from typing import Any


def is_iterator(obj: Any) -> bool:
    return hasattr(obj, '__next__')
