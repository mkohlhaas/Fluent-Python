"""
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__  # doctest: +ELLIPSIS
(<cell at 0x...: list object at 0x...>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
"""

from collections.abc import Callable


DEMO = """
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
"""


# def make_averager():
#     series: list[float] = []
#
#     def averager(new_value: float):
#         series.append(new_value)
#         total = sum(series)
#         return total / len(series)
#
#     return averager


def make_averager() -> Callable[[float], float]:
    count: float = 0
    total: float = 0

    def averager(new_value: float):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager
