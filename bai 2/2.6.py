print("Dau Nam Tan")
print("mssv:235752021610007")
numbers = []

for i in range(2000, 3201):

    if i % 7 == 0 and i % 5 != 0:
        numbers.append(str(i))
        
print(",".join(numbers))
