"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def SumNum(n):
    if n == 0:
        return 0
    return n % 10 + SumNum(n // 10)


sum = 0
num = 0
x = -1
while x != 0:
    x = int(input("Введите число: "))
    s = SumNum(x)
    if sum < s:
        sum = s
        num = x
print(f'Число: {num}, сумма цифр: {sum}')
