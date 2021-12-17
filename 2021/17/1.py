import re
import sys

f = open('./input', 'r')

x1, x2, y1, y2 = [int(x) for x in re.search(r"x=(-?\d+)\.\.(\d+), y=(-?\d+)..(-?\d+)", f.readline()).groups()]

x = 0
first = True
max_ys = []
while True:
    x += 1
    if x > x2:
        break
    dx = x
    xx = x
    i = 1
    possibles = []
    if x1 <= xx <= x2:
        possibles.append(i)
    while True:
        if dx == 0:
            break
        i += 1
        dx -= 1
        xx += dx
        # print(x, i, xx, dx, x1, x2)
        if xx < x1:
            continue
        if xx <= x2:
            possibles.append(i)
            if dx == 0:
                possibles.append(sys.maxsize)
            continue
        break
    # print(x, possibles)
    if not possibles:
        continue
    max_steps = max(possibles)
    min_steps = min(possibles)
    y = y1 - 1
    possible_ys = []
    while True:
        y += 1
        if y > -y1:
            # print(y*min_steps)
            break
        yy = 0
        dy = y
        max_y = 0
        # print(y)
        for i in range(max_steps):
            yy += dy
            dy -= 1
            max_y = max(max_y, yy)
            # print(x, y, i, yy, dy, y1, y2)
            if yy > y2:
                continue
            if yy >= y1:
                if min_steps <= (i+1) <= max_steps:
                    # print("YEAH!", y, i)
                    max_ys.append(max_y)
                    possible_ys.append(y)
                    break
                continue
            break
    if first and max_ys:
        first = False
        print(x, max(max_ys))
    # if possible_ys:
    #     print(x, possible_ys)

print(len(max_ys))

f.close()
