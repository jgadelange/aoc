from copy import deepcopy
from math import prod
from queue import Queue
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
        }
    elif m[0] == "%":
        machines[m[1:]] = {
            "type": "%",
            "targets": [t.strip() for t in ts.split(", ")],
            "state": False,
        }
    else:
        machines[m] = {
            "type": "*",
            "targets": [t.strip() for t in ts.split(", ")],
        }

for c, m in machines.items():
    for t in m["targets"]:
        try:
            if machines[t]["type"] == "&":
                machines[t]["state"][c] = False
        except KeyError:
            continue
print(machines)
d_machines = machines
# exit()
pulses = {False: 0, True: 0}
n_rx = 0
# for n in range(1000):
while True:
    # machines = deepcopy(d_machines)
    # print()
    q = Queue()

    q.put(("broadcaster", "button", False))

    while q.qsize():
        c, src, pulse = q.get()
        # print(f"{src} -{'high' if pulse else 'low'}-> {c}")
        pulses[pulse] += 1
        try:
            m = machines[c]
        except KeyError:
            if c == "rx" and pulse is False:
                n_rx+=1
                print(n)
                break
            continue
        if m["type"] == "%":
            if pulse:
                continue
            m["state"] = not m["state"]
            next_pulse = m["state"]
        elif m["type"] == "&":
            m["state"][src] = pulse
            next_pulse = not all(m["state"].values())
        else:
            next_pulse = pulse

        for t in m["targets"]:
            q.put((t, c, next_pulse))

print(pulses)
print(prod(pulses.values()))


if __name__ == "__main__":
    pass
