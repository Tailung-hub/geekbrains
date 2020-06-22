# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from itertools import count


def fact(x):
    for el in range(1, x):
        el = factorial(el)
        yield el

    # fact_x = factorial(x)
    # return fact_x
    # y = [el for el in range(1, x) ]


x = int(input("Введите число: "))
print(fact(x))
print(fact(x))
print(fact(x))


# def generator():
#     for el in (10, 20, 30):
#         yield el
#
# g = generator()
# print(g)





