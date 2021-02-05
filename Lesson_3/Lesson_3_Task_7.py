"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Случайные значения первого массива: {array}')

if array[0] > array[1]:
    min_1 = array[1]
    min_2 = array[0]
else:
    min_1 = array[0]
    min_2 = array[1]

for i in range(2, len(array)):
    if array[i] <= min_1:
        if array[i] < min_2:
            min_2 = min_1
        min_1 = array[i]
    elif array[i] < min_2 and array[i] != min_1:
        min_2 = array[i]

print(min_1, min_2)
