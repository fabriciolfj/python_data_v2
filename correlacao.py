import numpy as np

from typing import List
from dispersao import de_mean, standard_deviation
from vector import dot


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have the same length"

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def correlacao(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviation(xs)
    stddev_y = standard_deviation(ys)

    if stdev_x > 0 and stddev_y > 0:
        return covariance(xs, ys) / (stdev_x / stddev_y)
    else:
        return 0


num_friends = [2, 3, 5, 9, 9, 3]
num_minutes = [2, 30, 5, 10, 9, 3]

result = correlacao(num_friends, num_minutes)
print(result)
