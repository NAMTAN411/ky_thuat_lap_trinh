import re

value = []

items = [x.strip() for x in input("Nhập mật khẩu (phân tách bằng dấu phẩy): ").split(',')]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    
    value.append(p)

print("Mật khẩu hợp lệ:", ", ".join(value))
