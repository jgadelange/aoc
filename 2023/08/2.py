import re
from math import lcm

f = open('./input', 'r')

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


s = tuple(a for a in mapping if a[-1]=="A")
c = s
l = []
i = 0

while len(l) < len(s):
    c = list(
        mapping[a][lr_map[instr[i%len(instr)]]]
        for a in c
    )
    i+=1
    for a in c:
        if a[-1] == "Z":
            l.append(i)
    c = list(a for a in c if a[-1]!="Z")
print(lcm(*l))
if __name__ == "__main__":
    pass
