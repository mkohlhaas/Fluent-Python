#!/usr/bin/env python

"""
>>> avg = Averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0

"""


class Averager:
    def __init__(self):
        self.series: list[float] = []

    def __call__(self, new_value: float):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
