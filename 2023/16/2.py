f = open('./example', 'r')

grid = [line.strip() for line in f.readlines() if line.strip()]
h = len(grid)
w = len(grid[0])

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)



dirs = {
    "-": {N: [W,E], S:[W,E], W: [W], E:[E]},
    "|": {N: [N], S:[S], W:[N,S], E:[N,S]},
    "\\": {N: [W], S:[E], W:[N], E: [S]},
    "/": {N: [E], S: [W], W: [S], E: [N]},
}

m = 0
starts = []
for x in range(w):
    starts.append([((x, 0), S)])
    starts.append([((x, h-1), N)])
for y in range(h):
    starts.append([((0, y), E)])
    starts.append([((w-1, y), W)])
for stack in starts:
    visited = set()
    while len(stack):
        (x, y), (dx, dy) = stack.pop()
        if (x, y, dx, dy) in visited or x >= w or y >= h or x <0 or y < 0:
            continue
        visited.add((x,y,dx,dy))

        c = grid[y][x]
        if c == ".":
            stack.append(((x+dx,y+dy), (dx, dy)))
            continue

        for ddx, ddy in dirs[c][(dx,dy)]:
            stack.append(((x+ddx, y+ddy), (ddx, ddy)))

    coordinates = {
        (x, y)
        for (x, y, _, __) in visited
    }
    m = max(m, len(coordinates))
print(m)

if __name__ == "__main__":
    pass
