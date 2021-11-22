"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

array = [random.randint(-100, 99) for _ in range(10)]
print(array)


def bubble(data):
    n = 1
    strike = 0
    chek = 0
    while n < len(data):
        chek += 1
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
            else:
                strike += 1
        n += 1
        if strike == len(data) - 1:
            break
        strike = 0
        print(data)
    return data, chek


out = bubble(array)
print(f'Финиал: {out[0]} за {out[1]} попыток')
