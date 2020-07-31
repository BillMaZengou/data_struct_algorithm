from timeit import Timer, timeit
import random

for i in range(10000, 1000001, 10000):
    t = Timer("x[random.randrange(%d)]" % i, "from __main__ import random, x")
    x = list(range(i))
    find_time = t.timeit(number=1000)
    print("%d, %10.5f" % (i, find_time))
