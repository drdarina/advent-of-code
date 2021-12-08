test = False
import numpy as np
import pandas as pd


with open(f'data/input4_boards{"_test" if test else ""}.txt', 'r') as f:
    boards = f.readlines()
with open(f'data/input4_numbers{"_test" if test else ""}.txt', 'r') as f:
    numbers = f.read()

# preprocess to be a list of numpy matrices
boards = [[float(j) for j in i.split()] for i in boards]
total_boards = boards.count([]) + 1
boards = [i for i in boards if i != []]
boards_flat = np.array([i for j in boards for i in j])

numbers = [int(i) for i in numbers.split(',')]


def has_board_won(frame):
    if len(frame.dropna(axis=0, how='all')) != len(frame):
        return True
    elif len(frame.T.dropna(axis=0, how='all')) != len(frame):
        return True
    return False


def check_win_condition(l):
    arrays = [np.reshape(i, (5, 5)) for i in np.array_split(l, total_boards)]
    frames = [pd.DataFrame(i) for i in arrays]
    for frame in frames:
        if has_board_won(frame):
            return True, frame
    return False, None


# question 1
for number in numbers:
    boards_flat[np.where(boards_flat == number)] = np.nan
    cond, frame = check_win_condition(boards_flat)
    if cond:
        break

frame = frame.fillna(0).values
print(f'Result is {number*frame.sum()}')

# question 2
for number in numbers:
    boards_flat[np.where(boards_flat == number)] = np.nan
    arrays = [np.reshape(i, (5, 5)) for i in np.array_split(boards_flat, total_boards)]
    frames = [pd.DataFrame(i) for i in arrays]
    win_status = [has_board_won(i) for i in frames]
    if sum(win_status) == total_boards - 1:
        break
frame = frames[win_status.index(False)].values

for n in numbers[numbers.index(number)+1:]:
    frame[np.where(frame == n)] = np.nan
    if has_board_won(pd.DataFrame(frame)):
        break
print(f'Second result is {n * np.nansum(frame)}')