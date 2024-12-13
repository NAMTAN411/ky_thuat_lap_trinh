print("Dau Nam Tan")
print("mssv:235752021610007")
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã gửi {amount} VND. Số dư mới: {self.balance} VND")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        elif amount > self.balance:
            print("Số dư không đủ để thực hiện giao dịch.")
        else:
            self.balance -= amount
            print(f"Đã rút {amount} VND. Số dư mới: {self.balance} VND")

    def main_menu(self):
        while True:
            print("\n--- Menu ATM ---")
            print("1. Kiểm tra số dư")
            print("2. Gửi tiền")
            print("3. Rút tiền")
            print("4. Thoát")
            choice = input("Chọn một tùy chọn (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Nhập số tiền muốn gửi: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Nhập số tiền muốn rút: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
                break
            else:
                print("Tùy chọn không hợp lệ. Vui lòng thử lại.")

atm = ATM(100000)
atm.main_menu()
