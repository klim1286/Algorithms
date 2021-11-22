"""
Задача 6, 3 урока
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать.
"""


import random
from sys import getsizeof


sum_memory = 0


def my_array(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    global sum_memory
    sum_memory += getsizeof(array)
    return array


def my_sum(array):
    global sum_memory
    min_i, max_i, sum_ = 0, 0, 0
    P = 1
    for i in range(1, len(array)):
        if array[i] < array[min_i]:
            min_i = i
        elif array[i] > array[max_i]:
            max_i = i
    if min_i > max_i:
        min_i, max_i = max_i, min_i
    for i in range(min_i + P, max_i):
        sum_ = sum_ + array[i]
    sum_memory += getsizeof(min_i)
    sum_memory += getsizeof(max_i)
    sum_memory += getsizeof(sum_)
    sum_memory += getsizeof(P)
    sum_memory += getsizeof(i)

    return sum_


print(my_sum(my_array(100)))
print(f'Объем памяти использованных переменных: {sum_memory}')


"""
Win10 64
Python 3.10.0  64 bit
Объем памяти использованных переменных: 1060

Наиболее оптимальным вариантом с точки зрения использовании памяти является 3. Т.к. при решении используется
меньше переменных.
"""