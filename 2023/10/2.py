from queue import PriorityQueue

f = open('./input', 'r')

# grid = [
#     "."+line.strip()+"." for line in f.readlines() if line.strip()
# ]

grid = [
    line.strip() for line in f.readlines() if line.strip()
]


w = len(grid[0])
# grid = ["."*w] + grid + ["."*w]
h = len(grid)


s = None
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "S":
            s = (x, y)
            break

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)


adjacency = {
    "S": [N, W, S, E],
    "|": [N, S],
    "-": [E, W],
    "L": [N, E],
    "J": [N, W],
    "7": [S, W],
    "F": [S, E]
}


q = PriorityQueue()
ds = {s: 0}

x, y = s
dx, dy = N
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["|", "F", "7"]:
    q.put((1, (xx, yy)))

x, y = s
dx, dy = S
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["|", "L", "J"]:
    q.put((1, (xx, yy)))

x, y = s
dx, dy = W
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["-", "L", "F"]:
    q.put((1, (xx, yy)))

x, y = s
dx, dy = E
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["-", "7", "J"]:
    q.put((1, (xx, yy)))


while q.qsize():
    d, (x, y) = q.get()
    if (x, y) in ds:
        continue
    ds[(x,y)] = d
    c = grid[y][x]

    for dx, dy in adjacency[c]:
        xx = x+dx
        yy = y+dy

        if xx < 0 or xx >=w:
            continue
        if yy < 0 or yy >=h:
            continue

        cc = grid[yy][xx]

        if cc not in adjacency:
            continue
        if (xx, yy) in ds:
            continue
        q.put((d+1, (xx, yy)))

# print(ds)
print(max(ds.values()))

a = set()

x, y = s
dx, dy = N
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["|", "F", "7"]:
    a.add(N)

x, y = s
dx, dy = S
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["|", "L", "J"]:
    a.add(S)

x, y = s
dx, dy = W
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["-", "L", "F"]:
    a.add(W)

x, y = s
dx, dy = E
xx, yy = x+dx, y+dy
if grid[yy][xx] in ["-", "7", "J"]:
    a.add(E)

adjacency = {
    "|": {N, S},
    "-": {E, W},
    "L": {N, E},
    "J": {N, W},
    "7": {S, W},
    "F": {S, E},
    ".": {N, S, W, E}
}

ps = [k for k,v in adjacency.items() if v==a][0]
adjacency["S"] = adjacency[ps]


newgrid = {}
for y in range(h):
    for x in range(w):
        xx = x*3+1
        yy = y*3+1
        if (x, y) in ds:
            c = grid[y][x]
        else:
            c = "."
        newgrid.update({
            (xx+dx, yy+dy):
                c if (dx == 0 and dy == 0)
                else "." if c == "."
                else "|" if ((dx, dy) in adjacency[c] and (dx, dy) in {N, S})
                else "-" if ((dx, dy) in adjacency[c] and (dx, dy) in {E, W})
                else "."
            for dx in range(-1, 2)
            for dy in range(-1, 2)
        })
#
# for y in range(h*3):
#     print("".join(newgrid[(x,y)] for x in range(w*3)))


q = {(0,0)}
not_enclosed = set()

while len(q):
    (x, y) = q.pop()
    if (x, y) in not_enclosed:
        continue

    not_enclosed.add((x,y))

    c = newgrid[(x, y)]

    for dx, dy in adjacency[c]:
        xx = x+dx
        yy = y+dy

        if xx < 0 or xx >=w*3:
            continue
        if yy < 0 or yy >=h*3:
            continue

        cc = newgrid[(x,y)]

        if cc not in adjacency:
            continue
        if (xx, yy) in not_enclosed:
            continue
        q.add((xx, yy))

print(len(
    [
        (x,y)
        for x in range(0, w*3, 3)
        for y in range(0, h*3, 3)
        if (x, y) not in not_enclosed and ((x // 3, y // 3) not in ds)
    ]
))

if __name__ == "__main__":
    pass
