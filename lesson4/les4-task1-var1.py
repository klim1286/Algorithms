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
    min_, max_ = array[0], array[0]
    min_i, max_i, sum_ = 0, 0, 0
    P = 1
    for i in array:
        if i < min_:
            min_ = i
            min_i = array.index(i)
        elif i > max_:
            max_ = i
            max_i = array.index(i)
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
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.009932400000252528

array = my_array(1000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.040268700000524404

array = my_array(10000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 0.36993489999986195

array = my_array(100000)
print(timeit.timeit('my_sum(array)', number=1000, globals=globals()))  # 3.6496162000003096
#print(f'Сумма элементов между минимальным и максимальным: {sum_}')

cProfile.run('my_sum(array)')

#         10 function calls in 0.006 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#        1    0.005    0.005    0.005    0.005 les4-task1-var1.py:21(my_sum)
#        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}