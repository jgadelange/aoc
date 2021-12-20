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


def solution(ps):
    count = Counter()
    for (a, b), c in ps.items():
        count[a] += c
        count[b] += c
    cs = sorted(count.values())
    return (cs[len(cs)-1] // 2 - cs[0] // 2) + 1


for i in range(40):
    new_pairs = Counter()
    for (a, b), c in pairs.items():
        new_letter = mapping[(a,b)]
        new_pairs[(a, new_letter)] += c
        new_pairs[(new_letter, b)] += c
    pairs = new_pairs

    if i == 9:
        print(solution(pairs))

print(solution(pairs))
f.close()
