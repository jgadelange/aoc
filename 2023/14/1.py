f = open('./input', 'r')

grid = [[c for c in line.strip()] for line in f.readlines() if line.strip()]
h = len(grid)
w = len(grid[0])

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


print(*("".join(line) for line in grid), sep="\n")

print(sum(
    i
    for i, line in enumerate(grid[::-1], start=1)
    for c in line
    if c == "O"
))




if __name__ == "__main__":
    pass
