#Дана линейная краевая задача
#{ u'' + p(x)*u' + q(x)*u = f(x), x принадлежит [a,b]
#{ alfa*u'(a) + beta*u(a) = uppercaseA
#{ delta*u'(b) + gamma*u(b) = uppercaseB
#
#Решить краевую задачу, используя метод стрельбы для линейной краевой задачи

def p(x):
    return -(x ** (1/7)) + 1

def q(x):
    return -((x*x*x) ** (1/7))

def f(x):
    return x 

# Исходные данные
a = 1
b = 2
alfa = 0
beta = -6
gamma = 1
delta = 0
uppercaseA = 1
uppercaseB = 1