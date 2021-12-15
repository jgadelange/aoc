import sys
from collections import Counter

f = open('./input', 'r')

start = list(f.readline().strip())
f.readline()

mapping = dict(
    [
        (tuple(list(line.split(" -> ")[0].strip())), line.split(" -> ")[1].strip())
        for line in f.readlines()
    ]
)
pairs = Counter([
    (start[i], start[i+1])
    for i in range(len(start)-1)
])

for _ in range(40):
    new_pairs = Counter()
    for (a, b), c in pairs.items():
        new_letter = mapping[(a,b)]
        new_pairs[(a, new_letter)] += c
        new_pairs[(new_letter, b)] += c
    pairs = new_pairs

count = Counter()
for (a, b), c in pairs.items():
    count[a] += c
    count[b] += c
cs = sorted(count.values())
# print(cs)
print((cs[len(cs)-1] // 2 - cs[0] // 2) + 1)
f.close()
