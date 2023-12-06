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
l = len(seeds)//2
t = sum(seeds[1::2])
print(t)

min = sys.maxsize
d = 0
for (b, a) in sorted(zip(seeds[1::2], seeds[:-1:2])):
    print(f"{d/t*100:.2f}% - {time.time()-start:.4}s")
    for seed in range(a, a+b):
        c = seed
        for ms in mappers:
            for dst_start, src_start, size in ms:
                src_end = src_start + size
                if src_start <= c < src_end:
                    c = dst_start + c - src_start
                    break
        if c < min:
            min = c
    d+=b

print(min)
print("time: ", time.time()-start)

if __name__ == "__main__":
    pass
