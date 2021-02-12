"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

from random import randint

n = [randint(0, 50) for i in range(10)]
print(f'Начальный массив: ', n)


def merge_sort(array):
    if len(array) == 1:
        return array

    center = len(array) // 2
    left = merge_sort(array[:center])
    right = merge_sort(array[center:])

    array_sort = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array_sort.append(left[i])
            i += 1
        else:
            array_sort.append(right[j])
            j += 1
    while i < len(left):
        array_sort.append(left[i])
        i += 1
    while j < len(right):
        array_sort.append(right[j])
        j += 1
    return array_sort


print(f'Отсортированный массив: ', merge_sort(n))