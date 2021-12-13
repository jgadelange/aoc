f = open('./input', 'r')
scores = {
    "(": 1,
    ")": 1,
    "[": 2,
    "]": 2,
    "{": 3,
    "}": 3,
    "<": 4,
    ">": 4,
}

mapping = {
    ")": "(",
    "(": ")",
    "]": "[",
    "[": "]",
    "}": "{",
    "{": "}",
    ">": "<",
    "<": ">",
}
opening = {"(", "[", "{", "<"}
closing = set(mapping.keys()) - opening

score = 0
closing_scores = []
for line in f.readlines():
    line = line.strip()
    stack = []
    broken = False
    for c in line:
        if c in opening:
            stack.append(c)
        if c in closing:
            top = stack.pop()
            if mapping[c] != top:
                score += scores[c]
                broken = True
                break
    if broken:
        continue
    if len(stack):
        cs = 0
        # string_to_score = [mapping[c] for c in reversed(stack)]
        for c in reversed(stack):
            cs = (cs * 5) + scores[mapping[c]]
        closing_scores.append(cs)

closing_scores.sort()
print(closing_scores[len(closing_scores)//2])

f.close()
