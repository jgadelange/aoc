import re
import sys
from collections import defaultdict
from math import prod

f = open('./input', 'r')

workflows, ratings = f.read().split("\n\n")
re_flow = re.compile(r"(\w+)\{([^}]+)}")
re_rule = re.compile(r"(\w)([<>])(\d+)")

flows = {}
for flow in workflows.split("\n"):
    name, rules = re_flow.match(flow).groups()
    flows[name] = []
    for rule in rules.split(","):
        if ":" not in rule:
            flows[name].append(("True", rule))
            continue
        iff, then = rule.split(":")

        match = re_rule.match(iff)
        if match:
            (var, op, val) = match.groups()
            val = int(val)
            iff=(var, op, val)
        flows[name].append((iff, then))

adjacency = defaultdict(set)
for name, rules in flows.items():
    for i, (_, res) in enumerate(rules):
        adjacency[res].add((name, i))
stack = [(("A",0),)]


xmin, xmax, mmin, mmax, amin, amax, xmin, xmax = [-sys.maxsize, sys.maxsize] * 4

paths = []

while(len(stack)):
    path = stack.pop()
    if path[0][0] == "in":
        paths.append(path)
    for adj in adjacency[path[0][0]]:
        stack.append((adj,)+path)


total = 0
for path in paths:
    options = {
        "x": {"min": 1, "max": 4000},
        "m": {"min": 1, "max": 4000},
        "a": {"min": 1, "max": 4000},
        "s": {"min": 1, "max": 4000},
    }
    for name, target_i in path:
        if name == "A":
            continue
        rules = flows[name]
        for i in range(target_i):
            rule, _ = rules[i]
            var, op, val = rule
            if op == "<":
                options[var]["min"] = max(options[var]["min"], val)
            else:
                options[var]["max"] = min(options[var]["max"], val)

        rule, _ = rules[target_i]
        if rule == "True":
            continue
        var, op, val = rule
        if op == "<":
            options[var]["max"] = min(options[var]["max"], val-1)
        else:
            options[var]["min"] = max(options[var]["min"], val+1)

    s = prod(
        x["max"] - x["min"] + 1
        for x in options.values()
    )
    total+=s

print(total)

if __name__ == "__main__":
    pass
