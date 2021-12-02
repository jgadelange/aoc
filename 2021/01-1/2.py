import sys

f = open('./input', 'r')
input = [int(val) for val in f]

prev = sys.maxsize
c = 0

values = [sum(input[i:i+3]) for i in range(len(input)-2)]
for val in values:
    if prev < val:
        c += 1
    prev = val

print(c)

f.close()
