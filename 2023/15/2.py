from collections import defaultdict

f = open('./input', 'r')

total = 0


def hash(op):
    current = 0
    for c in op:
        current += ord(c)
        current *= 17
        current %= 256
    return current

boxes = defaultdict(dict)
labels = {}
for op in f.readlines()[0].split(","):
    op = op.strip()
    if op[-1]=="-":
        op = op[:-1]
        b = hash(op)
        if op in boxes[b]:
            del boxes[b][op]
        continue

    op, l = op.split("=")
    l = int(l)
    b = hash(op)
    boxes[b][op] = l

total = 0
for i, x in boxes.items():
    for j, l in enumerate(x.values()):
        print(i, j, l)
        total += (i+1) * (j+1) * l


print(total)

if __name__ == "__main__":
    pass
