f = open('./input', 'r')

cubes = set(
    tuple(map(int, line.strip().split(",")))
    for line in f.readlines()
    if line.strip()
)

adjacency = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def adj(cube):
    for ad in adjacency:
        yield tuple(a+b for a, b in zip(cube,ad))


minx = min(xx for xx, yy, zz in cubes)
maxx = max(xx for xx, yy, zz in cubes)
miny = min(yy for xx, yy, zz in cubes)
maxy = max(yy for xx, yy, zz in cubes)
minz = min(zz for xx, yy, zz in cubes)
maxz = max(zz for xx, yy, zz in cubes)
cavity = set()

#
# def ray(cube):
#     x, y, z = cube
#     for xx in range(minx, maxx+1):
#         if x == xx:
#             continue
#         yield (xx, y, z)
#     for yy in range(miny, maxy+1):
#         if y == yy:
#             continue
#         yield (x, yy, z)
#     for zz in range(minz, maxz+1):
#         if z == zz:
#             continue
#         yield (x, y, zz)

def rayxplus(cube):
    x, y, z = cube
    for xx in range(x+1, maxx+1):
        yield (xx, y, z)
def rayxmin(cube):
    x, y, z = cube
    for xx in range(minx, x):
        yield (xx, y, z)
def rayyplus(cube):
    x, y, z = cube
    for yy in range(y+1, maxy+1):
        yield (x, yy, z)
def rayymin(cube):
    x, y, z = cube
    for yy in range(miny, y):
        yield (x, yy, z)
def rayzplus(cube):
    x, y, z = cube
    for zz in range(z+1, maxz+1):
        yield (x, y, zz)
def rayzmin(cube):
    x, y, z = cube
    for zz in range(minz, z):
        yield (x, y, zz)


for z in range(minz, maxz+1):
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y, z) in cubes:
                continue
            if all(
                any(r in cubes for r in ray((x,y,z)))
                for ray in [
                    rayxmin,
                    rayxplus,
                    rayymin,
                    rayyplus,
                    rayzmin,
                    rayzplus,
                ]
            ):
                cavity.add((x,y,z))

cavity = {
    c
    for c in cavity
    if any(a in cavity for a in adj(c)) or all(a in cubes for a in adj(c))
}
print(len(cavity), cavity)

cubes.update(cavity)

print(
    sum(
        6 - sum(a in cubes for a in adj(c))
        for c in cubes
    )
)




if __name__ == "__main__":
    pass
