from part1.gaussian import gaussian_eliminate

def determinant(A):
    m = len(A)
    n = len(A[0]) if m > 0 else 0
    
    if m != n or m == 0:
        return None # Chỉ tính định thức cho ma trận vuông
        
    # Tạo vector b giả (toàn 0) để tận dụng hàm gaussian_eliminate
    b = [0.0] * m
    M, _, swaps = gaussian_eliminate(A, b)
    
    # Tính tích các phần tử trên đường chéo chính
    det = (-1) ** swaps
    for i in range(n):
        det *= M[i][i]
        
    return det