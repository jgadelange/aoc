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
    tuple(map(lambda x: x == "1", bin(i)[2:].zfill(9))): v == "#"
    for i, v in enumerate(f.readline()) if v != "\n"
}
# print(conversion)
extra = 1

assert f.readline() == "\n"

image = {
    (y, x)
    for y, line in enumerate(f.readlines())
    for x, c in enumerate(line) if c != "\n"
    if c == "#"
}


def print_grid(g):
    minx, maxx = min(x for _, x in image), max(x for _, x in image)
    miny, maxy = min(y for y, _ in image), max(y for y, _ in image)
    print("\n".join(
        "".join(
            "#" if (y,x) in g else "."
            for x in range(minx, maxx+1)
        )
        for y in range(miny,maxy+1)
    ))
    print()


background_lookup = {
    False: conversion[tuple(False for _ in range(9))],
    True: conversion[tuple(True for _ in range(9))],
}

background = False
w = max(x for _, x in image) + 1
h = max(y for y, _ in image) + 1


def enhance(im, old_background):
    next_background = background_lookup[old_background]
    minx, maxx = min(x for _, x in im), max(x for _, x in im)
    miny, maxy = min(y for y, _ in im), max(y for y, _ in im)
    not_old = not old_background
    not_next = not next_background
    return {
        (y, x)
        for y in range(miny-1, maxy+2)
        for x in range(minx-1, maxx+2)
        if conversion[(
            not_old if (y - 1, x - 1) in im else old_background,
            not_old if (y - 1, x) in im else old_background,
            not_old if (y - 1, x + 1) in im else old_background,
            not_old if (y, x - 1) in im else old_background,
            not_old if (y, x) in im else old_background,
            not_old if (y, x + 1) in im else old_background,
            not_old if (y + 1, x - 1) in im else old_background,
            not_old if (y + 1, x) in im else old_background,
            not_old if (y + 1, x + 1) in im else old_background,
        )] is not_next
    }, next_background


# print_grid(dark)
for i in range(50):
    image, background = enhance(image, background)

    if i == 1:
        print(len(image))

print(len(image))

print(f"Took {time.time()-starttime}s")
f.close()
