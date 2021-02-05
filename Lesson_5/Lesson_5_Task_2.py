"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

hex_num = [input('Введите первое шестнадцатеричное число: '), input('Введите второе шестнадцатеричное число: ')]
n = []
for i in range(2):
    n.append(deque())
    for j in hex_num[i]:
        n[i].appendleft(j)

max_len = max([len(n[0]), len(n[1])])
for i in range(2):
    while len(n[i]) < max_len:
        n[i].append('0')

transfer = 0
n_sum = deque()
for i in range(max_len):
    sum_r = int(n[0][i], 16) + int(n[1][i], 16)
    if sum_r + transfer >= 16:
        n_sum.append(hex(sum_r + transfer - 16).replace('0x', ''))
        transfer = 1
    else:
        n_sum.append(hex(sum_r + transfer).replace('0x', ''))
        transfer = 0
if transfer == 1:
    n_sum.append('1')

print('Сумма чисел = ', end='')
for i in range(len(n_sum)):
    print(n_sum[i], end='')
print()
