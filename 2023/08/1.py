import re

f = open('./example2', 'r')

lines = f.readlines()
instr = lines[0].strip()

lr_map = {"L": 0, "R":1}

patt = re.compile("(\w+) = \((\w+), (\w+)\)")

mapping = [
    patt.match(line).groups()
    for line in lines[2:]
]
mapping = {
    a: (l, r)
    for a, l, r in mapping
}

c = "AAA"
i = 0
while c != "ZZZ":
    c = mapping[c][lr_map[instr[i%len(instr)]]]
    i+=1
print(i)
if __name__ == "__main__":
    pass
