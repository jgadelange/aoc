from collections import defaultdict
from queue import Queue

f = open('./input', 'r')

bricks = []
for line in f.readlines():
    line = line.strip()
    if not line:
        continue
    a, b = line.split("~")
    a = tuple(map(int, a.split(",")))
    b = tuple(map(int, b.split(",")))
    d = len([1 for x,y in zip(a,b) if x!=y])
    bricks.append((a,b))

end = dict()

bricks = list(sorted(bricks, key=lambda a: min(a[0][2],a[1][2])))
locs = dict()
for i, (a,b) in enumerate(bricks):
    locs[i] = set()
    x1, y1, z1 = a
    x2, y2, z2 = b

    dz = 0
    while True:
        dz -= 1
        zz1 = z1 + dz
        zz2 = z2 + dz
        if zz1 == 0 or zz2 == 0:
            break
        if any(
            (xx, yy, min(zz1, zz2)) in end
            for xx in range(min(x1,x2), max(x1,x2)+1)
            for yy in range(min(y1,y2), max(y1,y2)+1)
            for zz in range(min(z1,z2), max(z1,z2)+1)
        ):
            break
    for xx in range(min(x1,x2), max(x1,x2)+1):
        for yy in range(min(y1,y2), max(y1,y2)+1):
            for zz in range(min(z1,z2), max(z1,z2)+1):
                end[(xx, yy, zz+dz+1)] = i
                locs[i].add((xx,yy,zz+dz+1))

endd = end
c = 0
blocks_above = defaultdict(set)
blocks_below = defaultdict(set)
for j in range(len(bricks)):
    for k in range(j):
        if any((x,y,z-1) in locs[k] for (x,y,z) in locs[j]):
            blocks_below[j].add(k)
            blocks_above[k].add(j)
c2 = 0
for j in range(len(bricks)):
    above = blocks_above[j]
    if len(above) == 0:
        c+=1
        continue
    if all(
        blocks_below[k] != {j}
        for k in above
    ):
        c += 1

for j in range(len(bricks)):
    to_remove = Queue()
    to_remove.put(j)
    removed = set()
    while to_remove.qsize():
        current = to_remove.get()
        removed.add(current)
        for above in blocks_above[current]:
            if all(below in removed for below in blocks_below[above]):
                to_remove.put(above)
    # print(len(removed))
    c2+=len(removed)-1



print(c)
print(c2)

if __name__ == "__main__":
    pass
