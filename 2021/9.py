import numpy as np

test = True
with open(f'data/input9{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

data = [i.split()[0] for i in data]
data = [list(i) for i in data]
arr = np.array(data).astype(int)

mins = []
min_coords = []
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        x = arr[i, j]
        minimum = True
        for coord_pair in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            try:
                if arr[coord_pair] <= x:
                    minimum = False
                    break
            except IndexError:
                continue
        if minimum:
            mins.append(x)
            min_coords.append((i,j ))

print(len(mins) + sum(mins))
