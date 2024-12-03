import re

f = open('./input', 'r')

inp = f.read()
mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

s = mul.findall(inp)
print(sum(
    int(a)*int(b)
    for a,b in s
))

if __name__ == "__main__":
    pass
