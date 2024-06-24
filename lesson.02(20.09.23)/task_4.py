import time
import random
import numpy as np
import matplotlib.pyplot as plt

numpyarray = []
xarray = []
array1 = []
pylist = []
n = 0
p = 0

for i in range(10, 5000000, 100000):
    array = np.random.sample(i)
    start = time.time()
    np.sort(array)
    end = time.time() - start
    numpyarray.append(end)
    xarray.append(i)
    n += 1
    print(n)
    print(numpyarray)
    print(xarray)
    plt.plot(xarray, numpyarray)

for y in range(10, 5000000, 100000):
    for x in range(y):
        array1.append(random.random())
    start1 = time.time()
    array1.sort()
    end1 = time.time() - start1
    pylist.append(end1)
    p += 1
    print(p)
    print(pylist)
    print(xarray)
    plt.plot(xarray, pylist)

plt.show()