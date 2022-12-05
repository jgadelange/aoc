f = open('./input', 'r')

A = ord("A")
a = ord("a")


def prio(v):
    o = ord(v)
    if o >= a:
        return o - a + 1
    return o - A + 27


value = 0
for line in f.readlines():
    line = line.strip()
    l = len(line.strip())
    half = int(round(l/2))

    duplicate = set(line[:half]).intersection(set(line[half:])).pop()

    value += prio(duplicate)

print(value)

if __name__ == "__main__":
    pass
