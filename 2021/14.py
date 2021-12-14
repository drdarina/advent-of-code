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


# for part 2 let's do a less naive version
# each time we execute a rule for an existing pair p, that pair gets deleted and two new pairs are created as many
# times as the pair was present in the original polymer
pairs = [i+j for i, j in zip(poly, poly[1:])]
distinct_pairs = list(set(pairs))
pair_counts = defaultdict(int)
for p in distinct_pairs:
    pair_counts[p] = pairs.count(p)
for i in range(40):
    existing = [i for i, j in pair_counts.items() if j > 0]
    new_counts = defaultdict(int)
    for tup in instructions:
        if tup[0] in existing:
            n_pairs = pair_counts[tup[0]]
            new_counts[tup[0][0]+tup[1]] += n_pairs
            new_counts[tup[1] + tup[0][1]] += n_pairs
            pair_counts[tup[0]] = 0
    for k, v in new_counts.items():
        pair_counts[k] += v

total_pair_counts = defaultdict(int)
for c, count in pair_counts.items():
    total_pair_counts[c[0]] += count
    total_pair_counts[c[1]] += count

# deal with first and last letter in the polynomial
total_pair_counts[poly[0]] += 1
total_pair_counts[poly[-1]] += 1
print((max(total_pair_counts.values()) - min(total_pair_counts.values()))/2)