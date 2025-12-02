# Advent of Code 2025 - Day 02 – https://adventofcode.com/2025/day/2
from itertools import islice


def batched(iterable, n, *, strict=False):
    # batched('ABCDEFG', 2) → AB CD EF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch

f = open('./input', 'r')

total1 = 0
total2 = 0
for s in f.read().split(","):
    a, b = map(int, s.strip().split("-"))
    found = set()
    for i in range(a, b+1):
        c = str(i)

        for l in range(1, len(c)//2+1):
            chunks = list(batched(c, n=l))

            if all(chunks[0] == chunk for chunk in chunks[1:]):
                found.add(i)

        if c[:len(c)//2] == c[len(c)//2:]:
            total1+=i
    total2 += sum(found)

print(total1, total2)

if __name__ == '__main__':
    pass

