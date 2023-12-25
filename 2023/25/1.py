import random
import sys
from collections import defaultdict
from copy import deepcopy
from itertools import combinations
from math import prod
from queue import Queue

f = open('./input', 'r')

adj = defaultdict(set)
edges = set()

for line in f.readlines():
    line = line.strip()
    if not line:
        continue

    current, a = line.split(": ")
    for x in a.split():
        adj[current].add(x)
        adj[x].add(current)
        edges.add(tuple(sorted([current, x])))


while True:
    graph = {
        k: list(a)
        for k, a in adj.items()
    }
    super_vertices = {
        key: {key}
        for key in adj
    }
    mincut = 0
    while len(graph) > 2:
        v1 = random.choice(list(graph.keys()))
        v2 = random.choice(list(graph[v1]))

        # print(v1,v2)
        # es.remove((v1,v2))

        graph[v1].extend(graph[v2])
        for v in graph[v2]:
            graph[v].remove(v2)
            graph[v].append(v1)

        graph[v1] = [x for x in graph[v1] if x != v1]
        del graph[v2]

        super_vertices[v1].update(super_vertices.pop(v2))
    for c, e in graph.items():
        mincut = len(e)
        if mincut == 3:
            print(c, e)

    if mincut == 3:
        break

s1, s2 = super_vertices.values()

v_to_remove = []
for k, a in adj.items():
    for kk in a:
        if k in s1 and kk in s2:
            v_to_remove.append((k, kk))


for a, b in v_to_remove:
    adj[a].remove(b)
    adj[b].remove(a)

seen = set()
stack = [a]
seen.add(a)
while stack:
    c = stack.pop()
    for a in adj[c]:
        if not a in seen:
            stack.append(a)
            seen.add(a)

print(len(seen) * (len(adj) - len(seen)))



if __name__ == "__main__":
    pass
