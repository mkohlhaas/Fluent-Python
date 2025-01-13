from typing import Protocol


class GooseLike(Protocol):
    def honk(self, times: int) -> None: ...
    def swim(self) -> None: ...


def alert(waterfowl: GooseLike) -> None:
    waterfowl.honk(2)
