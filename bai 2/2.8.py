print("Dau Nam Tan")
print("mssv:235752021610007")
a, b = 1, 2
total = 0

print(a, end=', ')

while a <= 4000000:
    
    if a % 2 == 0:
        total += a 
    
    a, b = b, a + b  
    if a <= 4000000: 
        print(a, end=', ')

print("\nTổng các số chẵn trong dãy Fibonacci: ", total)
