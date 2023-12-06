import time

f = open('./input', 'r')

start = time.time()
print("s", start)

groups = f.read().split("\n\n")
maps = {}
maps_to = {}

seeds = [int(x) for x in groups.pop(0).split(":")[1].split()]

current = [
    x
    for a, b in zip(seeds[:-1:2], seeds[1::2])
    for x in range(a, a+b)
]
print("init", time.time()-start)

for group in groups:
    lines = group.split("\n")
    if not lines[0]:
        continue

    source, dest, _ = lines.pop(0).replace(" map", "-to-").split("-to-")
    maps_to[source] = dest

    maps[source] = {}

    new = []
    # print(len(current))

    for c in current:
        found = False
        for line in lines:
            dst_start, src_start, size = map(int, line.split())
            src_end = src_start + size
            # print(src_start <= c < src_end)
            # print(src_start, c, src_end)
            if src_start <= c < src_end:
                d = dst_start + c - src_start

                new.append(d)
                # print(d)
                found = True
                break
        if not found:
            new.append(c)

    current=new

print(min(current))
print("time: ", time.time()-start)
if __name__ == "__main__":
    pass
