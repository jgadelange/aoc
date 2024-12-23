import time
start = time.time()
from collections import defaultdict

f = open('./input', 'r')

computers = set()
adjacency = defaultdict(set)

for line in f.readlines():
    line = line.strip()
    if not line:
        continue

    a, b = line.split("-")

    computers.add(a)
    computers.add(b)
    adjacency[a].add(b)
    adjacency[b].add(a)


def bron_kerbosch(r, p, x):
    if len(p) == 0 and len(x) == 0:
        return {tuple(sorted(r))}

    result = set()

    for v in p:
        result |= bron_kerbosch(r | {v}, p & adjacency[v], x & adjacency[v])

        p -= {v}
        x |= {v}
    return result


def bron_kerbosch_pivot(r, p, x):
    if len(p) == 0 and len(x) == 0:
        return {tuple(sorted(r))}

    u = max(
        (v for v in p | x),
        key=lambda v: len(adjacency[v])
    )

    result = set()

    for v in p - adjacency[u]:
        result |= bron_kerbosch_pivot(r | {v}, p & adjacency[v], x & adjacency[v])

        p -= {v}
        x |= {v}
    return result


def bron_kerbosch_vertex_ordering(r, p, x):
    if len(p) == 0 and len(x) == 0:
        return {tuple(sorted(r))}

    result = set()

    for v in sorted(p, key=lambda v: -len(adjacency[v])):
        result |= bron_kerbosch_vertex_ordering(r | {v}, p & adjacency[v], x & adjacency[v])

        p -= {v}
        x |= {v}
    return result


# cliques = bron_kerbosch_pivot(set(), computers, set())
# default = time.time()
cliques2 = bron_kerbosch_pivot(set(), computers, set())
# pivot = time.time()
# cliques3 = bron_kerbosch_vertex_ordering(set(), computers, set())


# print(f"default        : {default-start}s")
# print(f"pivot          : {pivot-default}s")
# print(f"vertex_ordering: {end-pivot}s")

print(",".join(max(cliques2, key=len)))
end = time.time()
print("runtime:", end - start)

if __name__ == "__main__":
    pass
