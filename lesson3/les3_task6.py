import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_, max_ = array[0], array[0]
min_i, max_i, sum_ = 0, 0, 0
P = 1  # Константа
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
print(f'Сумма элементов между минимальным и максимальным: {sum_}')
