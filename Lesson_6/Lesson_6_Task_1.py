"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

# Python 3.8.5
# ОС Windows 10 (x64)

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, надо вывести 6843.

# 1 Вариант
from sys import getsizeof


def show(obj):
    print(f'{type(obj)=}\t{getsizeof(obj)=}\t{obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items:
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)


memory = 0

# num = int(input('num = '))  # зависит он введенных данных
num = 123456789
memory += getsizeof(num)
show(num)
copy_num = num  # копируем переменную -> память тоже копируется
memory += getsizeof(copy_num)
show(copy_num)
buf_num = 0
memory += getsizeof(buf_num)
show(buf_num)
while copy_num != 0:
    buf_num = buf_num * 10 + copy_num % 10
    copy_num //= 10

show(num)
show(copy_num)
show(buf_num)
sum_mem = getsizeof(num) + getsizeof(copy_num) + getsizeof(buf_num)
#
#
# print(f'Число {num} наоборот будет таким {buf_num}')
# print(f'Общее кол-во памяти программы {memory} байт')

# Результат запуска программы и измерения:
#
# Введено число: 123456789
#
# type(obj)=<class 'int'>	getsizeof(obj)=16	obj=123456789
# type(obj)=<class 'int'>	getsizeof(obj)=16	obj=123456789
# type(obj)=<class 'int'>	getsizeof(obj)=12	obj=0
# type(obj)=<class 'int'>	getsizeof(obj)=16	obj=123456789
# type(obj)=<class 'int'>	getsizeof(obj)=12	obj=0
# type(obj)=<class 'int'>	getsizeof(obj)=16	obj=987654321
# Число 123456789 наоборот будет таким 987654321
# Общее кол-во памяти программы 44 байт


# 2 Вариант
memory = 0
# num = input("Введите целое число: ")
num = '123456789'
show(num)
memory += getsizeof(num)
n_list = list(num)
show(n_list)
memory += getsizeof(n_list)
n_list.reverse()
num_2 = ''.join(n_list)
show(num_2)
memory += getsizeof(num_2)
print('"Обратное" ему число:', num_2)
print(f'Общее кол-во памяти программы {memory} байт')

# Результат запуска программы и измерения:
#
# Введено число: 123456789
#
# type(obj)=<class 'str'>	getsizeof(obj)=34	obj='123456789'
# type(obj)=<class 'list'>	getsizeof(obj)=64	obj=['1', '2', '3', '4', '5', '6', '7', '8', '9']
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='1'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='2'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='3'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='4'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='5'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='6'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='7'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='8'
# type(obj)=<class 'str'>	getsizeof(obj)=26	obj='9'
# type(obj)=<class 'str'>	getsizeof(obj)=34	obj='987654321'
# "Обратное" ему число: 987654321
# Общее кол-во памяти программы 132 байт


# 3 Вариант
memory = 0
# num = input('Введите целое число: ')
num = '123456789'
show(num)
memory += getsizeof(num)
result = num[::-1]
show(result)
memory += getsizeof(result)
print(result)
print(f'Общее кол-во памяти программы {memory} байт')


# Результат запуска программы и измерения:
#
# Введено число: 123456789
#
# type(obj)=<class 'str'>	getsizeof(obj)=34	obj='123456789'
# type(obj)=<class 'str'>	getsizeof(obj)=34	obj='987654321'
# 987654321
# Общее кол-во памяти программы 68 байт

'''вывод:  программы с наиболее эффективным использованием памяти - первая. 
Использование памяти в этих программах зависит от колличества введенных чисел.
'''