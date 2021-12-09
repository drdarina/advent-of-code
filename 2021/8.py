test = False

with open(f'data/input8{"_test" if test else ""}.txt', 'r') as f:
    data = f.readlines()

digits = [i.split('|')[1].split() for i in data]
digits = [i for sublist in digits for i in sublist]
lengths = [len(i) for i in digits]
total = 0
for i in [2, 3, 4, 7]:
    total += lengths.count(i)

print(total)