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


connects = set()
for a in computers:
    if not a[0] == "t":
        continue

    for b in adjacency[a]:
        for c in (adjacency[a] - {b}):
            if c in adjacency[b]:
                connects.add(tuple(sorted([a,b,c])))

print(len(connects))

cliques_by_length = defaultdict(set)
for a in computers:
    for b in adjacency[a]:
        cliques_by_length[2].add(tuple(sorted([a,b])))

i = 2
while cliques_by_length[i]:
    for clique in cliques_by_length[i]:
        a = clique[0]
        for b in adjacency[a]:
            if all(b in adjacency[c] for c in clique):
                cliques_by_length[i+1].add(tuple(sorted(clique + (b,))))

    i += 1

# print(len([c for c in cliques_by_length[3] if any(x[0] == "t" for x in c)]))
print(",".join(cliques_by_length[i-1].pop()))

if __name__ == "__main__":
    pass
