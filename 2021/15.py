import networkx as nx
import numpy as np

test = False
with open(f'data/input15{"_test" if test else ""}.txt', 'r') as f:
    data = [i.split()[0] for i in f.readlines()]

data = [list(i) for i in data]
arr = np.array(data).astype(int)


def get_graph(arr):
    g = nx.DiGraph()
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            g.add_node((i,j))
            for pair in [(i+1,j), (i,j+1)]:
                try:
                    g.add_edge((i,j), pair, weight=arr[pair])
                    g.add_edge(pair, (i, j), weight=arr[i,j])
                except IndexError:
                    continue
            if i-1 >= 0:
                g.add_edge((i-1,j), (i,j), weight=arr[i,j])
                g.add_edge((i, j), (i-1, j), weight=arr[i-1, j])
            if j-1 >= 0:
                g.add_edge((i,j-1), (i,j), weight=arr[i,j])
                g.add_edge((i,j), (i,j-1), weight=arr[i,j-1])
    return g


g = get_graph(arr)
start = (0, 0)
end = (arr.shape[0]-1, arr.shape[1]-1)

print(nx.dijkstra_path_length(g, source=(0, 0), target=end))

# part 2
big_arr = [arr]
for i in range(4):
    new_arr = big_arr[-1] + 1
    new_arr[new_arr > 9] = 1
    big_arr.append(new_arr)
horizontal = np.hstack(big_arr)
big_arr = [horizontal]
for i in range(4):
    new_arr = big_arr[-1] + 1
    new_arr[new_arr > 9] = 1
    big_arr.append(new_arr)
full = np.vstack(big_arr)

if test:
    with open(f'data/input15_test_res.txt', 'r') as f:
        data = [i.split()[0] for i in f.readlines()]
    data = [list(i) for i in data]
    arr = np.array(data).astype(int)
    assert (full - arr).all() == 0

g = get_graph(full)
end = (full.shape[0]-1, full.shape[1]-1)
print(nx.dijkstra_path_length(g, source=(0, 0), target=end))
