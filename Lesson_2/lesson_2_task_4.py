"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
def the_sum_of_the_series(amount_of_elements, num):
    global sum_
    if amount_of_elements > 1:
        the_sum_of_the_series(amount_of_elements - 1, num / -2)
    sum_ += num
    return sum_


amount_of_elements = int(input('Введите количество элементов (натуральное число) : '))
sum_ = 0
num = 1
x = the_sum_of_the_series(amount_of_elements, num)
print(f'Сумма ряда из {amount_of_elements} элементов = {x}')
