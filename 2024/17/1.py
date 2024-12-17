from itertools import pairwise

f = open('./input', 'r')

regs, ops = f.read().split('\n\n')

regs = [
    int(l.split(":")[1])
    for l in regs.splitlines()
]

ops = list(map(int, ops.split(":")[1].split(",")))
print(regs, ops)


def run(r, o):
    regs = r.copy()
    ops = o.copy()
    out = []
    pointer = 0
    i = 0
    while pointer < len(ops):
        i+=1
        opcode, operand = ops[pointer], ops[pointer+1]
        if opcode == 0:
            regs[0] = regs[0] // (2**combo(regs, operand))
        elif opcode == 1:
            regs[1] = regs[1] ^ operand
        elif opcode == 2:
            regs[1] = combo(regs, operand) % 8
        elif opcode == 3:
            if regs[0] != 0:
                pointer = operand
                continue
        elif opcode == 4:
            regs[1] = regs[1] ^ regs[2]
        elif opcode == 5:
            out.append(combo(regs, operand) % 8)
        elif opcode == 6:
            regs[1] = regs[0] // (2**combo(regs, operand))
        elif opcode == 7:
            regs[2] = regs[0] // (2**combo(regs, operand))
        pointer += 2
    print(i)
    return regs, out


def combo(r, op):
    if op <= 3:
        return op
    return r[op-4]


print(run([0,0,9], [2,6]))
print(run([10,0,0], [5,0,5,1,5,4]))
print(run([2024,0,0], [0,1,5,4,3,0]))
print(run([0,29,0], [1, 7]))
# print(run([0,0,9], [2,6]))
# print(run([0,0,9], [2,6]))

run([1]+regs[1:], ops)
regs, out = run(regs, ops)
print(",".join(map(str,out)))


if __name__ == "__main__":
    pass
