import numpy as np
#source = 'data/input3_test.txt'
source = 'data/input3.txt'
with open(source, 'r') as f:
    data = f.readlines()

data = [i.strip('\n') for i in data]

# make sure they are all the same length
assert len(set([len(i) for i in data])) == 1


def to_string(l):
    return ''.join([str(int(i)) for i in l])


# not sure how to initialize an array directly from data without losing the leading zeros
transposed = list(map(list, zip(*data)))
m = np.array(transposed).astype(int)
n = m.shape[1]
sums = m.sum(axis=1)
gamma = [i > n/2 for i in sums]
eps = [not i for i in gamma]
gamma = to_string(gamma)
eps = to_string(eps)
print(f'Gamma {gamma}, epsilon {eps}')

# convert to ints and multiply
print(f'integer gamma {int(gamma, 2)}, integer epsilon {int(eps, 2)}, result {int(gamma, 2) * int(eps, 2)}')

# question 2
# the answer is wrong and I don't have time to keep working on it
ox = m.T
co2 = m.T


def filter_vals(mat, bit, cond='ge'):
    if cond == 'ge':
        keep_val = 1 if mat.sum(axis=0)[bit] >= mat.shape[0] / 2 else 0
    else:
        keep_val = 1 if mat.sum(axis=0)[bit] < mat.shape[0] / 2 else 0
    keep = np.where(mat[:, bit] == keep_val)
    return mat[keep]

bit = 0
while ox.shape[0] > 1:
    ox = filter_vals(ox, bit, 'ge')
    bit += 1
ox = ox[0]#[:bit]

bit = 0
while co2.shape[0] > 1:
    co2 = filter_vals(co2, bit, 'le')
    bit += 1
co2 = co2[0]#[:bit]

co2 = to_string(co2)
ox = to_string(ox)
print(f'ox {ox}, co2 {co2}')

# convert to ints and multiply
print(f'integer ox {int(ox, 2)}, integer co2 {int(co2, 2)}, result {int(ox, 2) * int(co2, 2)}')