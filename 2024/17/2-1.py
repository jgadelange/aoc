import functools
import time
from itertools import pairwise

f = open('./example2', 'r')

regs, ops = f.read().split('\n\n')

regs = [
    int(l.split(":")[1])
    for l in regs.splitlines()
]

ops = list(map(int, ops.split(":")[1].split(",")))
print(regs, ops)
print(len(ops))


X = len(ops)
assert(ops[X-1] == 0)
assert(ops[X-2] == 3)
assert(ops[X-4] == 5)


def combo(r, op):
    if op <= 3:
        return op
    return r[op-4]


def run(regs):
    pointer = 0
    while pointer < len(ops):
        opcode, operand = ops[pointer], ops[pointer+1]
        if opcode == 0:
            regs[0] = regs[0] // (2**combo(regs, operand))
        elif opcode == 1:
            regs[1] = regs[1] ^ operand
        elif opcode == 2:
            regs[1] = combo(regs, operand) % 8
        elif opcode == 3:
            if regs[0] != 0:
                # Never happens 🤞
                pointer = operand
                print("Unexpected skip :(")
                break
        elif opcode == 4:
            regs[1] = regs[1] ^ regs[2]
        elif opcode == 5:
            return combo(regs, operand) % 8
            out.append(combo(regs, operand) % 8)
        elif opcode == 6:
            regs[1] = regs[0] // (2**combo(regs, operand))
        elif opcode == 7:
            regs[2] = regs[0] // (2**combo(regs, operand))
        pointer += 2

    # return regs, out

A = 0
ops = ops
for target in reversed(ops):
    A *= 8
    a = A
    while True:
        res = run([a, 0, 0])
        if res == target:
            A = a
            break
        a+=1

print(A)


# 0. (2,4) B = A % 8
# 1. (1,3) B = B ^ 3
# 2. (7,5) C = A / (2^B)
# 3. (1,4) B = B ^ 4
# 4. (4,7) B = B ^ C
# 5. (5,5) write(B)
# 6. (3,0) GOTO 0

if __name__ == "__main__":
    pass
