#media da distribuição dos dados
# mais próximos de 0 nao estao espalhados, maiores que 0 indicam dados muito espalhados
import math
from statistics import mean
from typing import List
import numpy as np

from vector import sum_of_squares


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


#calculo da variancia
def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

num_friends = np.random.randint(0, 101, 100)


print(standard_deviation(num_friends))