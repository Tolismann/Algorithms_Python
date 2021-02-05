# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, deque

quarters = 4
company = namedtuple('company', ['name', 'quarter', 'profit'])
all_company = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num+1):
    profit = 0
    quarter = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(quarters):
        quarter.append(int(input(f'Прибыль за {j+1} квартал: ')))
        profit += quarter[j]

    comp = company(name=name, quarter=tuple(quarter), profit=profit)

    all_company.add(comp)
    total_profit += profit

avg_ = total_profit / num

print(f'Средняя прибыль = {avg_}')

print(f'Предприятие с прибылью выше среднего: ')
for comp in all_company:
    if comp.profit > avg_:
        print(f'Компания {comp.name} заработала {comp.profit}')

print(f'Предприятие с прибылью ниже среднего: ')
for comp in all_company:
    if comp.profit < avg_:
        print(f'Компания {comp.name} заработала {comp.profit}')
