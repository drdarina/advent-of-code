with open('data/input16_translation.txt', 'r') as f:
    data = f.readlines()

data = [i.split() for i in data]
tr = dict(zip([i[0] for i in data], [i[2] for i in data]))
print(tr)

s = 'D2FE28'

def to_bits(s):
    res = []
    for c in list(s):
        res.append('1' + tr[c])
    res[-1] = '0' + res[-1][1:]
    return res

print(to_bits(s))
# Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit.
# These groups of five bits immediately follow the packet header. For example, the hexadecimal string D2FE28 becomes:
#
# 110100101111111000101000
# VVVTTTAAAAABBBBBCCCCC