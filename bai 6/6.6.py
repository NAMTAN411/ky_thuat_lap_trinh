print("Dau Nam Tan")
print("mssv:235752021610007")
class StringHandler:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        
        self.user_string = input("Nhập chuỗi: ")

    def print_String(self):
        
        print(self.user_string.upper())

handler = StringHandler()
handler.get_String() 
handler.print_String() 
