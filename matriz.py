from typing import List

Matrix = List[List[float]]
Vector = List[float]


def get_row(m: Matrix, row: int) -> Vector:
    return m[row]


def get_col(m: Matrix, col: int) -> Vector:
    return [A_i[col] for A_i in m]


A = [[1, 2],
     [3, 4],
     [5, 6]]



print(get_col(A, 1))