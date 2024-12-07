f = open('./input', 'r')

inp = []
for line in f.readlines():
    if not line.strip():
        continue
    a, b = line.split(": ")
    inp.append((int(a), list(map(int, b.split()))))


def concat(a, b):
    return int(str(a) + str(b))

ans = 0
for total, nums in inp:
    ts = {nums[0]}
    for num in nums[1:]:
        nts = set()
        for t in ts:
            if t > total:
                continue
            nts |= {t * num, t + num}
        ts = nts

    if total in ts:
        ans+=total

print(ans)


ans = 0
for total, nums in inp:
    ts = {nums[0]}
    for num in nums[1:]:
        nts = set()
        for t in ts:
            if t > total:
                continue
            nts |= {t * num, t + num, concat(t, num)}
        ts = nts

    if total in ts:
        ans+=total

print(ans)

if __name__ == "__main__":
    pass
