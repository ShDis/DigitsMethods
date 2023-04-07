#Определите число узлов для нахождения значения интеграла с точностью = 10^-3 по формулам прямоугольников. Вычислите с данной точностью.

import math

def f(x):
    return (1.0 / (x + math.sin(0.9 * x)))

a = 3.0 # левый предел интегрирования
b = 4.5 # правый предел интегрирования
eps = 1e-3 # требуемая точность
M2 = 4.0
n = math.ceil((b - a) * math.sqrt((M2 * (b - a)) / (2.0 * eps))) # определение числа узлов
h = (b - a) / n # шаг разбиения
sum = 0.0 # сумма значений функции на отрезке [a, b]

for i in range(n):
    xi = a + i * h # вычисление i-го узла
    fxi = f(xi) # вычисление значения функции в узле xi
    sum += fxi # добавление значения функции к сумме

result = h * sum # вычисление значения интеграла
print(f"Значение интеграла с точностью {eps} = {result:.3f}")
print(f"Значение интеграла = {result}")

print(f"Число узлов: {n}")