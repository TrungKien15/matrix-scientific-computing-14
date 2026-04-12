import math
import numpy as np

from GAUSS import gaussian_eliminate 
from SVD import svd_decomposition

# --- CÁC HÀM TRỢ GIÚP ---
def vector_norm_2(v):
    """Tính chuẩn bậc 2 của vector"""
    return math.sqrt(sum(x**2 for x in v))

def compute_relative_error(A, x, b):
    """Tính sai số tương đối ||Ax - b|| / ||b||"""
    A_np = np.array(A)
    x_np = np.array(x)
    b_np = np.array(b)
    res = np.linalg.norm(A_np @ x_np - b_np)
    return res / np.linalg.norm(b_np)

# --- PHƯƠNG PHÁP 1: GAUSS  ---
def solve_using_gauss(A, b):
    # Sử dụng hàm gaussian_eliminate 
    _, x, _ = gaussian_eliminate(A, b)
    return x

# --- PHƯƠNG PHÁP 2: SVD  ---
def solve_using_svd(A, b):
    # Sử dụng hàm svd_decomposition
    U, Sigma, Vt = svd_decomposition(np.array(A))
    m, n = Sigma.shape
    Ut_b = np.dot(U.T, b)
    y = np.zeros(n)
    for i in range(min(m, n)):
        if Sigma[i, i] > 1e-10:
            y[i] = Ut_b[i] / Sigma[i, i]
    x = np.dot(Vt.T, y)
    return x.tolist()

# --- PHƯƠNG PHÁP 3: GAUSS-SEIDEL ---
def is_convergent(A):
    """Kiểm tra điều kiện chéo trội hàng"""
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        off_diag = sum(abs(A[i][j]) for j in range(n) if i != j)
        if diag <= off_diag:
            return False
    return True

def solve_gauss_seidel(A, b, max_iter=1000, tol=1e-7):
    """Thuật toán lặp Gauss-Seidel"""
    n = len(A)
    x = [0.0] * n
    
    #[Gauss-Seidel hội tụ nếu ma trận chéo trội hoặc xác định dương
    status = is_convergent(A)
    
    for k in range(max_iter):
        x_old = list(x)
        for i in range(n):
            # Dùng giá trị mới nhất của x[j] ngay khi có (j < i)
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            
            if abs(A[i][i]) > 1e-15:
                x[i] = (b[i] - s1 - s2) / A[i][i]
        
        # Điều kiện dừng
        diff = [x[i] - x_old[i] for i in range(n)]
        if vector_norm_2(diff) < tol:
            return x, k + 1, status
            
    return x, max_iter, status