f = open('./input', 'r')

grid = [[c for c in line.strip()] for line in f.readlines() if line.strip()]
h = len(grid)
w = len(grid[0])

seen = {}
load = []
for i in range(1000000000):
    for _ in range(4):
        for x in range(w):
            for y in range(1, h):
                if grid[y][x] == "O":
                    yy = y
                    while yy > 0 and grid[yy-1][x] == ".":
                        yy-=1
                    grid[y][x] = "."
                    grid[yy][x] = "O"
                    # print(*("".join(line) for line in grid), sep="\n")
                    # print()
        grid = [list(reversed(x)) for x in zip(*grid)]
    strgrid = "".join("".join(line) for line in grid)
    if strgrid in seen:
        break
    seen[strgrid] = i
    load.append(sum(
        i
        for i, line in enumerate(grid[::-1], start=1)
        for c in line
        if c == "O"
    ))

startloop = seen[strgrid]
loopsize = i - startloop

# print(*("".join(line) for line in grid), sep="\n")
print(i, startloop)
print(load[startloop + (1000000000 - startloop) % loopsize - 1])

if __name__ == "__main__":
    pass
