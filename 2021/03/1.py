import sys

f = open('./input', 'r')
input = [list(val.strip()) for val in f.readlines()]

l = len(input[0])
s = len(input)

num_ones = [len([val[i] for val in input if val[i] == "1"]) for i in range(0, l)]
gamma_bin = "".join("1" if num > (s/2) else "0" for num in num_ones)
gamma = int(gamma_bin, 2)

print(gamma_bin, gamma)
epsilon = (gamma ^ (2 ** (l+1) - 1)) & (2 ** (l) - 1)
print(epsilon)
print(gamma * epsilon)

f.close()
