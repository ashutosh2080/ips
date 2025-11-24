
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

n = int(input("enter a number :"))
print(is_perfect(n))
