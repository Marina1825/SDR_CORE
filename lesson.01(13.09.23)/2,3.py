import random
array = []
for i in range(1024):
    array.append(random.uniform(-1000, 1000))
print(array)
sort = [i for i in array if i > 0]
print(sort)