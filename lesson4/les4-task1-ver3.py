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
    for i in range(1, len(array)):
        if array[i] < array[min_i]:
            min_i = i
        elif array[i] > array[max_i]:
            max_i = i
    if min_i > max_i:
        min_i, max_i = max_i, min_i
    for i in range(min_i + P, max_i):
        sum_ = sum_ + array[i]
    return sum_



array = my_array(100)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.009400400000231457

array = my_array(1000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.0929348999998183

array = my_array(10000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.8292053000004671

array = my_array(100000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 8.301848099999916


cProfile.run('my_sum(array)')
#         5 function calls in 0.009 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#        1    0.009    0.009    0.009    0.009 les4-task1-ver3.py:20(my_sum)
#        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}