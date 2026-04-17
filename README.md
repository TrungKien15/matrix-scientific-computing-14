# Matrix Scientific Computing Project

## 1. Giới thiệu

Đây là đồ án môn *Scientific Computing*, tập trung cài đặt các thuật toán đại số tuyến tính cơ bản bằng Python.

Mục tiêu chính:
- Hiểu bản chất thuật toán (không phụ thuộc thư viện có sẵn)
- Tự cài đặt các phương pháp giải hệ phương trình
- So sánh hiệu năng giữa các phương pháp

---

## 2. Nội dung thực hiện

### Part 1 – Linear Algebra cơ bản
- Gaussian Elimination (có pivot)
- Determinant
- Inverse matrix
- Rank và Basis

### Part 2 – SVD
- Cài đặt SVD bằng:
  - Power Iteration
  - Deflation
- Không dùng `numpy.linalg.svd`

### Part 3 – Solver & Benchmark
- Giải hệ bằng:
  - Gaussian
  - SVD
  - Gauss-Seidel

---

## 3. Cấu trúc thư mục

part1/        # Thuật toán cơ bản  
part2/        # SVD + visualization
part3/        # Solver + Benchmark  
tests/        # Test bằng pytest  
report       
README.md  
requirements.txt  

---

## 4. Cài đặt

Cài thư viện cần thiết:

pip install -r requirements.txt

---

## 5. Cách chạy

Chạy test:

python -m pytest

Chạy benchmark:

python -m part3.benchmark

---
## 6. Demo

Video minh họa SVD: `demo/SVD.mp4`

Được tạo bằng Manim

