with open('data/input2.txt', 'r') as f:
    data = f.readlines()

data = [i.split() for i in data]
data = [(i[0], int(i[1])) for i in data]

# question 1
h = sum([i[1] for i in data if i[0] == 'forward'])
d = sum([i[1] for i in data if i[0] == 'down']) - sum([i[1] for i in data if i[0] == 'up'])

print('The submarine moves {} horizontally and {} down, making the answer {}'.format(h, d, h*d))

# question 2
aim = 0
d = 0
h = 0
for i in data:
    if i[0] == 'forward':
        h += i[1]
        d += i[1] * aim
    elif i[0] == 'down':
        aim += i[1]
    else:
        aim -= i[1]
# h should not change
print('The submarine moves {} horizontally and {} down, making the answer {}'.format(h, d, h*d))
