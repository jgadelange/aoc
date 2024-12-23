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

if __name__ == "__main__":
    pass
