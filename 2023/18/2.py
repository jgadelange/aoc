from collections import defaultdict

f = open('./input', 'r')
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)
U=N
D=S

mapping={
    "U": N,
    "D": S,
    "L": W,
    "R": E,
    "0": E,
    "1": S,
    "2": W,
    "3": N,
}

points = set()
current = (0, 0)
points.add(current)


minx = 0
maxx = 0
miny = 0
maxy = 0
lines_vertical = defaultdict(list)
lines_horizontal = defaultdict(list)
coordinates = [(0,0)]
edge_length = 0
for line in f.readlines():
    line = line.strip()
    if not line: continue

    x,y = current
    dd, nn, c = line.split()

    n = int(c[2:7], 16)

    d = c[7]
    dx, dy = mapping[d]

    xx, yy = x+dx*n, y+dy*n

    edge_length += max(yy, y) - min(yy, y)
    edge_length += max(xx, x) - min(xx, x)

    current = xx,yy
    coordinates.append((xx,yy))

s = sum(
    (xa*yb)-(ya*xb)
    for (xa, ya), (xb, yb) in zip(coordinates, coordinates[1:]+coordinates[:1])
)
print(s//2 + edge_length//2 + 1)
#
# print(*("".join(
#     "#" if (x, y) in points else "x" if (x,y) in filled else "."
#     for x in range(minx, maxx+1)
# ) for y in range(miny, maxy+1)), sep="\n")

if __name__ == "__main__":
    pass
