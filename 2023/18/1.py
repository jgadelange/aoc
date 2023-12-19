
f = open('./input', 'r')
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)
U=N
D=S

mapping={
    "U": N,
    "D": S,
    "L": W,
    "R": E,
}

points = set()
current = (0, 0)
points.add(current)
for line in f.readlines():
    line = line.strip()
    if not line: continue

    dd, nn, c = line.split()
    nn = int(nn)
    dx, dy = mapping[dd]

    for i in range(1, nn+1):
        current = current[0]+dx, current[1]+dy
        points.add(current)



minx = min(x for (x,y) in points)
maxx = max(x for (x,y) in points)
miny = min(y for (x,y) in points)
maxy = max(y for (x,y) in points)


c = 0
filled = set()
for y in range(miny, maxy+1):
    n_edges = 0
    for x in range(minx, maxx+1):
        edge = (x,y) in points
        prev_edge = (x-1, y) in points
        up_edge = (x, y-1) in points

        if edge and up_edge:
            n_edges+=1

        if edge:
            c+=1
        else:
            if n_edges%2 == 1:
                c+=1
                filled.add((x,y))

print(*("".join(
    "#" if (x, y) in points else "x" if (x,y) in filled else "."
    for x in range(minx, maxx+1)
) for y in range(miny, maxy+1)), sep="\n")
print(c)

if __name__ == "__main__":
    pass
