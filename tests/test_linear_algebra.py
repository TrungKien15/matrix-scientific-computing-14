# =========================
# TEST: m < n (ít phương trình, nhiều ẩn)
# =========================
def test_m_less_n_infinite():
    A = [[1, 2, 3]]   # 1 phương trình, 3 ẩn
    b = [4]

    result = gaussian_eliminate(A, b)

    assert result == "infinite solutions"


# =========================
# TEST: m > n (dư phương trình nhưng phụ thuộc)
# =========================
def test_m_greater_n_infinite():
    A = [[1, 2],
         [2, 4],
         [3, 6]]   # các hàng phụ thuộc nhau
    b = [3, 6, 9]

    result = gaussian_eliminate(A, b)

    assert result == "infinite solutions"


# =========================
# TEST: m > n (mâu thuẫn → vô nghiệm)
# =========================
def test_m_greater_n_no_solution():
    A = [[1, 2],
         [2, 4],
         [3, 6]]
    b = [3, 6, 10]   # mâu thuẫn

    result = gaussian_eliminate(A, b)

    assert result == "no solution"