import operator
import re
import sys
import time

f = open('./input', 'r')
starttime = time.time()

inp = [
    (
        line[:2] == "on",
        list(
            map(
                int,
                [x for x in re.search(r"x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line).groups()]
            )
        )
    )
    for line in f.readlines()
  ]

on = set()
for put_on, [x1, x2, y1, y2, z1, z2] in inp:
    op = operator.or_ if put_on else operator.sub
    x1, x2 = max(-50, x1), min(50, x2)
    y1, y2 = max(-50, y1), min(50, y2)
    z1, z2 = max(-50, z1), min(50, z2)
    on = op(on, {(x, y, z) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1)})
print(len(on))


print(f"Took {time.time()-starttime}s")
f.close()
