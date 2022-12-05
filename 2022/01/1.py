f = open('./input', 'r')

data = f.read()

elfs = [[int(x) for x in elf.split("\n") if x] for elf in data.split("\n\n")]

x = list(reversed(sorted((sum(elf) for elf in elfs))))

print(x[0])
print(sum(x[:3]))
