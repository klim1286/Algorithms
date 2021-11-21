"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

i = 0
y = 0
n = int(input("Введите количество предприятий: "))
data = defaultdict(int)
loose, win = '', ''

while i != n:
    i += 1
    name = input("Введите название предприятия: ")
    quarter1 = int(input("Введите данные за 1 квартал: "))
    quarter2 = int(input("Введите данные за 2 квартал: "))
    quarter3 = int(input("Введите данные за 3 квартал: "))
    quarter4 = int(input("Введите данные за 4 квартал: "))
    data[name] = quarter1 + quarter2 + quarter3 + quarter4


for i in data:
    y = y + data[i]
    avrg = y / n

print("\nСредняя прибыль: %.0f." % avrg)
for i in data:
    if data[i] > avrg:
        win = win + i + ' '
    else:
        loose = loose + i + ' '
print(f'Названия фирм с прибылью выше среднего:\n{win}')
print(f'Названия фирм с прибылью ниже среднего:\n{loose}')
