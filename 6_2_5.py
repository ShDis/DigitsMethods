#Дана задача Коши
#{ y' = f(x,y)
#{ y(a) = y0
#где функция f(x,y), отрезок [a,b], начальное значение y0
#
#n = 9
#
#Решите задачу Коши методом Адамса

# Определение функции f(x, y)
def f(x,y):
    return -(1+x*y)/(x*x)

def adams_bashforth_2nd_order(f, a, b, y0, h):
    """
    Метод Адамса-Башфорта второго порядка для решения задачи Коши.

    Параметры:
    f: callable
        Функция правой части дифференциального уравнения y' = f(x, y).
    a: float
        Начальное значение x.
    b: float
        Конечное значение x.
    y0: float
        Начальное значение y.
    h: float
        Шаг.

    Возвращает:
    x: array
        Массив значений x.
    y: array
        Массив значений y.
    """

    # Вычисляем количество шагов
    n = int((b - a) / h)

    # Инициализируем массивы x и y
    x = [a]
    y = [y0]

    # Вычисляем второе значение y используя метод Эйлера
    x.append(a + h)
    y.append(y0 + h * f(a, y0))

    # Проходимся циклом по оставшимся шагам
    for i in range(2, n + 1):
        xi = x[i]
        yi_prev = y[i]
        # Вычисляем новое значение y используя формулу Адамса-Башфорта
        yi = yi_prev + h * ((3 / 2) * f(xi, yi_prev) - (1 / 2) * f(x[i - 1], y[i - 1]))
        x.append(xi + h)
        y.append(yi)

    return x, y

# Исходные данные
a = 1
b = 2
y0 = 1
h = 0.1  # Шаг

# Вызов метода Адамса-Башфорта второго порядка
x, y = adams_bashforth_2nd_order(f, a, b, y0, h)

# Вывод результатов
print("x\t\ty(x)")
for i in range(len(y)):
    print("{:.1f}\t\t{:.6f}".format(x[i], y[i]))