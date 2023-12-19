f = open('./input', 'r')

grids = [[line for line in grid.split("\n") if line.strip()] for grid in f.read().split("\n\n")]

total = 0
for grid in grids:
    h = len(grid)
    w = len(grid[0])
    found = False
    for x in range(1, w):
        mirroring = True
        for y in range(h):
            mirroring &= all(
                a == b for a, b in zip(
                    reversed(grid[y][:x]),
                    grid[y][x:]
                )
            )

        if mirroring:
            found = True
            print("x", x)
            total += x
            break
    if found:
        continue
    for y in range(1, h):
        mirroring = True
        for x in range(w):
            mirroring &= all(
                a == b for a, b in zip(
                    reversed([l[x] for l in grid[:y]]),
                    [l[x] for l in grid[y:]]
                )
            )

        if mirroring:
            found = True
            print("y", y)
            total += (y)*100
            break
    if not found:
        print(":(")

print(total)
if __name__ == "__main__":
    pass
