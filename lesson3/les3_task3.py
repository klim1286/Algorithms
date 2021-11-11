import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_, max_ = array[0], array[0]
min_i, max_i = 0, 0
for i in array:
    if i < min_:
        min_ = i
        min_i = array.index(i)
    elif i > max_:
        max_ = i
        max_i = array.index(i)
array[min_i] = max_
array[max_i] = min_
print(array)
