"""
Ссылка на блок схемы выполненых заданий
https://drive.google.com/file/d/1PITN94N2sNiDmhKG1Yy17SGu6UQmHMzy/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
num1 = int(input("Введите целое трёхзначное число: "))
num2 = num1 % 10
num1 = num1 // 10
num3 = num1 % 10
num1 = num1 // 10
print(f"Сумма числа = {num1 + num2 + num3}")
print(f"Произведение числа = {num1 * num2 * num3}")
