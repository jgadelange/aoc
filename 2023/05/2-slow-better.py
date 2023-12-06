import sys
import time

f = open('./input', 'r')

start = time.time()
print("s", start)

groups = f.read().split("\n\n")
seeds = [int(x) for x in groups.pop(0).split(":")[1].split()]

mappers = [
    [
        tuple(map(int, line.split()))
        for line in group.split("\n")[1:]
    ]
    for group in groups
]

def gen_seeds():
    for a, b in zip(seeds[:-1:2], seeds[1::2]):
        yield from range(a, a+b)

min = sys.maxsize
for seed in gen_seeds():
    c = seed
    for ms in mappers:
        for dst_start, src_start, size in ms:
            src_end = src_start + size
            if src_start <= c < src_end:
                c = dst_start + c - src_start
                break
    if c < min:
        min = c

print(min)
print("time: ", time.time()-start)

if __name__ == "__main__":
    pass
