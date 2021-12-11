import numpy as np

test = False
small_test = False

if small_test:
    with open('data/input11_small_test.txt', 'r') as f:
        data = f.readlines()
else:
    with open(f'data/input11{"_test" if test else ""}.txt', 'r') as f:
        data = f.readlines()

data = [list(i.split()[0]) for i in data]
data = np.array(data).astype(int)


def update_at_coords(i, j, data):
    new_shiny = []
    for combination in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if combination[0] >= 0 and combination[1] >= 0:
            try:
                data[combination] +=1
                if data[combination] == 10:
                    new_shiny.append(combination)
            except IndexError:
                continue
    return data, new_shiny


total_zeros = 0
for cycle in range(100):
    data += 1
    shiny = np.where(data > 9)
    lit_up = []
    for i, j in zip(*shiny):
        data, new_shiny = update_at_coords(i, j, data)
        lit_up.extend(new_shiny)
    while len(lit_up) > 0:
        lit_up_copy = lit_up[:]
        lit_up = []
        for coords in lit_up_copy:
            data, new_shiny = update_at_coords(*coords, data)
            lit_up.extend(new_shiny)
    data[np.where(data >= 10)] = 0
    total_zeros += (data == 0).sum()
    all_flash = data.sum() == 0

print(total_zeros)

all_flash = False
step = 101
while not all_flash:
    data += 1
    shiny = np.where(data > 9)
    lit_up = []
    for i, j in zip(*shiny):
        data, new_shiny = update_at_coords(i, j, data)
        lit_up.extend(new_shiny)
    while len(lit_up) > 0:
        lit_up_copy = lit_up[:]
        lit_up = []
        for coords in lit_up_copy:
            data, new_shiny = update_at_coords(*coords, data)
            lit_up.extend(new_shiny)
    data[np.where(data >= 10)] = 0
    total_zeros += (data == 0).sum()
    all_flash = data.sum() == 0
    if all_flash:
        print('all flash at step {}'.format(step))
        break
    step += 1
