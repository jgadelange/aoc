from collections import defaultdict
from functools import cmp_to_key
from itertools import pairwise

f = open('./input', 'r')

rules, pages = f.read().split('\n\n')
rules = [tuple(map(int, rule.split("|"))) for rule in rules.split('\n')]
pages = [list(map(int, page.split(","))) for page in pages.split('\n') if page]

r = defaultdict(set)
for a, b in rules:
    r[a].add(b)

def compare(a, b):
    if b in r[a]:
        return -1
    if a in r[b]:
        return 1
    return 0

t1, t2 = 0, 0
for page in pages:
    s = sorted(page, key=cmp_to_key(compare))
    if s == page:
        t1 += page[len(page)//2]
    else:
        t2 += s[len(page)//2]


print(t1)
print(t2)
if __name__ == "__main__":
    pass
