"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например,
пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque, defaultdict

numb_1 = deque(input('Введите первое шестнадцатеричнео число: '))
numb_2 = deque(input('Введите второе шестнадцатеричнео число: '))
sum_numbs = deque()
SYSTEM = 16
memory = 0


def num_to_nums(num):
    nums = deque()
    for i in num:
        if i == 'a' or i == 'A':
            nums.appendleft(10)
        elif i == 'b' or i == 'B':
            nums.appendleft(11)
        elif i == 'c' or i == 'C':
            nums.appendleft(12)
        elif i == 'd' or i == 'D':
            nums.appendleft(13)
        elif i == 'e' or i == 'E':
            nums.appendleft(14)
        elif i == 'f' or i == 'F':
            nums.appendleft(15)
        else:
            nums.appendleft(int(i))
    return nums


def num_to_nums16(num):
    s_16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    nums = deque()
    for i in num:
        nums.append(s_16[i])
    return nums


n1 = num_to_nums(numb_1)
n2 = num_to_nums(numb_2)
if len(n2) > len(n1):
    for _ in range(len(n2) - len(n1)):
        n1.append(0)
elif len(n1) > len(n2):
    for _ in range(len(n1) - len(n2)):
        n2.append(0)


sum_ = deque()
for i, j in zip(n1, n2):
    s = i + j + memory
    if s >= SYSTEM:
        s -= SYSTEM
        memory = 1
    else:
        memory = 0
    sum_.appendleft(s)
if memory == 1:
    sum_.appendleft(1)

print(f'{numb_1} + {numb_2} = {num_to_nums16(sum_)}')
