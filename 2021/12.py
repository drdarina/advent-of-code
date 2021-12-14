test = True
with open(f'data/input12{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()


#Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more
# than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in
# lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large
# enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at
# most once, and can visit big caves any number of times.

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
g = nx.Graph()

data = [i.split()[0].split('-') for i in data]

for row in data:
    g.add_edge(*row)


print(list(nx.all_simple_paths(g, 'start', 'end')))