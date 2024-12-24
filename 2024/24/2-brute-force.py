from collections import defaultdict
from itertools import combinations

f = open('./input', 'r')

values, ops = f.read().split('\n\n')

valu = {
    k: bool(int(v))
    for k, v in
    [line.split(": ") for line in values.split('\n')]
}


def get_value(vs, start):
    z_values = [
        (k, v)
        for k, v in vs.items()
        if k[0] == start
    ]
    return int("".join(str(int(v)) for _, v in reversed(sorted(z_values))), base=2)


x = get_value(valu, "x")
y = get_value(valu, "y")

operations = defaultdict(list)
os = set()
for line in ops.split('\n'):
    line = line.strip()
    if not line:
        continue
    op, to = line.split(" -> ")
    a, op, b = op.split(" ")

    operations[a,b].append((a, b, op, to))
    os.add((a,b,op,to))

print(max(operations.values(), key=len))

desired_z_values = f"{(x+y):b}"
print(desired_z_values)
desired_z_values = {
    f"z{int(i):02d}": bool(int(x))
    for i, x in enumerate(reversed(desired_z_values))
}
print(desired_z_values)


def swap(one, two):
    (a1,b1,op1,to1) = one
    (a2,b2,op2,to2) = two
    return (a1,b1,op1,to2),(a2,b2,op2,to1)


for a, b in combinations(os, 2):
    for c, d in combinations(os - {a,b}, 2):
        for e, f in combinations(os - {a,b,c,d}, 2):
            ops = os - {a,b,c,d,e,f} | set(swap(a,b)) | set(swap(c,d)) | set(swap(e,f))

            done = set()
            values = valu
            stop = True
            prev = -1
            while len(done) > prev and stop:
                prev = len(done)
                for (aa,bb,op,to) in ops - done:
                    if aa in values and bb in values:
                        if to in values:
                            continue
                        v = None
                        if op == 'AND':
                            v = values[aa] and values[bb]
                        if op == 'OR':
                            v = values[aa] or values[bb]
                        if op == 'XOR':
                            v = values[aa] ^ values[bb]
                        values[to] = v

                        if to[0] == "z":
                            if desired_z_values.get(to, False) != v:
                                stop=False
                                break
                        done.add((a,b, op,to))

            if get_value(values, "z") == x+y:
                print(",".join(sorted(c[3] for c in [a,b,c,d,e,f])))
                exit()


if __name__ == "__main__":
    pass
