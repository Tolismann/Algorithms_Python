"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

SIZE = 40
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Случайные значения первого массива: {array}')

array_2 = {}
for i in array:
    if i not in array_2:
        array_2[i] = 1
    else:
        array_2[i] += 1

maximum_repetitions = 0
max_el = 0
for _ in array_2:
    if array_2[_] > maximum_repetitions:
        max_el = _
        maximum_repetitions = array_2[_]

print(f'Число {max_el} повторяется {maximum_repetitions} раз(-а).')
