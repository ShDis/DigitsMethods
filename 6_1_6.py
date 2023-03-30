import math
#import scipy.integrate

def f(x):
    return 1.0 / (x + math.sin(0.9 * x))

# Создаем сплайн
#spline = scipy.interpolate.UnivariateSpline(x, f(x), s=0)
# Вычисляем интеграл
#I = spline.integral(a, b)

a = 3
b = 4.5

x1 = 3
x2 = 3.5
x3 = 4
x4 = 4.5

y1 = 1 / (x1 + math.sin(0.9 * x1))
y2 = 1 / (x2 + math.sin(0.9 * x2))
y3 = 1 / (x3 + math.sin(0.9 * x3))
y4 = 1 / (x4 + math.sin(0.9 * x4))

# Рассчитаем параметры сплайна
A0 = y1
A1 = (y2 - y1) / (x2 - x1)
A2 = ((y3 - y1) / (x3 - x1) - (y2 - y1) / (x2 - x1)) / (x3 - x2)
A3 = (y4 - y1 - (y3 - y1) * (x4 - x1) / (x3 - x1) - (y2 - y1) * (x4 - x2) / (x2 - x1)) / ((x4 - x3) * (x4 - x2) * (x4 - x1))

# Рассчитаем значение сплайна в точках 
S1 = A0 + A1 * (x2 - x1) + A2 * (x2 - x1) * (x2 - x1) + A3 * (x2 - x1) * (x2 - x1) * (x2 - x1)
S2 = A0 + A1 * (x3 - x1) + A2 * (x3 - x1) * (x3 - x1) + A3 * (x3 - x1) * (x3 - x1) * (x3 - x1)
S3 = A0 + A1 * (x4 - x1) + A2 * (x4 - x1) * (x4 - x1) + A3 * (x4 - x1) * (x4 - x1) * (x4 - x1)

# Вычислим интеграл
I = (b-a) * (A0 + (A1 + A2 * (b - a) + A3 * (b - a) * (b - a)) * (b - a) / 2) + (S1 + S2 + S3) * (b - a) / 6
print('Значение интеграла равно:', I)
