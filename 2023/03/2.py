f = open('./input', 'r')

grid = [line.strip() for line in f.readlines() if line]

adjacency = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

visited = set()

w = len(grid[0])
s = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c != "*":
            continue
        p = 1
        l = 0
        for dy, dx in adjacency:
            yy = y+dy
            xx = x+dx
            if xx<0 or yy>=w or (yy,xx) in visited or not (adj := grid[yy][xx]).isdigit():
                continue

            minx = xx
            maxx = xx

            while minx >0 and grid[yy][minx-1].isdigit():
                minx -= 1
            while maxx+1 < w and grid[yy][maxx+1].isdigit():
                maxx += 1

            visited.update(
                (yy, xxx)
                for xxx in range(minx, maxx+1)
            )
            p*=int(grid[yy][minx:maxx+1])
            l+=1
        if l==2:
            s+=p

print(s)

if __name__ == "__main__":
    pass
