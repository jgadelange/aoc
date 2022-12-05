import operator
import sys
import time
from copy import deepcopy
from queue import PriorityQueue

f = open('./input', 'r')
starttime = time.time()
ops = {
    "inp": lambda x: x,
    "add": operator.add,
    "mul": operator.mul,
    "div": operator.floordiv,
    "mod": operator.mod,
    "eql": operator.eq,
}

lines = [
    line.strip().split()
    for line in f.readlines()
]


def execute_program(inp):
    mem = {"w": 0, "x":0, "y": 0, "z":0}

    for line in lines:
        if line[0] == "inp":
            mem[line[1]] = int(inp.pop(0))
            continue
        second = mem[line[2]] if line[2] in ["w", "x", "y", "z"] else int(line[2])
        mem[line[1]] = ops[line[0]](mem[line[1]], second)
    return mem

try:
    x = 10**14
    for i in range(1, 10**13):
        inp = list(str(x-i))
        if "0" in inp:
            continue
        if execute_program(inp)["z"] == 0:
            print(x-i)
            break
except KeyboardInterrupt:
    print(x-i)
# print(execute_program([15]))

print(f"Took {time.time()-starttime}s")
f.close()
