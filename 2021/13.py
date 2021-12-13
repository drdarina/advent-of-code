import numpy as np

test = False
with open(f'data/input13{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

coords = [[int(j) for j in i.split()[0].split(',')] for i in data if not i.startswith('fold') and i!='\n']
folds = [i.split()[-1].split('=') for i in data if i.startswith('fold')]
folds = [(i, int(j)) for (i, j) in folds]

arr = np.zeros((max([i[0] for i in coords])+1, max([i[1] for i in coords])+1))
for pair in coords:
    arr[pair[0], pair[1]] = 1
arr = arr.T

def fold_up(arr, x):
    # split into two pars
    arr1 = arr[:x, :]
    arr2 = arr[x+1:, :]
    if arr1.shape[0] < arr2.shape[0]:
        arr1 = np.vstack([np.zeros((arr2.shape[0] - arr1.shape[0], arr1.shape[1])), arr1])
    else:
        arr2 = np.vstack([np.zeros((arr1.shape[0] - arr2.shape[0], arr1.shape[1])), arr2])
    # reverse second array for "folding"
    arr2 = arr2[::-1, :]
    return arr1 + arr2


def fold_left(arr, y):
    arr1 = arr[:, :y]
    arr2 = arr[:, y + 1:]
    if arr1.shape[1] < arr2.shape[1]:
        arr1 = np.hstack([arr1, np.zeros((arr1.shape[0], arr2.shape[1] - arr1.shape[1]))])
    else:
        arr2 = np.hstack([arr2, np.zeros((arr1.shape[0], arr1.shape[1] - arr2.shape[1]))])
    arr2 = arr2[:, ::-1]
    return arr1 + arr2


for direction, value in folds:
    if direction == 'y':
        arr = fold_up(arr, value)
    else:
        arr = fold_left(arr, value)

for a in np.array_split(arr, 8, axis=1):
    print(np.where(a>0, 1, 0))
    print()