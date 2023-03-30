#С точностью eps=10e-8 найти значение интеграла методом Румбе-Ромберга

import math

eps = 1e-8

def f(x):
    return 1.0 / (x + math.sin(0.9 * x))

def rumbe_romberg(f, a, b):
    n = 1
    m = 1
    R = [[0 for i in range(10)] for i in range(10)]
    R[0][0] = (b - a) * (f(a) + f(b)) / 2
    while True:
        h = (b - a) / (2**n)
        s = 0
        for i in range(1, 2**(n-1) + 1):
            s += f(a + (2 * i - 1) * h)
        R[n][0] = 0.5 * (R[n-1][0] + h * s)

        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)

        if abs(R[n][n-1] - R[n][n]) < eps:
            return R[n][n]

        n += 1

a = 3
b = 4.5

result = rumbe_romberg(f, a, b)
print(result)