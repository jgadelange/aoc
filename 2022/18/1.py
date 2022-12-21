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


print(
    sum(
        6 - sum(a in cubes for a in adj(c))
        for c in cubes
    )
)

if __name__ == "__main__":
    pass
