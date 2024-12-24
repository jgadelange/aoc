from collections import defaultdict

f = open('./input', 'r')

values, ops = f.read().split('\n\n')

values = {
    k: bool(int(v))
    for k, v in
    [line.split(": ") for line in values.split('\n')]
}

operations = defaultdict(list)

for line in ops.split('\n'):
    line = line.strip()
    if not line:
        continue
    op, to = line.split(" -> ")
    a, op, b = op.split(" ")

    operations[a,b].append((a, b, op, to))

done = set()
prev = -1
while len(done) > prev:
    prev = len(done)
    print(len(done), len(operations))
    for (a,b) in operations.keys() - done:
        if a in values and b in values:
            for a,b,op,to in operations[a,b]:
                if to in values:
                    continue
                v = None
                if op == 'AND':
                    v = values[a] and values[b]
                if op == 'OR':
                    v = values[a] or values[b]
                if op == 'XOR':
                    v = values[a] ^ values[b]
                print(f"{a} {values[a]} {op} {b} {values[b]} -> {to} {v}")
                values[to] = v
            done.add((a,b))

z_values = [
    (k, v)
    for k, v in values.items()
    if k[0] == "z"
]


print(list(sorted(z_values)))
z = "".join(str(int(v)) for _, v in reversed(sorted(z_values)))


print(z)
print(int(z, base=2))


if __name__ == "__main__":
    pass
