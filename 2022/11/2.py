from functools import reduce
from operator import mul, add

f = open('./input', 'r')

data = f.read()

monkeys = []


def ev(v, val):
    if v == "old":
        return val
    return int(v)


op_map = {
    "*": mul,
    "+": add,
}


def operator(oparts, value):
    r = ev(oparts[0], value)
    op = op_map[oparts[1]]
    r = op(r, ev(oparts[2], value))

    return r


for monkey_data in data.split("\n\n"):
    lines = monkey_data.split("\n")
    oparts = [x.strip() for x in lines[2][18:].strip().split(" ")]

    d = int(lines[3][20:].strip())
    t = int(lines[4][28:].strip())
    f = int(lines[5][29:].strip())

    monkey = {
        "items": [int(x) for x in lines[1][17:].strip().split(",")],
        "oparts": oparts,
        "test": d,
        "t": t,
        "f": f,
    }
    monkeys.append(monkey)

mod = reduce(mul, [x["test"] for x in monkeys])

counts = [0] * len(monkeys)

for _ in range(10_000):

    for i in range(len(monkeys)):
        while len(monkeys[i]["items"]):
            counts[i] += 1
            item = monkeys[i]["items"].pop(0)
            # print(item)
            item = operator(monkeys[i]["oparts"], item)
            # print(item)
            item = item % mod
            # print(item)

            t = item % monkeys[i]["test"] == 0
            # print(t)

            new_i = monkeys[i]["t"] if t else monkeys[i]["f"]
            # print(new_i)
            # print()
            monkeys[new_i]["items"].append(item)
    if (_+1) % 1000 == 0 or _ == 0 or _ == 19:
        print(f"{_+1}:")
        for monkey in counts:
            print(monkey)
        print()


# print(monkeys)
max2 = sorted(counts)[-2:]
print(max2[0] * max2[1])

if __name__ == "__main__":
    pass
