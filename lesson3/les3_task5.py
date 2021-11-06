import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

j = 0
for i in array:
    if i < 0:
        j += 1
        if j == 1:
            max_ = i
            max_i = array.index(i)
        elif max_ < i:
            max_ = i
            max_i = array.index(i)
if j == 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Максимальный отрицательный элемент: {max_} с индексом: {max_i}')
