import sys
from queue import PriorityQueue

f, w, h, s = open('./input', 'r'), 71, 71, 1024
# f, w, h, s = open('./example', 'r'), 7, 7, 12
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

ADJ_ORT = [N, E, S, W]


def in_bounds(x, y):
    return 0 <= x < w and 0 <= y < h

ps = [
    tuple(map(int, line.split(",")))
    for line in f.readlines()
    if line.strip()
]

start = (0, 0)
end = (w-1, h-1)

path = {}
dist = {}

lb, ub = s, len(ps)

while True:
    i = lb + (ub - lb) // 2
    if lb == ub:
        break

    points = ps[:i]
    dist = {
        (0, 0): 0,
    }

    q = PriorityQueue()
    q.put((0, 0, 0))

    while not q.empty():
        d, x, y = q.get()
        # print(x,y)
        # if d < dist[(x, y)]:
        #     continue
        if (x,y) == end:
            break

        for dx, dy in ADJ_ORT:
            xx, yy = x + dx, y + dy
            if not in_bounds(xx, yy) or (xx, yy) in points:
                continue
            dd = dist.get((xx, yy), sys.maxsize)
            if d+1 < dd:
                dist[(xx, yy)] = d+1
                q.put((d+1, xx, yy))
    if i == s:
        print(dist[end])
    if end not in dist:
        ub = i
    else:
        lb = i + 1

print(",".join(map(str, ps[i-1])))



if __name__ == "__main__":
    pass
