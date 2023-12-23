import functools
from collections import defaultdict
from queue import PriorityQueue
import sys

f = open('./input', 'r')

grid = [line.strip() for line in f.readlines() if line.strip()]

h, w = len(grid), len(grid[0])

start = (grid[0].index("."), 0)
end = (grid[-1].index("."), h-1)

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

adj = {
    ">": [E],
    "<": [W],
    "v": [S],
    "^": [N],
    ".": [N,W,E,S],
}

maxl = 0

dots = set((x,y) for x in range(w) for y in range(h) if grid[y][x] != "#" )

q = PriorityQueue()
q.put((0, 0, start, dots))

# Start by creating graph with corridor removed:


stack = [
    (start, S)
]
graph = defaultdict(dict)
i = 0

while stack:
    current, d = stack.pop()

    x, y = current
    dx, dy = d
    x,y = x+dx, y+dy
    path = [(x,y)]
    possible = []
    while True:
        possible = []
        for dx, dy in adj["."]:
            if (-dx,-dy) == d:
                continue
            xx, yy = x+dx, y+dy
            if (xx,yy) not in dots:
                continue
            possible.append((dx,dy))

        if len(possible) != 1:
            break
        d = possible[0]
        x,y = x+d[0], y+d[1]
        path.append((x,y))

    stop = path[-1]
    graph[current][stop] = path
    graph[stop][current] = path
    x, y = stop
    all_paths = set()
    for p in graph[stop].values():
        all_paths.update(p)
    for dx, dy in possible:
        xx, yy = x+dx, y+dy
        if (xx,yy) in all_paths:
            continue
        stack.append((stop, (dx,dy)))
    # print(stack)
    i+=1
    # if i == 5:
    #     break

print("done reduce")
stack = [((start,), 0)]
while stack:
    path, d = stack.pop()
    current = path[-1]
    if current == end:
        maxl = max(maxl, d)
        # print(maxl)
        continue

    for next, p in graph[current].items():
        if next in path:
            continue
        stack.append((path + (next,), d+len(p)))

print(maxl)


if __name__ == "__main__":
    pass
