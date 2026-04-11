def inverse(A):
    n = len(A)
    if n == 0 or len(A[0]) != n:
        return None

    # Tạo ma trận tăng cường [A | I]
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]

    for i in range(n):
        # Partial pivoting
        max_val, max_idx = 0, i
        for k in range(i, n):
            if abs(M[k][i]) > max_val:
                max_val = abs(M[k][i])
                max_idx = k
                
        if max_val < 1e-9:
            return None # Ma trận suy biến, không có nghịch đảo

        if max_idx != i:
            M[i], M[max_idx] = M[max_idx], M[i]

        # Chuẩn hóa dòng pivot (chia cho phần tử chốt để pivot = 1)
        pivot = M[i][i]
        for j in range(i, 2 * n):
            M[i][j] /= pivot

        # Khử các dòng khác (cả trên và dưới)
        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(i, 2 * n):
                    M[k][j] -= factor * M[i][j]

    # Trích xuất ma trận nghịch đảo từ nửa bên phải
    inv_A = [row[n:] for row in M]
    return inv_A