"""
TV1 must implement:

gaussian_eliminate(A, b)

Requirements:
- Return nghiệm nếu có nghiệm duy nhất (list)
- Return "no solution" nếu vô nghiệm
- Return "infinite solutions" nếu vô số nghiệm
- Phải có partial pivoting
"""

# =========================
# TEST 1: nghiệm duy nhất
# =========================
def test_unique_solution():
    A = [[2, 1],
         [1, 3]]
    b = [5, 6]

    expected = [1, 2]

    x = gaussian_eliminate(A, b)

    assert all(abs(x[i] - expected[i]) < 1e-6 for i in range(2))


# =========================
# TEST 2: vô nghiệm
# =========================
def test_no_solution():
    A = [[1, 2],
         [2, 4]]
    b = [3, 7]

    result = gaussian_eliminate(A, b)

    assert result == "no solution"


# =========================
# TEST 3: vô số nghiệm
# =========================
def test_infinite_solution():
    A = [[1, 2],
         [2, 4]]
    b = [3, 6]

    result = gaussian_eliminate(A, b)

    assert result == "infinite solutions"


# =========================
# TEST 4: m < n
# =========================
def test_m_less_n():
    A = [[1, 2, 3]]
    b = [4]

    result = gaussian_eliminate(A, b)

    assert result == "infinite solutions"


# =========================
# TEST 5: m > n
# =========================
def test_m_greater_n():
    A = [[1, 2],
         [2, 4],
         [3, 6]]
    b = [3, 6, 9]

    result = gaussian_eliminate(A, b)

    assert result == "infinite solutions"


# =========================
# TEST 6: partial pivoting
# =========================
def test_partial_pivoting():
    A = [[0, 1],
         [1, 2]]
    b = [1, 3]

    x = gaussian_eliminate(A, b)

    assert x is not None


# =========================
# TEST 7: pivot = 0
# =========================
def test_zero_pivot():
    A = [[0, 0],
         [0, 1]]
    b = [0, 1]

    result = gaussian_eliminate(A, b)

    assert "không có pivot" in result


# =========================
# TEST 8: số thực
# =========================
def test_float_values():
    A = [[0.5, 1.5],
         [1.0, 3.0]]
    b = [2.0, 4.0]

    result = gaussian_eliminate(A, b)

    assert result == "infinite solutions"


# =========================
# TEST 9: ma trận lớn hơn
# =========================
def test_larger_matrix():
    A = [[1, 2, 3],
         [0, 1, 4],
         [5, 6, 0]]
    b = [7, 8, 9]

    x = gaussian_eliminate(A, b)

    assert x is not None