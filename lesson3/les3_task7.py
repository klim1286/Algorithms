import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min1, min2 = array[0], array[1]
min1_i, min2_i = 0, 1
j = 0
for i in array:
    if i < min1:
        min2 = min1
        min2_i = array.index(min1)
        min1 = i
        min1_i = j
    elif i < min2 and j > min2_i:
        min2 = i
        min2_i = j
    j += 1
print(f'Первый минимум: {min1} с индексом: {min1_i}. Второй минимум: {min2} с индексом: {min2_i}')
