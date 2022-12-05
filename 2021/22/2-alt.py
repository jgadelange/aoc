import json
import operator
import re
import sys
import time
from functools import reduce
from itertools import combinations
from queue import PriorityQueue

f = open('./input', 'r')
starttime = time.time()

inp = [
    (
        line[:2] == "on",
        tuple(
            map(
                int,
                [x for x in re.search(r"x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line).groups()]
            )
        )
    )
    for line in f.readlines()
  ]


def has_overlap(a, b):
    x, X, y, Y, z, Z = a
    u, U, v, V, w, W = b

    # return (
    #     x <= u <= X
    # )

    return (
            ((x <= u <= X) or (x <= U <= X) or (u <= x <= U) or (u <= X <= U)) and
            ((y <= v <= Y) or (y <= V <= Y) or (v <= y <= V) or (v <= Y <= V)) and
            ((z <= w <= Z) or (z <= W <= Z) or (w <= z <= W) or (w <= Z <= W))
    )


def get_overlap(a, b):
    if not has_overlap(a, b):
        return None
    x, X, y, Y, z, Z = a
    u, U, v, V, w, W = b
    o = (
        max(x,u),
        min(X,U),
        max(y,v),
        min(Y,V),
        max(z,w),
        min(Z,W),
    )
    return o


res = []
for on, cube in inp:
    res.extend([
        (not c, get_overlap(cube, x))
        for (c, x) in res
        if get_overlap(cube, x)
    ])
    if on:
        res.append((on, cube))

print(sum(
    (1 if c else -1) * (X-x+1) * (Y-y+1) * (Z-z+1)
    for c, (x, X, y, Y, z, Z) in res
))

print(len(res))
print(2758514936282235)


print(f"Took {time.time()-starttime}s")
f.close()
