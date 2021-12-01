import pandas as pd


def total_increasing(depths):
    return sum([i < j for i, j in zip(depths, depths[1:])])


# question 1
with open('data/input1.txt', 'r') as f:
    depths = f.readlines()
depths = [int(i) for i in depths]
print('Total increasing: {}'.format(total_increasing(depths)))


#question 2
depths = pd.Series(depths)
rolling_sum = depths.rolling(3).sum().dropna()
print('Total increasing for rolling sum: {}'.format(total_increasing(rolling_sum)))
