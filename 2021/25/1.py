import sys
import time
from copy import deepcopy
from queue import PriorityQueue

f = open('./input', 'r')
starttime = time.time()

grid = {
    (y, x): c
    for y, line in enumerate(f.readlines())
    for x, c in enumerate(line.strip())
    if c != "."
}

w = max(x for _, x in grid)
h = max(y for y, _ in grid)
# print(grid)

def print_grid(g):
    print("\n".join(
        "".join(g.get((y,x), ".") for x in range(w+1))
        for y in range(h+1)
    ))

# print_grid(grid)
# print()
i = 0
changed = True
while changed:
    i += 1
    changed = False
    new = dict()
    for y in range(h+1):
        for x in range(w+1):
            if grid.get((y,x), '.') == '>':
                if grid.get((y, (x+1) % (w+1)), ".") == ".":
                    changed = True
                    new[(y, (x+1)%(w+1))] = ">"
                else:
                    new[(y, x)] = ">"
    for y in range(h+1):
        for x in range(w+1):
            if grid.get((y,x), '.') == "v":
                new_y = (y + 1) % (h + 1)
                if new.get((new_y, x), ".") == "." and grid.get((new_y, x), ".") in [".", ">"]:
                    changed = True
                    new[(new_y, x)] = "v"
                else:
                    new[(y, x)] = "v"
    grid = new
    # input()

print(i)




print(f"Took {time.time()-starttime}s")
f.close()
