from itertools import pairwise

f = open('./input', 'r')

out = [list(map(int, line.split())) for line in f.readlines() if line]
diffs = [
    [a - b for a, b in pairwise(l)]
    for l in out
]

print(
    sum(
        (all(abs(i) <= 3 for i in l) and (
            all(i < 0 for i in l) or
            all(i > 0 for i in l)
        ))
        for l in diffs
    )

)

b = 0
for ll in out:
    l = [a - b for a, b in pairwise(ll)]
    a = int(
        (all(abs(i) <= 3 for i in l) and (
                all(i < 0 for i in l) or
                all(i > 0 for i in l)
        ))
    )
    if a == 1:
        b += 1
        continue

    for i in range(len(ll)):
        l = [a-b for a, b in pairwise(ll[0:i]+ll[i+1:])]
        a = int(
            (all(abs(i) <= 3 for i in l) and (
                    all(i < 0 for i in l) or
                    all(i > 0 for i in l)
            ))
        )
        if a == 1:
            b += 1
            break

print(b)

if __name__ == "__main__":
    pass
