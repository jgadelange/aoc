from functools import cmp_to_key

f = open('./input', 'r')

order = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2"
]

def compare(a, b):
    ca, _ = a
    cb, b = b

    numsa = sorted([ca.count(o) for o in order], reverse=True)
    numsb = sorted([cb.count(o) for o in order], reverse=True)

    if numsa != numsb:
        for aa, bb in zip(numsa, numsb):
            if aa - bb != 0:
                return aa - bb

    for aa, bb in zip(ca, cb):
        d = order.index(aa) - order.index(bb)
        # print(aa,bb, d)
        if d != 0:
            return -d
    return 0


hands = [
    (line.split()[0], int(line.split()[1]))
    for line in f.readlines()
    if line.strip()
]

sorted_hands = sorted(hands, key=cmp_to_key(compare))
print(sorted_hands)
print(sum(i*x for i, (_, x) in enumerate(sorted_hands, start=1)))


if __name__ == "__main__":
    pass
