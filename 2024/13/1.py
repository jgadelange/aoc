import re
import numpy as np
f = open('./input', 'r')

r = re.compile(r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""")

machines = []
for machine in f.read().split("\n\n"):
    machines.append(tuple(map(int, r.match(machine).groups())))

ans = 0
for ax, ay, bx, by, tx, ty in machines:

    a = 0
    found = False
    while not found:
        if a*ax > tx or a*ay > ty:
            break
        b = 0
        while not found:

            x = ax*a + bx*b
            y = ay*a + by*b
            if x == tx and y == ty:
                ans += a*3 + b
                found = True
                continue
            if x > tx or y > ty:
                break
            b+=1
        a+=1

print(ans)
if __name__ == "__main__":
    pass
