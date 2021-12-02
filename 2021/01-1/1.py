import sys

f = open('./input', 'r')
input = [int(val) for val in f]

prev = sys.maxsize
c = 0

for val in input:
    if prev < val:
       c += 1
    prev = val

print(c)
f.close()
