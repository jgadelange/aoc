from functools import reduce

f = open('./input', 'r')


class Inf:
    pass


heights = [
    [Inf] + [int(c) for c in r if c != "\n"] + [Inf]
    for r in f.readlines()
]
heights.insert(0, [Inf for _ in range(len(heights[1]))])
heights += [[Inf for _ in range(len(heights[1]))]]


def lt(a, b):
    if b is Inf:
        return True
    return a < b


low_points = [
    (i, j)
    for i in range(1, len(heights)-1)
    for j in range(1, len(heights[0])-1)
    if (
        lt(heights[i][j], heights[i-1][j]) and
        lt(heights[i][j], heights[i+1][j]) and
        lt(heights[i][j], heights[i][j-1]) and
        lt(heights[i][j], heights[i][j+1])
    )
]

basins = []

def out_bounds(y, x):
    return heights[y][x] == 9 or heights[y][x] is Inf

dydx = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)



for i, [sy, sx] in enumerate(low_points):
    basins.append({(sy, sx)})
    stack = [(sy, sx)]
    while len(stack):
        y, x = stack.pop(0)
        for dy, dx in dydx:
            y1 = y + dy
            x1 = x + dx
            if out_bounds(y1, x1) or (y1, x1) in basins[i]:
                continue
            basins[i].add((y1, x1))
            stack.append((y1, x1))

sorted_basins = list(reversed(sorted(basins, key=len)))


def mul(a, b):
    return a * b


print(reduce(mul, [len(b) for b in sorted_basins[:3]], 1))

f.close()
