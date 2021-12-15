test = False
with open(f'data/input12{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

if test:
    with open(f'data/input12_result.txt', 'r') as f:
        res = f.readlines()
    res = [tuple(i.split()[0].split(',')) for i in res]

#Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more
# than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in
# lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large
# enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at
# most once, and can visit big caves any number of times.

import networkx as nx
import numpy as np
import itertools

g = nx.Graph()

data = [i.split()[0].split('-') for i in data]

for row in data:
    g.add_edge(*row)

paths = []

lowercase = [i for i in g.nodes if i.islower()]
uppercase = [i for i in g.nodes if i.isupper()]
from_start = []
to_end = []
for node in [i for i in g.nodes if i not in ['start', 'end']]:
    to_end.extend(list(nx.all_simple_paths(g.subgraph([i for i in g.nodes if i!='start']), node, 'end')))
    new = list(nx.all_simple_paths(g.subgraph([i for i in g.nodes if i!='end']), 'start', node))
    from_start.extend(new)
    for p in new:
        if p[-2].isupper():
            from_start.append(p+[p[-2]])


for l1 in from_start:
    for l2 in to_end:
        if l1[-1] == l2[0]:
            merged = tuple(l1 + l2[1:])
        elif l1[-1] in uppercase and l1[-1] == l2[1]:
            merged = tuple(l1 + l2)
        if merged not in paths:
            valid = True
            for n in lowercase:
                if merged.count(n) > 1:
                    valid = False
            if valid:
                paths.append(merged)

if test:
    for p in res:
        if p not in paths:
            print(p)
    print('---')
    for p in paths:
        if p not in res:
            print(p)

print(len(set(paths)))