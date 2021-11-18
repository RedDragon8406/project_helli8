n = int(input())
def fibo(n):
    a=1
    b=1
    c=a
    for i in range(n):
        c = a + b
        b = c
        a = b
    return c
print(fibo(n))