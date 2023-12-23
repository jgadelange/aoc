f = open('./example', 'r')

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
    ".": [N,E,S,W],
}

maxl = 0

stack = [(start,)]
while stack:
    path = stack.pop()
    current = path[-1]
    if current == end:
        maxl = max(maxl, len(path))
        continue

    x, y = current
    c = grid[y][x]
    for dx, dy in adj[c]:
        xx, yy = x+dx, y+dy
        if (xx, yy) in path:
            continue
        if grid[yy][xx] == "#":
            continue
        stack.append(path + ((xx, yy),))

print(maxl-1)

if __name__ == "__main__":
    pass
