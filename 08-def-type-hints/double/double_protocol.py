from typing import TypeVar, Protocol

T = TypeVar("T")


class Repeatable(Protocol):
    def __mul__(self: T, other: int) -> T: ...


RT = TypeVar("RT", bound=Repeatable)


def double(n: RT) -> RT:
    return n * 2
