import re
from sympy import symbols, Eq, solve

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
    a, b = symbols('a b')
    sol = solve([
        Eq(ax*a + bx*b, tx),
        Eq(ay*a + by*b, ty)
    ])
    # print(sol)
    a = sol[a]
    b = sol[b]
    if int(a) == a and int(b) == b:
        ans+= a*3+b
        # print("solve")

print(ans)
if __name__ == "__main__":
    pass
