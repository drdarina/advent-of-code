test = True
with open(f'data/input5{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

import numpy as np

if test:
    counts = np.zeros((10, 10))
else:
    counts = np.zeros(1000, 1000)
for row in data:
    vals = row.split()
    x0, y0 = [int(i) for i in vals[0].split(',')]
    x1, y1 = [int(i) for i in vals[2].split(',')]
    if x0 == x1:
        y0, y1 = sorted([y0, y1])
        counts[x0, y0:y1+1] += 1
    elif y0 == y1:
        x0, x1 = sorted([x0, x1])
        counts[x0:x1+1, y0] += 1

print(f'There are {np.where(counts >= 2, 1, 0).sum()} lines that overlap at least twice')

# question 2
# todo - not correct yet
for row in data:
    vals = row.split()
    x0, y0 = [int(i) for i in vals[0].split(',')]
    x1, y1 = [int(i) for i in vals[2].split(',')]
    if abs(x0 - x1) == abs(y0 - y1):
        if x0 < x1:
            if y0 < y1:
                iter = zip(range(x0, x1+1), range(y0, y1+1))
            else:
                iter = zip(range(x0, x1+1), range(y0, y1-1, -1))
        else:
            if y0 < y1:
                iter = zip(range(x1, x0+1), range(y0, y1+1))
            else:
                iter = zip(range(x1, x0+1), range(y0, y1-1, -1))
        for tup in iter:
            counts[tup] += 1

print(counts.T)

