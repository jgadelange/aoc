import re

f = open('./input', 'r')

workflows, ratings = f.read().split("\n\n")
re_flow = re.compile(r"(\w+)\{([^}]+)}")

flows = {}
for flow in workflows.split("\n"):
    name, rules = re_flow.match(flow).groups()
    flows[name] = []
    for rule in rules.split(","):
        if ":" not in rule:
            flows[name].append(("True", rule))
            continue
        iff, then = rule.split(":")
        flows[name].append((iff, then))

re_rating = re.compile(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
total=0
for rating in ratings.split("\n"):
    if not rating.strip():
        continue
    x, m, a, s = re_rating.match(rating).groups()
    x=int(x)
    m=int(m)
    a=int(a)
    s=int(s)

    res = None
    current_flow = flows["in"]
    i = 0
    while True:
        rule, nex = current_flow[i]
        b = eval(rule)
        if b:
            if nex == "A":
                total+=x+m+a+s
                break
            if nex == "R":
                break
            current_flow = flows[nex]
            i = 0
        else:
            i+=1


print(total)

if __name__ == "__main__":
    pass
