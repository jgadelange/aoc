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
    if isinstance(m, int):
        return m

    return eval(f"{get(m[0])} {m[1]} {get(m[2])}")


print(get("root"))


if __name__ == "__main__":
    pass
