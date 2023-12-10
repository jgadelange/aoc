from queue import PriorityQueue

f = open('./input', 'r')

grid = [
    line.strip() for line in f.readlines() if line.strip()
]

s = None
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "S":
            s = (x, y)
            break

h = len(grid)
w = len(grid[0])

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

if __name__ == "__main__":
    pass
