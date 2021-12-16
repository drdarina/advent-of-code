import numpy as np
test = True

with open('data/input16_translation.txt', 'r') as f:
    data = f.readlines()

data = [i.split() for i in data]
tr = dict(zip([i[0] for i in data], [i[2] for i in data]))

s = 'D2FE28'

def to_bits(s):
    res = []
    for c in list(s):
        res.append(tr[c])
    res = ''.join(res)
    split = [res[:3], res[3:6]]
    res = res[6:]
    for i in np.arange(0, len(res), 5):
        split.append(res[i:i+5])
    return split


def is_number(bits):
    if int(bits[1], 2) == 4:
        return True
    return False


def parse_number(bits):
    vals = ''
    for idx, rest in enumerate(bits):
        vals += rest[1:]
        if rest[0] == '0':
            return int(vals, 2), idx + 1


def parse_operator(bits):
    length = bits[2][0]
    rest = ''.join(bits[2:])[1:]
    if length == '0':
        subp_length = int(rest[:15], 2)
        rest = rest[15:]
    else:
        subp_length = int(rest[:11], 2)
        rest = rest[11:]
    numbers = []
    new_ind = 2
    bits = []
    print(rest)
    for i in np.arange(0, len(rest), 5):
        bits.append(rest[i:i+5])
    print(bits)
    while new_ind < len(bits[new_ind:]):
        number, ind = parse_number(bits[new_ind:])
        new_ind += ind
        numbers.append(number)
    return subp_length, numbers

if test:
    s = 'D2FE28'
    bits = to_bits(s)
    assert ''.join(bits) == '110100101111111000101000'
    assert is_number(bits)
    assert parse_number(bits[2:])[0] == 2021
    s = '38006F45291200'
    bits = to_bits(s)
    assert ''.join(bits) == '00111000000000000110111101000101001010010001001000000000'
    assert not is_number(bits)
    print(parse_operator(bits))
    assert parse_operator(bits) == (27,  [10, 20])

# Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.
#
# For example, here is an operator packet (hexadecimal string 38006F45291200) with length type ID 0 that contains two sub-packets:
#
# 001 110 0 000000000011011 11010001010 0101001000100100 0000000
# VVV TTT I LLLLLLLLLLLLLLL AAAAAAAAAAA BBBBBBBBBBBBBBBB
# The three bits labeled V (001) are the packet version, 1.
# The three bits labeled T (110) are the packet type ID, 6, which means the packet is an operator.
# The bit labeled I (0) is the length type ID, which indicates that the length is a 15-bit number representing the number of bits in the sub-packets.
# The 15 bits labeled L (000000000011011) contain the length of the sub-packets in bits, 27.
# The 11 bits labeled A contain the first sub-packet, a literal value representing the number 10.
# The 16 bits labeled B contain the second sub-packet, a literal value representing the number 20.
