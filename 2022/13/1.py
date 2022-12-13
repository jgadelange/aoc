f = open('./example', 'r')

pairs = [
    [eval(line) for line in block.split("\n") if line]
    for block in f.read().split("\n\n")
    if block
]


def compare(a, b):
    # print(a, b)
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b

    if isinstance(a, list) and isinstance(b, list):
        for aa, bb in zip(a, b):
            r = compare(aa, bb)
            if r is not None:
                return r
        if len(a) > len(b):
            return False
        if len(a) < len(b):
            return True

    if isinstance(a, list) and not isinstance(b, list):
        return compare(a, [b])
    if isinstance(b, list) and not isinstance(a, list):
        return compare([a], b)

tot = 0
for i, pair in enumerate(pairs):
    print(pair)
    r = compare(*pair)
    if r is True or r is None:
        tot += (i+1)
    print(r)
    # print()

print(tot)

if __name__ == "__main__":
    pass
