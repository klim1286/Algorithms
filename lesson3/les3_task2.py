import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_i = []
j = 0
for i in array:
    if i % 2 == 0:
        array_i.append(j)
    j += 1
print(array_i)
