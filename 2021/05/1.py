import sys
from collections import defaultdict

f = open('./input', 'r')
input = [
    l.split(" -> ")
    for l in f.readlines()
]

lines = []
for l in input:
    fro = l[0]
    to = l[1]

    x1, y1 = fro.split(",")
    x2, y2 = to.split(",")

    lines.append(((int(x1), int(y1)), (int(x2), int(y2))))

print(lines)

grid = defaultdict(lambda: defaultdict(lambda: 0))
max_x = 0
max_y = 0

def get_sign(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    return 0

for ((x1, y1), (x2, y2)) in lines:
    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)

    if x1 != x2 and y1 != y2:
        continue

    if x1 == x2:
        x = x1
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[x1][y] += 1
    if y1 == y2:
        y = y1
        for x in range(min(x1, x2), max(x1, x2)+1):
            grid[x][y] += 1



def print_grid(g):
    print("\n".join(
        "".join(
            str(g[x][y] or ".")
            for x in range(0, max_x+1)
        )
        for y in range(0, max_y+1)
    ))

print_grid(grid)

print(sum(
    1 if grid[x][y] >= 2 else 0
    for x in range(0, max_x+1)
    for y in range(0, max_y+1)
))



f.close()
