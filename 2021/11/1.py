f = open('./input', 'r')
scores = {
    "(": 3,
    ")": 3,
    "[": 57,
    "]": 57,
    "{": 1197,
    "}": 1197,
    "<": 25137,
    ">": 25137,
}

mapping = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
opening = set(mapping.values())
closing = set(mapping.keys())

score = 0
for line in f.readlines():
    line = line.strip()
    stack = []
    for c in line:
        if c in opening:
            stack.append(c)
        if c in closing:
            top = stack.pop()
            if mapping[c] != top:
                score += scores[c]
                break
print(score)

f.close()
