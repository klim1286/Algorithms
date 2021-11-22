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
    max_ = max(array)
    max_i = array.index(max(array))
    min_ = min(array)
    min_i = array.index(min(array))
    if max_i > min_i:
        x = min_i + P
        y = max_i
    else:
        x = max_i + P
        y = min_i
    for j in range(x, y):
        sum_ = sum_ + array[j]
    sum_memory += getsizeof(min_)
    sum_memory += getsizeof(max_)
    sum_memory += getsizeof(min_i)
    sum_memory += getsizeof(max_i)
    sum_memory += getsizeof(sum_)
    sum_memory += getsizeof(P)
    sum_memory += getsizeof(j)
    sum_memory += getsizeof(x)
    sum_memory += getsizeof(y)
    return sum_


print(my_sum(my_array(100)))
print(f'Объем памяти использованных переменных: {sum_memory}')

"""
Win10 64
Python 3.10.0  64 bit
Объем памяти использованных переменных: 1172
"""