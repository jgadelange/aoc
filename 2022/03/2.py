f = open('./input', 'r')

A = ord("A")
a = ord("a")


def prio(v):
    o = ord(v)
    if o >= a:
        return o - a + 1
    return o - A + 27


lines = [line.strip() for line in f.readlines()]
value = 0
for aa,bb,cc in zip(*[iter(lines)]*3):
    duplicates = set(aa).intersection(bb).intersection(cc)
    duplicate = duplicates.pop()
    value += prio(duplicate)

print(value)

if __name__ == "__main__":
    pass
