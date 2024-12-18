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

points = [
    tuple(map(int, line.split(",")))
    for line in f.readlines()
    if line.strip()
][:s]

# print(
#     "\n".join(
#         "".join("#" if (x,y) in points else "." for x in range(w))
#         for y in range(h)
#     )
# )

start = (0, 0)
end = (w-1, h-1)
dist = {
    (0, 0): 0,
}

def manh(point, point2):
    return abs(point[0] - point2[0]) + abs(point[1] - point2[1])


q = PriorityQueue()
q.put(((manh(start, end), 0, 0, 0)))

while not q.empty():
    _, d, x, y = q.get()
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
            q.put((manh((xx,yy), end), d+1, xx, yy))


print(dist[end])

if __name__ == "__main__":
    pass
