import sys

f = open('./input', 'r')


monkeys = {}
for line in f.readlines():
    if not line.strip():
        continue
    monkey, operation = line.strip().split(": ")
    try:
        monkeys[monkey] = int(operation)
    except ValueError:
        monkeys[monkey] = operation.split()


def get(name):
    m = monkeys[name]
    if name == "humn" and not isinstance(m, int):
        return name

    if isinstance(m, int):
        return m

    l = get(m[0])
    r = get(m[2])
    return (f"({l} {m[1]} {r})")


monkeys["root"][1] = "=="
monkeys["humn"] = "DDFJOJFDO"

l = (monkeys["root"][0])
r = (monkeys["root"][2])

humn_in_l = "humn" in get(l)
humn_in_r = "humn" in get(r)

if humn_in_r and humn_in_l:
    print("AHOH!")
    exit(1)

fn = l if humn_in_l else r
res = eval(get(l)) if humn_in_r else eval(get(r))

monkeys["humn"] = 0
a0 = eval(get(fn))
monkeys["humn"] = 1
a1 = eval(get(fn))

increasing_fn = a0 < a1

lower = 0
upper = sys.maxsize
while True:
    c = (lower + upper) // 2
    monkeys["humn"] = c

    a = eval(get(fn))

    if a == res:
        print(c)
        break

    if a < res and increasing_fn or res < a and not increasing_fn:
        lower = c+1
    else:
        upper = c-1

if __name__ == "__main__":
    pass
