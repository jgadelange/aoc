from copy import deepcopy
from math import prod
from queue import Queue
from math import lcm
f = open('./input', 'r')

machines = {}
for line in f.readlines():
    line = line.strip()
    if not line:
        continue
    m, ts = line.split(" -> ")
    if m[0] == "&":
        machines[m[1:]] = {
            "type": "&",
            "targets": [t.strip() for t in ts.split(", ")],
            "state": {},
            "inputs": []
        }
    elif m[0] == "%":
        machines[m[1:]] = {
            "type": "%",
            "targets": [t.strip() for t in ts.split(", ")],
            "state": False,
            "inputs": []
        }
    else:
        machines[m] = {
            "type": "*",
            "targets": [t.strip() for t in ts.split(", ")],
        }
machines["rx"] = {"type": "d", "targets": [], "inputs": []}

for c, m in machines.items():
    for t in m["targets"]:
        try:
            if machines[t]["type"] == "&":
                machines[t]["state"][c] = False
            machines[t]["inputs"].append(c)
        except KeyError:
            print(c)
#
# paths = []
# stack = [("rx",)]
# while stack:
#     path = stack.pop()
#     if path[0] == "broadcaster":
#         paths.append(path)
#     else:
#         for i in machines[path[0]]["inputs"]:
#             if i not in path:
#                 stack.append((i,)+path)
#             else:
#                 print("loop", i, path)
#
# print(*paths, sep="\n")
#
# print([machines[inp]['type'] for inp in machines["kc"]["inputs"]])
# print(machines["kc"])

pulses = {False: 0, True: 0}
n_rx = 0
# for n in range(1000):
n = 0
q = Queue()

switches = {c: -1 for c, m in machines.items() if m["type"] == "%"}
ands = {c: -1 for c, m in machines.items() if m["type"] == "&"}
while True:
    for c in switches:
        if switches[c] == -1:
            if machines[c]["state"]:
                switches[c] = n

    # print({c: m["state"] for c, m in machines.items() if m["type"]=="%"})

    # print([(inp, machines[inp]['state']) for inp in machines["fd"]["inputs"]])
    # if all(x != -1 for x in switches.values()):
    #     print(switches)
    #
    #     print(lcm(*[x+1 for x in switches.values()]))
    #     break

    n+=1
    # machines = deepcopy(d_machines)
    # # print()
    # if n%10000 == 0:
    #     print(n)
    q.put(("broadcaster", "button", False))

    while q.qsize():
        c, src, pulse = q.get()
        # print(f"{src} -{'high' if pulse else 'low'}-> {c}")
        pulses[pulse] += 1

        m = machines[c]
        if c == "rx" and pulse is False:
            print(n)
            break

        if m["type"] == "%":
            if pulse:
                continue
            m["state"] = not m["state"]
            next_pulse = m["state"]
        elif m["type"] == "&":
            m["state"][src] = pulse
            next_pulse = not all(m["state"].values())
            if not next_pulse:
                if ands[c] == -1:
                # if n - ands[c] + 1 > 1:
                    ands[c] = n
                    if len([c for c, x in ands.items() if x == -1]) == 1:
                        print(lcm(*ands.values()))
                        exit()

        else:
            next_pulse = pulse

        for t in m["targets"]:
            q.put((t, c, next_pulse))

print(pulses)
print(prod(pulses.values()))


if __name__ == "__main__":
    pass
