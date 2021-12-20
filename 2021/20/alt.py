import operator
import time
from functools import reduce

f = open('./input', 'r')

starttime = time.time()

adj = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

conversion = {
    tuple(map(int, bin(i)[2:].zfill(9))): 1 if v == "#" else 0
    for i, v in enumerate(f.readline()) if v != "\n"
}
extra = 1

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
    0: conversion[tuple(0 for _ in range(9))],
    1: conversion[tuple(1 for _ in range(9))],
}

background = 0
w = max(x for _, x in grid) + 1
h = max(y for y, _ in grid) + 1

for i in range(50):
    grid = {
        (y, x): conversion[(
            grid.get((y-2, x-2), background),
            grid.get((y-2, x-1), background),
            grid.get((y-2, x), background),
            grid.get((y-1, x-2), background),
            grid.get((y-1, x-1), background),
            grid.get((y-1, x), background),
            grid.get((y, x-2), background),
            grid.get((y, x-1), background),
            grid.get((y, x), background),
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
