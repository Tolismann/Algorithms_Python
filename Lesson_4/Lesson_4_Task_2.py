"""Алгоритм нахождения i-го по счёту простого числа
без использования Решета Эратосфена
"""

from timeit import timeit
from cProfile import run


def prime(n):
    count = 1
    current_prime = 1
    while count < n:
        current_prime += 2
        for i in range(2, current_prime // 2 + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1
    return current_prime


print(timeit('prime(10)', number=100, globals=globals()))  # 0.0006179000000000011
print(timeit('prime(50)', number=100, globals=globals()))  # 0.013748900000000001
print(timeit('prime(100)', number=100, globals=globals()))  # 0.0564749
print(timeit('prime(200)', number=100, globals=globals()))  # 0.2602916
print(timeit('prime(1000)', number=100, globals=globals()))  # 9.481785


def prime(n):
    count = 1
    current_prime = 1
    while count < n:
        current_prime += 2
        for i in range(2, current_prime // 2 + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1
    return current_prime


run('prime(100)')
run('prime(1000)')

#          4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Lesson_4_Task_2.py:28(prime)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.107 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.107    0.107 <string>:1(<module>)
#         1    0.107    0.107    0.107    0.107 Lesson_4_Task_2.py:28(prime)
#         1    0.000    0.000    0.107    0.107 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Алгоритм нахождения i-го по счёту простого числа
с использованием Решета Эратосфена
"""


def sieve(n):
    if n > 1:
        size = n ** 2 + 3
        s = [i for i in range(size)]
        s[1] = 0

        for i in range(2, n):
            if s[i] != 0:
                j = i + i
                while j < size:
                    s[j] = 0
                    j += i
        sift = [i for i in s if i != 0]
        return sift[n - 1]
    else:
        return 2


print(timeit('sieve(10)', number=100, globals=globals()))    # 0.0021971000000000004
print(timeit('sieve(50)', number=100, globals=globals()))    # 0.0482621
print(timeit('sieve(100)', number=100, globals=globals()))   # 0.2089705
print(timeit('sieve(200)', number=100, globals=globals()))   # 0.9647285999999999
print(timeit('sieve(1000)', number=100, globals=globals()))  # 35.2900354


def sieve(n):
    if n > 1:
        size = n ** 2 + 3
        s = [i for i in range(size)]
        s[1] = 0

        for i in range(2, n):
            if s[i] != 0:
                j = i + i
                while j < size:
                    s[j] = 0
                    j += i
        sift = [i for i in s if i != 0]
        return sift[n - 1]
    else:
        return 2


run('sieve(100)')
run('sieve(1000)')

#        6 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:101(<listcomp>)
#      1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:110(<listcomp>)
#      1    0.002    0.002    0.002    0.002 Lesson_4_Task_2.py:98(sieve)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       6 function calls in 0.371 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.010    0.010    0.371    0.371 <string>:1(<module>)
#      1    0.056    0.056    0.056    0.056 Lesson_4_Task_2.py:101(<listcomp>)
#      1    0.027    0.027    0.027    0.027 Lesson_4_Task_2.py:110(<listcomp>)
#      1    0.278    0.278    0.361    0.361 Lesson_4_Task_2.py:98(sieve)
#      1    0.000    0.000    0.371    0.371 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
