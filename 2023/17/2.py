import sys
from collections import defaultdict
from queue import PriorityQueue

f = open('./input', 'r')
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

turn = {
    N: [E, W],
    S: [E, W],
    W: [N, S],
    E: [N, S],
}

grid = [[int(x) for x in line.strip()] for line in f.readlines() if line.strip()]
h, w = len(grid), len(grid[0])


queue = PriorityQueue()
visited = set()
loss = dict()


queue.put((0, (0, 0), S))
queue.put((0, (0, 0), E))

loss[(0, 0, N)] = 0
loss[(0, 0, S)] = 0
loss[(0, 0, W)] = 0
loss[(0, 0, E)] = 0

while queue.qsize():
    # print(queue.qsize())
    (l, (x, y), d) = queue.get()
    dx, dy = d

    if (x,y) == (w-1, h-1):
        print(l)
        break

    for dx, dy in turn[d]:
        ll = l
        for n in range(1, 4):
            xx, yy = x+(dx*n), y+(dy*n)
            if 0 <= xx < w and 0 <= yy < h:
                ll += grid[yy][xx]
        for n in range(4, 11):
            xx, yy = x+(dx*n), y+(dy*n)
            if 0 <= xx < w and 0 <= yy < h:
                ll += grid[yy][xx]
                dd = (dx,dy)
                key = (xx,yy,dd)
                item = (ll, (xx, yy), dd)
                if key not in loss or ll < loss[(xx,yy,dd)]:
                    loss[(xx,yy,dd)] = ll
                    loss[(xx,yy,(-dx,-dy))] = ll
                    queue.put(item)


if __name__ == "__main__":
    pass
