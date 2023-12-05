f = open('./input', 'r')

groups = f.read().split("\n\n")
maps = {}
maps_to = {}

seeds = [int(x) for x in groups.pop(0).split(":")[1].split()]
current = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
print(current)

for group in groups:
    lines = group.split("\n")
    if not lines[0]:
        continue

    source, dest, _ = lines.pop(0).replace(" map", "-to-").split("-to-")
    maps_to[source] = dest

    maps[source] = {}

    new = []
    # print(len(current))

    for line in lines:
        dst_start, src_start, size = map(int, line.split())

        src_end = src_start + size
        diff = dst_start-src_start
        todo = []
        for lb, ub in current:
            if lb > src_end or ub < src_start:
                todo.append((lb, ub))
                continue
            mlb = max(lb, src_start)
            mub = min(ub, src_end)

            new.append((mlb+diff, mub+diff))
            if lb < mlb:
                todo.append((lb, mlb))
            if mub < ub:
                todo.append((mub, ub))
        current = todo

    current = new + current
    # print(current)

print(min(current)[0])

if __name__ == "__main__":
    pass
