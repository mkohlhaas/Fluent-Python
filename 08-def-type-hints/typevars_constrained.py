from typing import TypeVar, TYPE_CHECKING
from decimal import Decimal

RT = TypeVar("RT", float, Decimal)


def triple1(a: RT) -> RT:
    return a * 3


res1 = triple1(2)

if TYPE_CHECKING:
    pass
    # reveal_type(res1)

BT = TypeVar("BT", bound=float)


def triple2(a: BT) -> BT:
    return a * 3


res2 = triple2(2)

if TYPE_CHECKING:
    pass
    # reveal_type(res2)
