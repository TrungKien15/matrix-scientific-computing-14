import time
import numpy as np
from part3.solvers import solve_using_gauss, solve_using_svd, solve_gauss_seidel

def run_benchmark(sizes=[50, 100, 200, 500]):
    print(f"{'n':>5} | {'Gauss (s)':>12} | {'SVD (s)':>12} | {'G-Seidel (s)':>12}")
    print("-" * 55)
    
    for n in sizes:
        # Tạo ma trận SPD (xác định dương) để đảm bảo các phương pháp đều chạy tốt
        A_raw = np.random.rand(n, n)
        A = (np.dot(A_raw, A_raw.T) + n * np.eye(n)).tolist()
        b = np.random.rand(n).tolist()
        
        methods = [solve_using_gauss, solve_using_svd, solve_gauss_seidel]
        results_time = []
        
        for func in methods:
            exec_times = []
            for _ in range(5): # Chạy 5 lần
                start = time.perf_counter()
                func(A, b)
                exec_times.append(time.perf_counter() - start)
            results_time.append(sum(exec_times) / 5)
            
        print(f"{n:5d} | {results_time[0]:12.6f} | {results_time[1]:12.6f} | {results_time[2]:12.6f}")

if __name__ == "__main__":
    run_benchmark()