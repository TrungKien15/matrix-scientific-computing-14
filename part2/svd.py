import numpy as np

def get_dominant_eigen(M, iterations=100, eps=1e-10):
    """Tìm trị riêng lớn nhất bằng Power Iteration"""
    n = M.shape[0]
    v = np.random.rand(n)
    
    v_norm = (sum(x**2 for x in v)**0.5)
    v = v / v_norm
    
    for _ in range(iterations):
        v_next = M @ v
        v_next_norm = (sum(x**2 for x in v_next)**0.5)
        
        if v_next_norm < eps:
            break
            
        v = v_next / v_next_norm

    eigenvalue = (v.T @ M @ v) / (v.T @ v)
    return eigenvalue, v


def find_all_eigen(M, num_eigen):
    """Tìm các trị riêng và vector riêng bằng Power Iteration + Deflation"""
    eigenvalues = []
    eigenvectors = []
    M_temp = M.copy().astype(float)

    for _ in range(num_eigen):
        val, vec = get_dominant_eigen(M_temp)
        eigenvalues.append(val)
        eigenvectors.append(vec)
        M_temp -= val * np.outer(vec, vec)

    return np.array(eigenvalues), np.array(eigenvectors).T


def gram_schmidt(vectors):
    """Thuật toán Gram-Schmidt trực chuẩn hóa"""
    basis = []
    for v in vectors:
        w = v.copy().astype(float)
        for b in basis:
            w -= np.dot(v, b) * b
            
        w_norm = (sum(x**2 for x in w)**0.5)
        if w_norm > 1e-10:
            basis.append(w / w_norm)

    return np.array(basis).T


def svd(A):
    """Phân rã SVD: A = U * Sigma * V^T"""
    m, n = A.shape
    ATA = A.T @ A

    lambdas, V = find_all_eigen(ATA, n)
    sigmas = [abs(l)**0.5 for l in lambdas]

    Sigma = np.zeros((m, n))
    for i in range(min(m, n)):
        Sigma[i, i] = sigmas[i]

    U = np.zeros((m, m))
    for i in range(min(m, n)):
        if sigmas[i] > 1e-10:
            U[:, i] = (A @ V[:, i]) / sigmas[i]

    if m > n:
        full_vectors = [U[:, i] for i in range(n)]
        for _ in range(m - n):
            full_vectors.append(np.random.rand(m))
        U = gram_schmidt(full_vectors)

    return U, Sigma, V.T