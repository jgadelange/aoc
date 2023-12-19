f = open('./input', 'r')

grids = [[[c=="#" for c in line] for line in grid.split("\n") if line.strip()] for grid in f.read().split("\n\n")]

ms = []
total=0
for i, grid in enumerate(grids):
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
            ms.append(x)
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
            ms.append(y*100)
            break
    if not found:
        print(":(")

total = 0
for i, ggrid in enumerate(grids):
    h = len(ggrid)
    w = len(ggrid[0])
    found = False
    m = ms[i]
    for xx in range(w):
        if found: break
        for yy in range(h):
            if found:
                break
            grid = [[c for c in line] for line in ggrid]
            grid[yy][xx] = not grid[yy][xx]
            for x in range(1, w):
                if m == x:
                    continue
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
                if m == y*100:
                    continue
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


print(total)
if __name__ == "__main__":
    pass
