def rank_and_basis(A):
    m = len(A)
    n = len(A[0]) if m > 0 else 0
    M = [row[:] for row in A]
    pivot_cols = []
    pivot_row = 0

    for col in range(n):
        if pivot_row >= m: break
        
        # Pivoting
        max_val, max_idx = 0, pivot_row
        for i in range(pivot_row, m):
            if abs(M[i][col]) > max_val:
                max_val = abs(M[i][col])
                max_idx = i
                
        if max_val < 1e-9:
            for i in range(pivot_row, m): M[i][col] = 0.0
            continue

        if max_idx != pivot_row:
            M[pivot_row], M[max_idx] = M[max_idx], M[pivot_row]

        pivot_cols.append(col)

        # Chuẩn hóa RREF
        pivot = M[pivot_row][col]
        for j in range(col, n):
            M[pivot_row][j] /= pivot

        for i in range(m):
            if i != pivot_row:
                factor = M[i][col]
                for j in range(col, n):
                    M[i][j] -= factor * M[pivot_row][j]
        pivot_row += 1

    rank = len(pivot_cols)

    # Cơ sở không gian dòng (các dòng khác 0 của RREF)
    row_basis = [M[i] for i in range(rank)]

    # Cơ sở không gian cột (các cột tương ứng với pivot từ ma trận GỐC A)
    col_basis = [[A[i][j] for i in range(m)] for j in pivot_cols]

    # Cơ sở không gian nghiệm (Ax = 0)
    free_cols = [j for j in range(n) if j not in pivot_cols]
    null_basis = []
    for free_var in free_cols:
        vec = [0.0] * n
        vec[free_var] = 1.0
        for i, p_col in enumerate(pivot_cols):
            vec[p_col] = -M[i][free_var]
        null_basis.append(vec)

    return rank, row_basis, col_basis, null_basis