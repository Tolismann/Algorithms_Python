"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Случайные значения первого массива: {array}')

max_el = array[0]
min_el = array[0]

for i in array:
    if i > max_el:
        max_el = i
    elif i < min_el:
        min_el = i
min_index = array.index(min_el)
max_index = array.index(max_el)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Поменяли местами минимальный и максимальный элементы первого массива: {array}')
