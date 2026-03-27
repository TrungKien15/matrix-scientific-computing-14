# Kế hoạch Thực hiện Đồ án 1: Ma Trận và Cơ Sở của Tính Toán Khoa Học

**Thời gian:** 28/03/2026 - 15/04/2026
**Nhân sự:** Nhóm 5 người:
- Nguyễn Lê Anh Tuấn - TV1 (Dev Toán 1): Focus Phần 1.
- Đỗ Bá Lâm - TV2 (Dev Toán 2): Focus thuật toán Phần 2.
- Trần Đại Hiệp  - TV3 (Manim Creator): Chuyên làm video Manim Phần 2.
- Huỳnh Thành Phát - TV4 (Data/Thực nghiệm): Focus Phần 3.
- Trần Trung Kiên - TV5 (Tech Writer/Leader): Lắp ráp, viết báo cáo LaTeX, review code.

| Thời gian | Trọng tâm | Nhiệm vụ chi tiết từng thành viên | Yêu cầu Kỹ thuật / Ghi chú |
| :--- | :--- | :--- | :--- |
| **28/03 - 31/03** | **Khởi động & Code nền tảng** | - **TV1:** Code `gaussian_eliminate` quét cả $m$ dòng, $n$ cột. Xử lý max pivot = 0 thì in `"không có pivot tại cột k"`. Code `back_substitution` phân loại 3 trường hợp: Vô nghiệm, 1 nghiệm, Vô số nghiệm.<br>- **TV2:** Phân tích thuật toán SVD ($A = U \Sigma V^T$). Code tìm trị riêng, vector riêng của $A^T A$.<br>- **TV3:** Lên storyboard Manim. Setup bối cảnh 2D, vẽ ma trận rỗng và vector chuẩn bị.<br>- **TV4:** Code phương pháp lặp Gauss-Seidel. Viết script đo thời gian bằng data giả.<br>- **TV5:** Tạo repo Git, setup cấu trúc thư mục chuẩn. Viết test cases cho ma trận $m < n$ và $m > n$. | - Code từ đầu bằng Python $\ge$ 3.10.<br>- Bắt buộc có Partial Pivoting. |
| **01/04 - 05/04** | **Tích hợp & Xử lý Logic khó** | - **TV1:** Rút trích nghiệm tổng quát khi vô số nghiệm (chuyển ma trận về RREF, tách biến cơ sở và biến tự do). Code `determinant`, `inverse`, `rank_and_basis`.<br>- **TV2:** Hoàn thiện code phân rã SVD. Bàn giao ma trận $U, \Sigma, V^T$ cho TV3.<br>- **TV3:** Code hoạt ảnh biến đổi "rotate-scale-rotate" của SVD lên hình tròn đơn vị.<br>- **TV4:** Chạy đo thời gian thực tế với các ma trận $n \in \{50, 100, 200, 500, 1000\}$.<br>- **TV5:** Tích hợp code TV1, TV2 vào `part1_demo.ipynb`. Mở file `report.tex` gõ dàn ý báo cáo. | Output vô số nghiệm phải rõ ràng: $x = x_0 + t_1 v_1 + \dots$ hoặc $x_1 = 2t, x_2 = t$. |
| **06/04 - 10/04** | **Phân tích Sâu & Video Final** | - **TV1 & TV2:** Hỗ trợ TV4 tạo ma trận Hilbert và SPD. Review chéo code.<br>- **TV3:** Thêm demo nén ảnh bằng xấp xỉ hạng thấp $A_k$. Render video final.<br>- **TV4:** Vẽ đồ thị log-log so sánh thời gian với $O(n^3)$. Phân tích tính ổn định số dựa trên số điều kiện $\kappa_2(A)$.<br>- **TV5:** Ráp nội dung vào báo cáo LaTeX. Viết file `README.md`. | Video Manim từ 2-30 phút, $\ge$ 720p. Đồ thị phải có chú thích đầy đủ. |
| **11/04 - 15/04** | **Review, Báo cáo & Đóng gói** | - **Cả nhóm:** Test chéo code trên máy cá nhân. Đọc hiểu báo cáo. Mock interview (vấn đáp thử).<br>- **TV5:** Rà soát lỗi chính tả báo cáo. Chốt file `requirements.txt`.<br>- **TV5:** Kiểm tra lại toàn bộ cấu trúc thư mục nộp bài lần cuối. Nén `.zip` và nộp lên Moodle. | Ghi rõ phân công từng người trong báo cáo. Không code thêm tính năng mới ở giai đoạn này. |