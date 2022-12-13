from functools import cmp_to_key

f = open('./input', 'r')

pairs = [
    eval(line)
    for block in f.read().split("\n\n")
    for line in block.split("\n") if line
    if block
]
pairs.append([[2]])
pairs.append([[6]])


def compare(a, b):
    # print(a, b)
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return 0
        return a-b

    if isinstance(a, list) and isinstance(b, list):
        for aa, bb in zip(a, b):
            r = compare(aa, bb)
            if r != 0:
                return r
        return len(a) - len(b)

    if isinstance(a, list) and not isinstance(b, list):
        return compare(a, [b])
    if isinstance(b, list) and not isinstance(a, list):
        return compare([a], b)


sorted_pairs = sorted(pairs, key=cmp_to_key(compare))

print((sorted_pairs.index([[2]])+1) * (sorted_pairs.index([[6]])+1))
if __name__ == "__main__":
    pass
