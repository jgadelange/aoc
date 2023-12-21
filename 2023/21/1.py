f = open('./input', 'r')

grid = [line.strip() for line in f.readlines() if line.strip()]
h, w = len(grid), len(grid[0])

start = None
for y in range(h):
    for x in range(w):
        if grid[y][x] == "S":
            start = (x,y)

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)
adj = [N,W,E,S]

current = {start}

for i in range(64):
    next = set()
    for x,y in current:
        for dx,dy in adj:
            xx, yy = x+dx, y+dy
            if xx < 0 or xx >=w or yy <0 or yy>=h:
                continue
            if grid[yy][xx] != "#":
                next.add((xx,yy))
    current = next

print(len(current))

if __name__ == "__main__":
    pass
