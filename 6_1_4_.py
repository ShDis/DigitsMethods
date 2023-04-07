import math

def simpson_integration(f, a, b, n):
    """
    Вычисляет интеграл f(x) на отрезке [a, b] с использованием формулы Симпсона
    и n интервалов.

    :param f: функция, которую нужно проинтегрировать
    :param a: левый конец отрезка интегрирования
    :param b: правый конец отрезка интегрирования
    :param n: количество интервалов разбиения
    :return: значение интеграла и оценка погрешности
    """
    h = (b - a) / n  # шаг разбиения
    x = [a + i*h for i in range(n+1)]  # узлы интерполяции
    y = [f(x_i) for x_i in x]  # значения функции в узлах

    integral = h/3 * (y[0] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-1:2]) + y[-1])  # формула Симпсона
    '''
    h/3 - множитель формулы Симпсона, который остается постоянным при фиксированном числе интервалов разбиения.
    (y[0] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-1:2]) + y[-1]) - формула Симпсона для подсчета значения интеграла на интервале [a, b] при помощи линейной интерполяции на каждом из подинтервалов. Каждый подинтервал разбивается на три равных части, и в каждой точке подинтервала вычисляются значения функции. Далее вычисляется значение интеграла на этом подинтервале при помощи формулы Симпсона.
    y[0] - значение функции в левом конце интервала a.
    y[-1] - значение функции в правом конце интервала b.
    sum(y[1:-1:2]) - сумма значений функции в нечетных точках подинтервалов (кроме первой и последней). Срезы с шагом 2, чтобы получить только нечетные элементы.
    sum(y[2:-1:2]) - сумма значений функции в четных точках подинтервалов (кроме последней). Срезы с шагом 2, чтобы получить только четные элементы.
    Коэффициенты 4 и 2 в формуле отражают то, что значения функции используются в формуле с разными весами, в зависимости от того, находятся ли они в нечетной или четной точке.
    '''

    # оценка погрешности
    error = -(h**4 / 180) * f((a+b)/2) * ((b - a) / 2)**(-3)
    
    return integral, error

def f(x):
    return (1.0 / (x + math.sin(0.9 * x)))

a = 3.0 # левый предел интегрирования
b = 4.5 # правый предел интегрирования
eps = 1e-3 # требуемая точность
n = 1 # начальное число узлов

integral, error = simpson_integration(f, a, b, 2)
print("Значение интеграла:", integral)
print("Оценка погрешности:", error)