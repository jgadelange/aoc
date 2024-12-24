# Strongly inspired by: https://github.com/verwoerd/AoC2024/blob/master/day24/src/main/kotlin/day24/part2/solution.kt

from collections import defaultdict
from itertools import combinations

f = open('./input', 'r')

values, ops = f.read().split('\n\n')

values = {
    k: bool(int(v))
    for k, v in
    [line.split(": ") for line in values.split('\n')]
}

operations = defaultdict(list)
os = set()
for line in ops.split('\n'):
    line = line.strip()
    if not line:
        continue
    op, to = line.split(" -> ")
    a, op, b = op.split(" ")

    os.add((a,b,op,to))


def find(a, b, op):
    try:
        return next(
            to
            for aa, bb, oopp, to in os
            if op == oopp and a in [aa, bb] and b in [aa, bb]
        )
    except StopIteration:
        return None


numZ = len([1 for op in os if op[3][0] == "z"])
wrong = set()
carry = ""
next_carry = ""
for i in range(numZ-1):
    x = f"x{i:02d}"
    y = f"y{i:02d}"
    z = f"z{i:02d}"

    s1 = find(x, y, "XOR")
    cleft = find(x, y, "AND")
    if carry:
        cright = find(carry, s1, "AND")
        if cright is None:
            wrong.update([s1, cleft])
            cleft, s1 = s1, cleft
            cright = find(carry, s1, "AND")

        sum = find(s1, carry, "XOR")

        if s1[0] == "z":
            wrong.update([s1, sum])
            sum, s1 = s1, sum

        if cleft[0] == "z":
            wrong.update([sum, cleft])
            sum, cleft = cleft, sum

        if cright[0] == "z":
            wrong.update([sum, cright])
            sum, cright = cright, sum

        next_carry = find(cright, cleft, "OR")
        if next_carry[0] == "z" and next_carry != f"z{numZ-1}":
            wrong.update([next_carry, sum])
            sum, next_carry = next_carry, sum

    carry = next_carry if carry else cleft

print(",".join(sorted(wrong)))


if __name__ == "__main__":
    pass
