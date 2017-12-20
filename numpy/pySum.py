import numpy as np

def pySum1():
    a = list(range(10000))
    b = list(range(10000))
    c = []
    for i in range(len(a)):
        c.append(a[i]**2 + b[i]**2)

    return c


def npSum():
    a = np.arange(10000)
    b = np.arange(10000)
    c = a**2 + b**2
    return c

