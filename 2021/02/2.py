import sys

f = open('./input', 'r')
input = [(val.split(' ')[0], int(val.split(' ')[1])) for val in f]

prev = sys.maxsize
loc = [0, 0, 0]

for direction, diff in input:
    if direction == 'up':
        loc[0] -= diff
        if loc[0] < 0:
            print("HUH?!")
    elif direction == 'down':
        loc[0] += diff
    elif direction == 'forward':
        loc[1] += diff
        loc[2] += loc[0] * diff

print(loc)
print(loc[1]*loc[2])
f.close()
