f = open('./input', 'r')

total = 0
for op in f.readlines()[0].split(","):
    op = op.strip()
    current = 0
    for c in op:
        current += ord(c)
        current *= 17
        current %= 256
    print(repr(op), current)
    total += current

print(total)

if __name__ == "__main__":
    pass
