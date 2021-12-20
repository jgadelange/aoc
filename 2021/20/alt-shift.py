import time

f = open('./input', 'r')

starttime = time.time()

conversion = [
    1 if v == "#" else 0
    for v in f.readline() if v != "\n"
]

assert f.readline() == "\n"

grid = {
    (y, x): 1 if c == "#" else 0
    for y, line in enumerate(f.readlines())
    for x, c in enumerate(line) if c != "\n"
}


def print_grid(g):
    w = max(x for _, x in grid) + 1
    h = max(y for y, _ in grid) + 1
    print("\n".join(
        "".join(
            "#" if g[(y,x)] else "."
            for x in range(w)
        )
        for y in range(h)
    ))


background_lookup = {
    0: conversion[0],
    1: conversion[511],
}
# print(conversion)

background = 0
w = max(x for _, x in grid) + 1
h = max(y for y, _ in grid) + 1

for i in range(50):
    grid = {
        (y, x): conversion[(
            (grid.get((y - 2, x - 2), background) << 8) +
            (grid.get((y - 2, x - 1), background) << 7) +
            (grid.get((y - 2, x), background) << 6) +
            (grid.get((y - 1, x - 2), background) << 5) +
            (grid.get((y - 1, x - 1), background) << 4) +
            (grid.get((y - 1, x), background) << 3) +
            (grid.get((y, x - 2), background) << 2) +
            (grid.get((y, x - 1), background) << 1) +
            (grid.get((y, x), background) << 0)
        )]
        for y in range(h+2)
        for x in range(w+2)
    }

    w += 2
    h += 2
    background = background_lookup[background]

    if i == 1:
        print(sum(grid.values()))

# print_grid(grid)
print(sum(grid.values()))

print(f"Took {time.time()-starttime}s")
f.close()
