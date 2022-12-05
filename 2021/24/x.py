data = [line.strip() for line in open("input").readlines()]


def alu(inp, instrs, pre_mem=None):
    inp = list(reversed(inp))
    mem = {**{x: 0 for x in "wxyz"}, **(pre_mem or {})}
    for instr in instrs:
        if instr.startswith("inp"):
            mem[instr.split()[1]] = inp.pop()
            continue
        code, a, b = instr.split()
        val = mem[b] if b in mem else int(b)
        if code == "add":
            mem[a] += val
        if code == "mul":
            mem[a] *= val
        if code == "div":
            mem[a] //= val
        if code == "mod":
            mem[a] %= val
        if code == "eql":
            mem[a] = 1 if val == mem[a] else 0
    return mem


def clamp(x):
    return max(1, min(9, x))


ranges = [tuple()] * 14
todo = []
for i in range(14):
    if data[i * 18 + 4] == "div z 1":
        todo.append((int(data[i * 18 + 15].split(" ")[2]), i))
    if data[i * 18 + 4] == "div z 26":
        x, left = todo.pop()
        x += int(data[i * 18 + 5].split(" ")[2])
        ranges[left] = (clamp(1 - x), clamp(9 - x))
        ranges[i] = (clamp(1 + x), clamp(9 + x))

ans = ["".join(str(r[2 - part]) for r in ranges) for part in (1, 2)]
assert all(alu([int(x) for x in model], data)["z"] == 0 for model in ans)
print(*ans, sep="\n")

