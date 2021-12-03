import sys

f = open('./input', 'r')
input = [list(val.strip()) for val in f.readlines()]

l = len(input[0])
s = len(input)

def count(vals, more_ones=1, i=0):
    if len(vals) == 1:
        return vals
    num_ones = len([val[i] for val in vals if val[i] == "1"])
    desired = str(more_ones if num_ones >= len(vals)/2.0 else 1 - more_ones)
    return count([val for val in vals if val[i] == desired], more_ones, i+1)

ox_bin = "".join(count(input)[0])
ox = int(ox_bin, 2)
co2_bin = "".join(count(input, 0)[0])
co2 = int(co2_bin , 2)

print(ox_bin)
print(co2_bin)

print(ox, co2)
print(ox*co2)

f.close()
