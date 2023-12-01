f = open('./input', 'r')

data = f.read()

def isdigit(s):
    try:
        int(s)
    except:
        return False
    else:
        return True

numbers = []
for line in data.split("\n"):
    if not line.strip():
        continue
    ns = list(filter(isdigit, line))
    numbers.append(ns)

print(numbers)

print(sum(
    int(ns[0]+ns[-1])
    for ns in numbers
))

if __name__ == "__main__":
    pass
