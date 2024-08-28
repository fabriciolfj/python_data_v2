import math
from typing import List

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * value for value in v]


def vector_mean(v: List[Vector]) -> Vector:
    size = len(v)

    return scalar_multiply(1 / size, vector_sum(v))


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "vectors cannot be empty"

    num_elements = len(vectors[0])
    assert all(len(vector) == num_elements for vector in vectors), "vectors must have the same length"

    for i in range(num_elements):
        for vector in vectors:
            print(vector[i])

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


#soma os produtos pares de elementos correspondentes
def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be the same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

# calcular a distancia entre 2 pontos
print(distance([8, 9], [3, 5]))
