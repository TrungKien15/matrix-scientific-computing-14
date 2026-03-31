import pytest
from part1.gaussian import gaussian_eliminate


def test_m_less_n_infinite():
    A = [[1, 2, 3]]
    b = [4]

    result_type, _ = gaussian_eliminate(A, b)

    assert result_type == "infinite"


def test_m_greater_n_no_solution():
    A = [
        [1, 1],
        [2, 2],
        [1, 1]
    ]
    b = [2, 4, 3]

    result_type, _ = gaussian_eliminate(A, b)

    assert result_type == "no_solution"


def test_square_unique():
    A = [
        [2, 1],
        [1, -1]
    ]
    b = [3, 0]

    result_type, x = gaussian_eliminate(A, b)

    assert result_type == "unique"

    assert abs(2*x[0] + x[1] - 3) < 1e-6
    assert abs(x[0] - x[1] - 0) < 1e-6


def test_zero_pivot():
    A = [
        [0, 1],
        [1, 2]
    ]
    b = [1, 3]

    result_type, _ = gaussian_eliminate(A, b)

    assert result_type == "unique"


def test_simple_no_solution():
    A = [
        [1, 1],
        [1, 1]
    ]
    b = [2, 3]

    result_type, _ = gaussian_eliminate(A, b)

    assert result_type == "no_solution"
