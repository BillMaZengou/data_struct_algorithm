from timeit import Timer, timeit
import random

""" Check if a value in the list/dic """
# for i in range(10000, 1000001, 20000):
#     t = Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     x = {j:None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))

""" TODO: Del an element """
for i in range(10000, 100001, 20000):
    del_element = Timer("del x[0]", "from __main__ import x")
    x = list(range(i))
    lst_time = del_element.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = del_element.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))
