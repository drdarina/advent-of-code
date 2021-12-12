import numpy as np

test = True
with open(f'data/input10{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

value_lookup = {')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137
                }

data = [list(i.split()[0]) for i in data]

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
pairs = dict(zip(opening, closing))
center = [i+j for i, j in zip(opening, closing)]


not_corrupted = []
unmatched_sum = 0
corrupted = False
for row in data:
    o = []
    # skip the first closing brackets
    for idx, c in enumerate(row):
        if c in opening:
            break
    row = row[idx:]
    for idx, c in enumerate(row):
        if c in opening:
            o.append(c)
        else:
            if c == pairs[o[-1]]:
                o.pop(-1)
            else:
                unmatched_sum += (value_lookup[c])
                corrupted = True
                break

    if not corrupted:
        not_corrupted.append(row)
    corrupted = False


print(unmatched_sum)

# part 2

value_lookup = zip([')', ']', '}', '>'], range(1,5))

#todo - hadn't read the puzzle correctly
scores = []
for row in not_corrupted:
    scores.append(0)
    for bracket in opening:
        n_open = row.count(bracket)
        n_closed = row.count(pairs[bracket])
        scores[-1]+=(n_open - n_closed) * value_lookup[pairs[bracket]]

print(scores)
print(int(np.median(scores)))