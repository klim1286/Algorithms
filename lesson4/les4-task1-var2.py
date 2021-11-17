"""
Задача 6, 3 урока
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать.
"""


import random
import timeit
import cProfile


def my_array(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    return array
    # print(array)


def my_sum(array):
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
    return sum_


array = my_array(100)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.008091000000604254

array = my_array(1000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.03606279999985418

array = my_array(10000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.3097280000001774

array = my_array(100000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 3.073042500000156


cProfile.run('my_sum(array)')
#         10 function calls in 0.003 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#        1    0.000    0.000    0.003    0.003 les4-task1-var2.py:21(my_sum)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        2    0.002    0.001    0.002    0.001 {built-in method builtins.max}
#        2    0.001    0.001    0.001    0.001 {built-in method builtins.min}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
