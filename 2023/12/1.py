import re
from itertools import combinations, chain

f = open('./input', 'r')
split = re.compile(r"[.?]+")

count = 0
for line in f.readlines():
    confs = 0
    if not line.strip():
        continue
    line, ns = line.split()
    ns = [int(n) for n in ns.split(",")]

    # print(line, ns)
    qs = [i for i, c in enumerate(line) if c == "?"]
    # print(qs)

    for n in range(len(qs)+1):
        for ins in combinations(qs, n):
            # print(ins)
            l = [c for c in line]
            for i in ins:
                l[i] = "#"
            l = "".join(l)

            # print(l)
            springs = [len(x) for x in split.split(l) if len(x)]
            if springs == ns:
                count += 1
                confs += 1
            # print(springs)

    # print(confs)
print(count)

if __name__ == "__main__":
    pass
