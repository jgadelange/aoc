from collections import defaultdict

f = open('./input', 'r')

a, b = f.read().split('\n\n')

available = a.split(", ")
lens = set(len(a) for a in available)

ans = 0
ans2 = 0
for desired in b.split("\n"):
    desired = desired.strip()
    if not desired:
        continue

    num_pos = defaultdict(int)
    dl = len(desired)
    for i in range(dl):
        rest = dl - i
        for l in lens:
            if l > rest:
                continue
            if desired[i:i+l] in available:
                if i == 0:
                    num_pos[i + l] += 1
                else:
                    num_pos[i + l] += num_pos[i]

    ans += num_pos[dl] != 0
    ans2+= num_pos[dl]

print(ans)
print(ans2)

if __name__ == "__main__":
    pass
