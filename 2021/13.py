import numpy as np

test = True
with open(f'data/input13{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

coords = [[int(j) for j in i.split()[0].split(',')] for i in data if not i.startswith('fold') and i!='\n']
folds = [i.split()[-1] for i in data if i.startswith('fold')]

arr = np.zeros((max([i[0] for i in coords])+1, max([i[1] for i in coords])+1))
for pair in coords:
    arr[pair[0], pair[1]] = 1
arr = arr.T
print(arr)

def fold_up(arr, x):
    # split into two pars
    arr1 = arr[:x, :]
    arr2 = arr[x+1:, :]
    # reverse second array for "folding"
    arr2 = arr2[::-1,:]
    # todo: sum arr1 + arr2, padding zeroes in the smaller array




def fold_left(arr, y):
    arr1 = arr[:, :y]
    arr2 = arr[:, y + 1:]


fold_up(arr, 7)