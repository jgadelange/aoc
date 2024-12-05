from collections import defaultdict
from functools import cmp_to_key
from itertools import pairwise

f = open('./input', 'r')

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

adj = [N, W, S, E]
adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), ]

rules, pages = f.read().split('\n\n')

rules = [tuple(map(int, rule.split("|"))) for rule in rules.split('\n')]
pages = [list(map(int, page.split(","))) for page in pages.split('\n') if page]

r = defaultdict(set)
for a, b in rules:
    r[a].add(b)

kaput = []
total = 0
for page in pages:
    c = True
    i = 0
    while c and i < len(page):
        c = all(p in r[page[i]] for p in page[i+1:])
        i += 1

    if not c:
        kaput.append(page)
        continue

    total += page[len(page)//2]


def compare(a, b):
    if b in r[a]:
        return -1
    if a in r[b]:
        return 1
    return 0

t2 = 0

for k in kaput:
    t2 += list(sorted(k, key=cmp_to_key(compare)))[len(k)//2]


print(total)
print(t2)
if __name__ == "__main__":
    pass
