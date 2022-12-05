from collections import defaultdict
from copy import deepcopy

f = open('./input', 'r')

data = f.read()
stack_data, move_data = data.split("\n\n")

stacks = defaultdict(list)

for line in reversed(stack_data.split("\n")[:-1]):
    for n in range(((len(line)+1)//4)):
        i = 1 + n*4
        contents = line[i]
        if contents != " ":
            stacks[f"{n+1}"].append(contents)

stacks2 = deepcopy(stacks)

for line in move_data.split("\n"):
    if not line:
        continue
    _, count, _, source, _, dest = line.split()

    count = int(count)

    stacks2[dest].extend(stacks2[source][-count:])
    for _ in range(count):
        stacks[dest].append(stacks[source].pop())
        stacks2[source].pop()

print("".join(s[-1] for s in stacks.values()))
print("".join(s[-1] for s in stacks2.values()))


if __name__ == "__main__":
    pass
