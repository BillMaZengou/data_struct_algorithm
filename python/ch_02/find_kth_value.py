from timeit import Timer, timeit
import random

def create_a_list(n):
    l = []
    for i in range(n):
        l[i] = random.random()
    return l

# TODO: linear algorithm
def linear_test(k, n):
    l = create_a_list(n)
    num = 1
    smallest = 1000000
    while num < k:
        for i in range(len(l)):
            if l[i] < smallest:
                smallest = l[i]





for i in range(10000, 1000001, 10000):
    t = Timer("x[random.randrange(%d)]" % i, "from __main__ import random, x")
    x = list(range(i))
    find_time = t.timeit(number=1000)
    print("%d, %10.5f" % (i, find_time))
