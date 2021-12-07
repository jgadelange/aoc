f = open('./input', 'r')
inp = [int(x) for x in f.readline().split(",") if x]

print(min(list(map(lambda loc: sum(((abs(x-loc)) * (abs(x-loc) + 1) // 2) for x in inp), range(max(inp))))))

f.close()
