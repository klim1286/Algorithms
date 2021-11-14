import timeit
import cProfile


def simple(position):
    i = 1
    number = 2
    while i < position:
        number += 1
        for j in range(2, number - 1):
            if number % j == 0:
                break
        else:
            i += 1
    return number


print(timeit.timeit('simple(16)', number=1000, globals=globals()))  # 0.02524260000063805
print(timeit.timeit('simple(32)', number=1000, globals=globals()))  # 0.09693619999961811
print(timeit.timeit('simple(64)', number=1000, globals=globals()))  # 0.40577979999943636
print(timeit.timeit('simple(128)', number=1000, globals=globals()))  # 1.8605879999995523
print(timeit.timeit('simple(256)', number=1000, globals=globals()))  # 8.851506700000755
print(timeit.timeit('simple(512)', number=1000, globals=globals()))  # 42.715959699999075
print(timeit.timeit('simple(1024)', number=1000, globals=globals()))  # 188.56791129999874

cProfile.run('simple(1000)')
#         4 function calls in 0.182 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.182    0.182 <string>:1(<module>)
#        1    0.182    0.182    0.182    0.182 les4-task2-prime.py:5(simple)
#        1    0.000    0.000    0.182    0.182 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
