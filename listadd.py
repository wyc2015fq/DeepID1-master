from timeit import timeit
import numpy as np

a = np.random.randn(10000, 3)
b = np.random.randn(20000, 3)
c = [1, 2, 3] * 10000

def func():
    return np.concatenate([a, b])

def func2():
    return np.r_[a, b]

def fix(x):
    return  1/(1+x)
def fix_list():
    d = [fix(x) for x in a]
    return d

def fix_list2():
    d = filter(fix, c)
    return d


print(timeit('fix_list()', 'from __main__ import fix_list', number=1))

print(timeit('fix_list2()', 'from __main__ import fix_list2', number=1))
