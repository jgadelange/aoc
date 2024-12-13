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
    tx += 10000000000000
    ty += 10000000000000

    # Coefficients of the equations
    # Equation 1: ax + by = c
    a, b, c = ax, bx, tx  # Replace with your values
    # Equation 2: dx + ey = f
    d, e, f = ay, by, ty  # Replace with your values

    # Create matrices for the equations
    A = np.array([[a, b], [d, e]])
    B = np.array([c, f])


    try:
        solution = np.linalg.solve(A, B)
    except:
        print("No solution")
        continue

    x, y = solution
    x, y = int(round(x)), int(round(y))
    if x*ax+y*bx == tx and x*ay+y*by == ty:
        ans+= x*3+y
        # print(f"Solution: x = {x}, y = {y}")

print(ans)
if __name__ == "__main__":
    pass
