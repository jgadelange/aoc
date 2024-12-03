import re

f = open('./input', 'r')

inp = f.read()

mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")

total = 0
do = True
for a, b, yes, no in mul.findall(inp):
    if no:
        do = False
        continue
    if yes:
        do = True
        continue
    if do:
        total += int(a)*int(b)
print(total)


if __name__ == "__main__":
    pass
