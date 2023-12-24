from sympy import Eq, symbols, solve
f = open('./input', 'r')

stones = []
for line in f.readlines():
    line = line.strip()
    if not line:
        continue
    coords, velocity = line.split("@")
    stones.append((
        tuple(map(int, coords.split(","))),
        tuple(map(int, velocity.split(","))),
    ))

# Doel: (x, y, z) (dx, dy, dz) vinden zodat
# x + dx * t = x_i + dx_i * t
# y + dy * t = y_i + dy_i * t
# z + dy * t = z_i + dz_i * t
# voor (x_i, y_i, z_i) (dx_i, dy_i, dz_i) in input

x, y, z, dx, dy, dz = symbols('x y z dx dy dz')
eqs = []
for i, ((x_i, y_i, z_i), (dx_i, dy_i, dz_i)) in enumerate(stones[:3]):
    t = symbols(f't{i}')
    eqs.extend([
        Eq(x + dx * t, x_i + dx_i * t),
        Eq(y + dy * t, y_i + dy_i * t),
        Eq(z + dz * t, z_i + dz_i * t),
    ])

solution = solve(eqs)[0]
# print(solution)
print(solution[x]+solution[y]+solution[z])

if __name__ == "__main__":
    pass
