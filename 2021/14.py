from collections import defaultdict

test = False
with open(f'data/input14{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

poly = data[0].split()[0]
instructions = [(i.split()[0], i.split()[-1]) for i in data[2:]]

def grow(n, poly):
    for i in range(n):
        new_poly = ''
        for idx, letter in enumerate(poly):
            new_poly += letter
            for tup in instructions:
                if poly[idx:idx+2] == tup[0]:
                    new_poly += tup[1]
        poly = new_poly
    return new_poly


if test:
    assert grow(4, poly) == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
else:
    grown = grow(10, poly)
    counts = defaultdict(int)
    for char in grown:
        counts[char] += 1
    print(counts)
    print(max(counts.values()) - min(counts.values()))