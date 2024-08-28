from collections import Counter

import numpy as np
from typing import List


def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[(len(xs) // 2)]


def _median_even(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(xs: List[float]) -> float:
    return _median_even(xs) if len(xs) % 2 == 0 else _median_odd(xs)


#separa uma pequena quantidade de dados com base na porcentagem
def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


# trazer os valores com mais frequencia
def mode(xs: List[float]) -> List[float]:
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2
assert quantile([1, 10, 2, 9, 5], 0.5) == 5


num_friends = np.random.randint(0, 101, 100)
print(mode(num_friends))