from timeit import timeit
from cProfile import run

"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


# ТЕСТ №1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# здесь имеем линейную асимптотику, с одним циклом
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10


# tests timeit
print(timeit('func(10)', number=1000, globals=globals()))
print(timeit('func(100)', number=1000, globals=globals()))
print(timeit('func(1000)', number=1000, globals=globals()))
print(timeit('func(10000)', number=1000, globals=globals()))
print(timeit('func(100000)', number=1000, globals=globals()))
print(timeit('func(1000000)', number=1000, globals=globals()))
print(timeit('func(10000000)', number=1000, globals=globals()))
print(timeit('func(100000000)', number=1000, globals=globals()))
print(timeit('func(1000000000)', number=1000, globals=globals()))
print(timeit('func(10000000000)', number=1000, globals=globals()))
print(timeit('func(100000000000)', number=1000, globals=globals()))
print(timeit('func(1000000000000)', number=1000, globals=globals()))


# 0.0007619000000000029
# 0.0010135000000000005
# 0.0010801000000000005
# 0.0011993999999999963
# 0.0019739000000000007
# 0.0023749999999999882
# 0.0028621000000000063
# 0.0036107999999999973
# 0.003726199999999999
# 0.003902900000000001
# 0.0033553000000000055
# 0.003666799999999998

# tests cProfile

def main(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10


print(run('main(100000000000)'))


# рузультаты не изменяются т.к. это почти линейная асимптотика
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:170(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# None

# ТЕСТ №2
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# здесь также, имеем линейную асимптотику, с одним циклом
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(num):
    result = ''
    for i in num:
        result = i + result


# tests timeit
print(timeit("func('10')", number=1000, globals=globals()))
print(timeit("func('100')", number=1000, globals=globals()))
print(timeit("func('1000')", number=1000, globals=globals()))
print(timeit("func('10000')", number=1000, globals=globals()))
print(timeit("func('100000')", number=1000, globals=globals()))
print(timeit("func('1000000')", number=1000, globals=globals()))
print(timeit("func('10000000')", number=1000, globals=globals()))
print(timeit("func('100000000')", number=1000, globals=globals()))
print(timeit("func('1000000000')", number=1000, globals=globals()))
print(timeit("func('10000000000')", number=1000, globals=globals()))
print(timeit("func('100000000000')", number=1000, globals=globals()))
print(timeit("func('1000000000000')", number=1000, globals=globals()))


# 0.0003258000000000011
# 0.0006059999999999954
# 0.0006443999999999964
# 0.000693100000000002
# 0.0008811999999999987
# 0.0009824999999999973
# 0.0010491000000000042
# 0.0017115000000000047
# 0.0012637999999999955
# 0.0013992999999999992
# 0.0015029000000000015
# 0.0017037000000000024

# tests cProfil

def main(num):
    result = ''
    for i in num:
        result = i + result


print(run("main('100000000000')"))
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:108(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# None

# ТЕСТ №3
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# этот вариант на мой взгляд имеет константнтную сложность O(1) означает,
# что вычислительная сложность алгоритма не зависит от размера входных данных
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(num):
    result = num[::-1]

# tests timeit
print(timeit("func('10')", number=1000, globals=globals()))
print(timeit("func('100')", number=1000, globals=globals()))
print(timeit("func('1000')", number=1000, globals=globals()))
print(timeit("func('10000')", number=1000, globals=globals()))
print(timeit("func('100000')", number=1000, globals=globals()))
print(timeit("func('1000000')", number=1000, globals=globals()))
print(timeit("func('10000000')", number=1000, globals=globals()))
print(timeit("func('100000000')", number=1000, globals=globals()))
print(timeit("func('1000000000')", number=1000, globals=globals()))
print(timeit("func('10000000000')", number=1000, globals=globals()))
print(timeit("func('100000000000')", number=1000, globals=globals()))
print(timeit("func('1000000000000')", number=1000, globals=globals()))
# 0.0002534999999999968
# 0.00024400000000000116
# 0.00024010000000000004
# 0.00025059999999999666
# 0.0002477999999999994
# 0.0002496000000000026
# 0.00024269999999999847
# 0.0002515000000000017
# 0.0002684999999999979
# 0.00024269999999999847
# 0.0002524999999999958
# 0.00028049999999999603

# tests cProfil

def main(num):
    result = num[::-1]

print(run("main('100000000000')"))
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:162(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# None


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Общий вывод : 3 вариант самый оптимальноый по времени среди всех проведенных проверок т.к. имеет
# наименьшее время и ассимптотику
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
