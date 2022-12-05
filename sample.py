from typing import List, Optional, Union


def add_all(foo: List[int]) -> Optional[int]:
    if isinstance(foo, list):
        return sum(foo)
    return None


def add_all2(foo: List[int]) -> int | None:
    if isinstance(foo, list):
        return sum(foo)
    return None


def add_all3(foo: List[int]) -> Union[int, None]:
    if isinstance(foo, list):
        return sum(foo)
    return None


result = add_all([1, 2, 3, 4])
print(result)
