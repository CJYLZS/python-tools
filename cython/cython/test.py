import enum
import time
import add
import random


def py_add(_list):
    return [a + b for a,b in _list]

cal_list = [(random.randint(1,1000000), random.randint(1,1000000)) for _ in range(10000000)]

start_time = time.time()
res1 = add.add(cal_list)
print(time.time() - start_time)
start_time = time.time()
res2 = py_add(cal_list)
print(time.time() - start_time)

assert res1 == res2