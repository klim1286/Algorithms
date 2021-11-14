import timeit
import cProfile


def sieve(n):
    if n == 1:
        return 2
    size = n ** 2
    sie = [i for i in range(size)]
    sie[1] = 0

    for i in range(2, size):
        if sie[i] != 0:
            j = i + i
            while j < size:
                sie[j] = 0
                j += i
    res = [i for i in sie if i != 0]
    return res[n - 1]


print(timeit.timeit('sieve(16)', number=1000, globals=globals()))  # 0.04607000000032713
print(timeit.timeit('sieve(32)', number=1000, globals=globals()))  # 0.21215599999959522
print(timeit.timeit('sieve(64)', number=1000, globals=globals()))  # 0.9005297000003338
print(timeit.timeit('sieve(128)', number=1000, globals=globals()))  # 3.794256499999392
print(timeit.timeit('sieve(256)', number=1000, globals=globals()))  # 15.648356800000329
print(timeit.timeit('sieve(512)', number=1000, globals=globals()))  # 75.82805860000008
print(timeit.timeit('sieve(1024)', number=1000, globals=globals()))  # 345.64276560000144
cProfile.run('sieve(1000)')
#         6 function calls in 0.345 seconds
#
#  Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.006    0.006    0.345    0.345 <string>:1(<module>)
#        1    0.025    0.025    0.025    0.025 les4-task2-sieve.py:18(<listcomp>)
#        1    0.275    0.275    0.339    0.339 les4-task2-sieve.py:5(sieve)
#        1    0.039    0.039    0.039    0.039 les4-task2-sieve.py:9(<listcomp>)
#        1    0.000    0.000    0.345    0.345 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
