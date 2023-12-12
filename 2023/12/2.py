import functools
import re
from itertools import combinations, chain, product

f = open('./input', 'r')
split = re.compile(r"[.?]+")
dots = re.compile(r"\.+")


@functools.cache
def num_possibilities(line, counts):
    if len(counts) == 0:
        if "#" in line:
            return 0
        return 1
    if len(line) == 0:
        return 0

    searching = counts[0]
    n = 0
    # print(searching, line)
    for i in range(len(line)-searching+1):
        if "#" in line[:i]:
            break

        possibility = line[i:i+searching]

        if "." in possibility:
             continue

        try:
            # print(repr(line[i+searching]))
            if line[i+searching] == "#":
                continue
        except IndexError:
            pass

        n += num_possibilities(line[i+searching+1:], counts[1:])
        # if line[i] == "#":
        #     continue
    return n


count = 0
for line in f.readlines():
    if not line.strip():
        continue
    line, ns = line.split()
    line = dots.sub(".", line)
    line = "?".join([line]*5)
    ns = tuple(int(n) for n in ns.split(",")) *5

    confs = num_possibilities(line, ns)
    print(confs)
    count += confs


print(count)

if __name__ == "__main__":
    pass
