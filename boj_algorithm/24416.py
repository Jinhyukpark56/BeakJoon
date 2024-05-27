# boj dp 24416 번 피보나치 수1

num = int(input())

def fib(n) :
    f = [0] * (n+1)
    f[1], f[2] = 1,1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i -2]
    return f[n]

def fibonacci(n) :
    return n - 2
print('%d %d' % (fib(num),fibonacci(num)))