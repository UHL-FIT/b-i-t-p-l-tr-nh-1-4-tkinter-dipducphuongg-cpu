import tkinter as tk
from tkinter import messagebox
import datetime

def xu_ly_du_lieu():
    # 1. Lấy dữ liệu từ ô nhập
    mssv = o_nhap_ma_sv.get().strip() # .strip() để loại bỏ dấu cách thừa
    ho_ten = o_nhap_ho_ten.get().strip()

    # --- BƯỚC 1: KIỂM TRA TRỐNG (Ưu tiên kiểm tra trước) ---
    if mssv == "" or ho_ten == "":
        messagebox.showwarning("Thông báo", "Vui lòng không để trống thông tin!")
        nhan_ket_qua.config(text="Vui lòng không để trống thông tin!", fg="red")
        return # Dừng hàm ngay lập tức

    # --- BƯỚC 2: KIỂM TRA ĐỊNH DẠNG SỐ ---
    if not mssv.isdigit():
        messagebox.showerror("Lỗi dữ liệu", "Mã sinh viên phải là số!")
        nhan_ket_qua.config(text="Lỗi: MSSV không hợp lệ", fg="red")
        return # Dừng hàm ngay lập tức

    # --- BƯỚC 3: XỬ LÝ KHI DỮ LIỆU ĐÃ CHUẨN ---
    thoi_gian_hien_tai = datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    print(f"[{thoi_gian_hien_tai}] Dữ liệu nhận được: MSSV: {mssv} - Họ tên: {ho_ten}")

    # Hiển thị thông báo thành công lên màn hình
    nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
    
    # Xóa trắng ô nhập để chuẩn bị cho lần nhập sau
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

# --- PHẦN GIAO DIỆN (Giữ nguyên từ Lộ trình 3) ---
tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- PHẦN MỚI: NÚT BẤM VÀ KẾT QUẢ ---

# Nút bấm có tham số 'command' kết nối tới hàm xử lý
nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

# Nhãn hiển thị kết quả ngay trên giao diện
nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
