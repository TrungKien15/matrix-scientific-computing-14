import pytest
from part1.gaussian import gaussian_eliminate

# ======================
# 1. m < n (vô số nghiệm)
# ======================
def test_m_less_n_infinite():
    A = [[1, 2, 3]]
    b = [4]

    result = gaussian_eliminate(A, b)

    assert result["type"] == "infinite"


# ======================
# 2. m > n (vô nghiệm)
# ======================
def test_m_greater_n_no_solution():
    A = [
        [1, 1],
        [2, 2],
        [1, 1]
    ]
    b = [2, 4, 3]  # mâu thuẫn

    result = gaussian_eliminate(A, b)

    assert result["type"] == "no_solution"


# ======================
# 3. m > n (vô số nghiệm)
# ======================
def test_m_greater_n_infinite():
    A = [
        [1, 1],
        [2, 2],
        [3, 3]
    ]
    b = [2, 4, 6]

    result = gaussian_eliminate(A, b)

    assert result["type"] == "infinite"


# ======================
# 4. hệ vuông (1 nghiệm duy nhất)
# ======================
def test_square_unique():
    A = [
        [2, 1],
        [1, -1]
    ]
    b = [3, 0]

    result = gaussian_eliminate(A, b)

    assert result["type"] == "unique"

    x = result["solution"]

    # kiểm tra nghiệm
    assert abs(2*x[0] + x[1] - 3) < 1e-6
    assert abs(x[0] - x[1] - 0) < 1e-6


# ======================
# 5. test pivot = 0 (partial pivoting)
# ======================
def test_zero_pivot():
    A = [
        [0, 1],
        [1, 2]
    ]
    b = [1, 3]

    result = gaussian_eliminate(A, b)

    assert result["type"] == "unique"


# ======================
# 6. hệ vô nghiệm rõ ràng
# ======================
def test_simple_no_solution():
    A = [
        [1, 1],
        [1, 1]
    ]
    b = [2, 3]

    result = gaussian_eliminate(A, b)

    assert result["type"] == "no_solution"


# ======================
# 7. hệ lớn hơn (test ổn định)
# ======================
def test_3x3_unique():
    A = [
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]
    ]
    b = [7, 4, 3]

    result = gaussian_eliminate(A, b)

    assert result["type"] == "unique"

    x = result["solution"]

    assert abs(1*x[0] + 2*x[1] + 3*x[2] - 7) < 1e-6
    assert abs(0*x[0] + 1*x[1] + 4*x[2] - 4) < 1e-6
    assert abs(5*x[0] + 6*x[1] + 0*x[2] - 3) < 1e-6
