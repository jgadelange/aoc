import functools
import time
from itertools import pairwise

f = open('./input', 'r')

regs, ops = f.read().split('\n\n')

regs = [
    int(l.split(":")[1])
    for l in regs.splitlines()
]

ops = list(map(int, ops.split(":")[1].split(",")))
print(regs, ops)
print(len(ops))


def s(regs, i, v):
    if i == 0:
        return (v, regs[1], regs[2])
    if i == 1:
        return (regs[0], v, regs[2])
    return (regs[0], regs[1], v)


A = 0
for target in reversed(ops):
    A *= 8
    for a in range(A, A+8):
        b = a % 8
        b = b ^ 3
        c = a // (1 << b)
        b = b ^ 4
        b = b ^ c
        if b % 8 == target:
            A = a
            break

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
