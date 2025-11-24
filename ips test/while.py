n = int(input("enter a value of n:"))
while n > 9:
    s = 0
    temp = n
    while temp > 0:
        s += temp % 10
        temp //= 10
    n = s

print(n)
