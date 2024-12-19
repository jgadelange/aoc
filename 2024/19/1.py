f = open('./input', 'r')

a, b = f.read().split('\n\n')

available = set(a.split(", "))
lens = set(len(a) for a in available)

ans = 0
for desired in b.split("\n"):
    desired = desired.strip()
    if not desired:
        continue

    stack = [0]
    tried = {0}
    while stack:
        current = stack.pop()
        if current == len(desired):
            ans+=1
            break
        rest = desired[current:]
        for l in lens:
            if l+current not in tried and rest[:l] in available:
                stack.append(current+l)
                tried.add(l+current)
print(ans)

if __name__ == "__main__":
    pass
