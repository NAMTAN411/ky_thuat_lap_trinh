print('sv : Dau Nam Tan')
print('mssv : 235752021610007')


def benefit(t, n, k):
    tien_nhan_duoc = n * (1 + t / 100) ** k
    return tien_nhan_duoc

try:
    t = float(input("Nhập lãi suất (t%/tháng): "))  
    n = float(input("Nhập số vốn ban đầu (n): "))  
    k = int(input("Nhập số tháng gửi (k): "))      

    tien = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {tien:.2f}")
except ValueError:
    print("Vui lòng nhập giá trị hợp lệ!")
