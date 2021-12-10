test = True
with open(f'data/input10{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

value_lookup = {')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137
                }

data = [i.split()[0] for i in data]

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
pairs = dict(zip(opening, closing))


def check_row(row):
    # find the first occurrence of a closing bracket at index i
    # from there go outward, checking if i-1, i match, i-2, i+1 match, etc, until you arrive at the next opening bracket
    # restart the process
    for idx, c in enumerate(row):
        while c in opening:
            continue
    # idx is now the index of the first closing bracket
    left = c[:idx]
    right = c[idx:2*idx]
    left = [pairs[i] for i in left][::-1]
    print(left, right)
    if left == right:
        return True
    # todo - keep checking the array. option b would be to immediately find pairs like '()' and start looking outward
    return False



for row in data:
    check_row(row)