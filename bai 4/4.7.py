print('SV : Dau Nam Tan ')
print('Mssv : 235752021610007')
s = input('Nhập chuỗi: ')

new_s = ''.join([ch for ch in s if not ch.isdigit()])

print('Chuỗi mới:', new_s)
