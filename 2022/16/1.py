import re
from itertools import permutations, combinations

f = open('./input', 'r')


regex = re.compile(r"Valve (\w+) has flow rate=(\d+)")

nodes = {}
for line in f.readlines():
    if not line:
        continue
    try:
        one, two = line.split("valves")
    except ValueError:
        one, two = line.split("valve")
    match = regex.match(one)
    name, flow = match.groups()
    nodes[name] = {
        "flow": int(flow),
        "adjacent": {adj: 1 for adj in two.strip().split(", ")}
    }


for curr, node in nodes.items():
    # if node["flow"] != 0:
    #     continue
    # remove node
    for a, b in combinations(node["adjacent"].keys(), 2):
        nodes[a]["adjacent"][b] = min(node["adjacent"][a] + node["adjacent"][b], nodes[a]["adjacent"].get(b, 1_000_000))
        nodes[b]["adjacent"][a] = min(node["adjacent"][a] + node["adjacent"][b], nodes[a]["adjacent"].get(b, 1_000_000))

    if node["flow"] == 0:
        for a in node["adjacent"].keys():
            del nodes[a]["adjacent"][curr]

nodes = {key: value for key, value in nodes.items() if value["flow"] or key == "AA"}
print(len(nodes))

print("\n".join(name + f"({len(node['adjacent'])}): " + str(node) for name, node in nodes.items()))

root = "AA"
stack = [(["AA"], 0, 30)]
max_released = 0
while len(stack):
    path, released, time_left = stack.pop()
    # print(path, released, time_left)
    for adj, d in nodes[path[-1]]["adjacent"].items():
        if adj not in nodes or adj in path:
            continue
        if (new_time_left := time_left - d - 1) <= 0:
            continue
        new_path = path + [adj]
        new_released = released + (new_time_left * nodes[adj]["flow"])
        if new_released > max_released:
            max_released = new_released
            print(path + [adj])
            print(new_released)
        stack.append((new_path, new_released, new_time_left))

if __name__ == "__main__":
    pass
