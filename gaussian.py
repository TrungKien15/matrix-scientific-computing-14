import math

def back_substitution(U, c):
    """Giải hệ tam giác trên Ux = c."""
    m = len(U)
    n = len(U[0]) if m > 0 else 0
    
    for i in range(m):
        all_zero = all(abs(U[i][j]) < 1e-9 for j in range(n))
        if all_zero and abs(c[i]) > 1e-9:
            return "no_solution"

    non_zero_rows = sum(1 for i in range(m) if any(abs(U[i][j]) >= 1e-9 for j in range(n)))
    if non_zero_rows < n:
        return "infinite"

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (c[i] - s) / U[i][i]
        
    return x

def gaussian_eliminate(A, b):
    """Trả về ma trận sau khi khử (M), nghiệm (x), số lần hoán đổi (swaps)."""
    m = len(A)
    n = len(A[0]) if m > 0 else 0
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    swaps = 0
    pivot_row = 0
    
    for col in range(n):
        if pivot_row >= m: break
            
        max_val, max_idx = 0, pivot_row
        for i in range(pivot_row, m):
            if abs(M[i][col]) > max_val:
                max_val = abs(M[i][col])
                max_idx = i
                
        if max_val < 1e-9: continue
            
        if max_idx != pivot_row:
            M[pivot_row], M[max_idx] = M[max_idx], M[pivot_row]
            swaps += 1
            
        for i in range(pivot_row + 1, m):
            if abs(M[i][col]) < 1e-9: continue
            factor = M[i][col] / M[pivot_row][col]
            for j in range(col, n + 1):
                M[i][j] -= factor * M[pivot_row][j]
                
        pivot_row += 1
        
    U_after = [row[:-1] for row in M]
    c_after = [row[-1] for row in M]
    x = back_substitution(U_after, c_after)
    
    return M, x, swaps