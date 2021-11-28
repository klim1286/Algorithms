"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

array = [random.uniform(0, 49) for _ in range(10)]
print(array)


def duble_merge(a, b):
    c = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    elif j < len(b):
        c += b[j:]
    return c


def sort_merge(a):
    if len(a) == 1:
        return a
    middle = len(a) // 2
    L = sort_merge(a[:middle])
    R = sort_merge(a[middle:])
    return duble_merge(L, R)


print(sort_merge(array))
