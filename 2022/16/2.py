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

min_dist = min(d for n, x in nodes.items() for d in x["adjacent"].values() if n != "AA")
print(min_dist)
root = "AA"
stack = [(["AA"], 26, ["AA"], 26, 0, {n for n in nodes.keys()} - {"AA"}, sum(x["flow"] for x in nodes.values()))]
tried = set()
max_released = 0
while len(stack):
    path, time_left, path2, time_left2, released, nodes_left, flow_left = stack.pop()
    if released + (max(time_left, time_left2)-1-min_dist) * flow_left < max_released:
        continue

    # print(path, released, time_left)
    for adj in nodes_left:
        d = nodes[path[-1]]["adjacent"][adj]
        if (new_time_left := time_left - d - 1) <= 0:
            continue
        new_path = path + [adj]
        new_released = released + (new_time_left * nodes[adj]["flow"])

        tup = tuple(sorted([tuple(new_path), tuple(path2)]))

        if tup in tried:
            continue
        if new_released > max_released:
            max_released = new_released
            print(new_path, path2, new_time_left, time_left)
            print(new_released)
        tried.add(tup)
        stack.append((new_path, new_time_left, path2, time_left2, new_released, nodes_left-{adj}, flow_left-nodes[adj]["flow"]))
    for adj in nodes_left:
        d = nodes[path2[-1]]["adjacent"][adj]
        if (new_time_left := time_left2 - d - 1) <= 0:
            continue
        new_path = path2 + [adj]
        new_released = released + (new_time_left * nodes[adj]["flow"])

        tup = tuple(sorted([tuple(new_path), tuple(path)]))
        if tup in tried:
            continue

        if new_released > max_released:
            max_released = new_released
            print(path, new_path, time_left, new_time_left)
            print(new_released)
        tried.add(tup)
        stack.append((path, time_left, new_path, new_time_left, new_released, nodes_left-{adj}, flow_left-nodes[adj]["flow"]))

if __name__ == "__main__":
    pass
