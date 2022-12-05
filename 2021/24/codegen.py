import operator
import sys
import time
from copy import deepcopy
from queue import PriorityQueue

f = open('./input', 'r')
starttime = time.time()
ops = {
    "add": "+=",
    "mul": "*=",
    "div": "//=",
    "mod": "%=",
    "eql": "",
}

lines = [
    line.strip().split()
    for line in f.readlines()
]
i = -1

indexes = {
    "x": 0,
    "y": 0,
    "z": 0,
}
print(f"x0, y0, z0 = 0,0,0")

for line in lines:
    if line[0] == "inp":
        i += 1
        # print(f"{line[1]} = inp.pop()")
        continue
    op, a, b = line
    if op == "div" and b == "1":
        continue
    if b == "w":
        b = f"inp[{i}]"
    if op == "mul" and b == "0":
        indexes[a] += 1
        print(f"{a}{indexes[a]} = 0")
        continue
    if b in ["x", "y", "z"]:
        b = f"{b}{indexes[b]}"
    if op == "eql":
        print(f"{a}{indexes[a]} = {a}{indexes[a]} == {b}")
        continue
    print(f"{a}{indexes[a]} {ops[op]} {b}")

# print(f"Took {time.time()-starttime}s")
f.close()
