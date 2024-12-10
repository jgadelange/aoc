import functools

f = open('./input', 'r')

grid = [
    list(map(int, line.strip()))
    for line in f.readlines()
    if line.strip()
]
h, w = len(grid), len(grid[0])

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

ADJ_ORT = [N, E, S, W]


def out_of_bounds(x, y):
    return x < 0 or x >= w or y < 0 or y >= h


starts = [
    (x, y) for y in range(h) for x in range(w)
    if grid[y][x] == 0
]


@functools.cache
def trace(x, y):
    c = grid[y][x]
    if c == 9:
        return [(x,y)]

    a = []
    for dx, dy in ADJ_ORT:
        xx, yy = x + dx, y + dy
        if out_of_bounds(xx, yy):
            continue
        if grid[yy][xx] == c+1:
            a += trace(xx, yy)
    return a


a1, a2 = 0, 0
for x, y in starts:
    a = trace(x, y)
    a1 += len(set(a))
    a2 += len(a)
    # ans += a
    # print(len(a))
# print(sum(trace(x, y) for x, y in starts))
print(a1, a2)

if __name__ == "__main__":
    pass
