import functools

f = open('./input', 'r')

a, b = f.read().split('\n\n')

available = a.split(", ")
lens = set(len(a) for a in available)

ans = 0
ans2 = 0


@functools.cache
def pat(rest):
    if rest in available:
        return 1 + sum(
            pat(rest[l:])
            for l in lens
            if rest[:l] in available and rest[:l] != rest
        )

    return sum(
        pat(rest[l:])
        for l in lens
        if rest[:l] in available
    )


for desired in b.split("\n"):
    desired = desired.strip()
    if not desired:
        continue

    ans += pat(desired) != 0
    ans2 += pat(desired)



print(ans)
print(ans2)

if __name__ == "__main__":
    pass
