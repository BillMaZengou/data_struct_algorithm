from timeit import Timer, timeit
import random

for i in range(10000, 1000001, 20000):
    get_value = Timer("x.get(random.randrange(%d))" % i, "from __main__ import random, x")
    assign_value = Timer("x[random.randrange(%d)] = random.randrange(%d)" % (i, i), "from __main__ import random, x")
    x = {j:None for j in range(i)}
    get_time = get_value.timeit(number=1000)
    x = {j:None for j in range(i)}
    assign_time = assign_value.timeit(number=1000)
    print("%d, %10.5f, %10.5f" % (i, get_time, assign_time))
