f = open('./input', 'r')
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

def add_points(*points):
    return tuple(map(sum, zip(*points)))


NE = add_points(N, E)
SE = add_points(S, E)
SW = add_points(S, W)
NW = add_points(N, W)

ADJ_ORT = [N, E, S, W]
ADJ_DIAG = [NE, SE, SW, NW]
ADJ = [N, NE, E, SE, S, SW, W, NW]

rotate = {
    N: E,
    E: S,
    S: W,
    W: N,
}


grid = [
    line.strip() for line in f.readlines()
    if line.strip()
]

h = len(grid)
w = len(grid[0])


def out_of_bounds( x, y):
    return x < 0 or x >= w or y < 0 or y >= h


start = (0, 0)
for y, line in enumerate(grid):
    for x, point in enumerate(line):
        if point == "^":
            start = (x, y)
            break
    if start != (0, 0):
        break

visited = set()
visited.add(start)
dir_visited = set((start, N))
current = start
d = N
while True:
    nex = add_points(current, d)
    x, y = nex
    if (nex, d) in dir_visited or out_of_bounds(x, y):
        break
    while grid[y][x] == "#":
        d = rotate[d]
        nex = add_points(current, d)
        x, y = nex
        if out_of_bounds(x, y):
            print("HOI")
            break
    if out_of_bounds(x, y):
        break

    visited.add(nex)
    print(nex)
    dir_visited.add((nex, d))
    current = nex

print(visited)

print(
    "\n".join(
        "".join("X" if (x,y) in visited else grid[y][x] for x in range(w))
        for y in range(h)
    )
)
print(len(visited))

if __name__ == "__main__":
    pass
