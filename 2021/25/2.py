import heapq
import time

starttime = time.time()
data = [x.replace("\n", "") for x in open("input").readlines()]

hallway_spots = (1, 2, 4, 6, 8, 10, 11)
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
pod_pos = {"A": 0, "B": 1, "C": 2, "D": 3}


def add(queue, done, new_cost, new_stacks, new_hallway):
    key = (new_stacks, new_hallway)
    if not key in done or new_cost < done[key]:
        done[key] = new_cost
        heapq.heappush(queue, (new_cost, new_stacks, new_hallway))


for part in (1, 2):
    if part == 2:
        data = [*data[:3], "  #D#C#B#A#  ", "  #D#B#A#C#  ", *data[3:]]
    stacks = tuple(tuple(data[y][x] for y in range(3 if part == 1 else 5, 1, -1)) for x in range(3, 11, 2))
    hallway = tuple(" " + "." * 11)
    queue = [(0, stacks, hallway)]
    done = dict()
    while queue:
        cost, stacks, hallway = heapq.heappop(queue)
        if all(len(stack) == (2 if part == 1 else 4) for stack in stacks) and \
                all(all(c == p for c in stacks[pod_pos[p]]) for p in "ABCD"):
            print(cost)
            break
        for i, stack in enumerate(stacks):
            if stack:
                stack_pos = (i + 1) * 2 + 1
                pod = stack[-1]
                for spot in hallway_spots:
                    if not all(q == "." for q in
                               (hallway[spot:stack_pos] if spot < stack_pos else hallway[stack_pos:spot + 1])):
                        continue
                    c = ((3 if part == 1 else 5) - len(stack) + abs(stack_pos - spot)) * costs[pod]
                    add(queue, done,
                        cost + c,
                        (*stacks[:i], stack[:-1], *stacks[i + 1:]),
                        (*hallway[:spot], pod, *hallway[spot + 1:]),
                        )
        for spot in hallway_spots:
            pod = hallway[spot]
            if pod == ".": continue
            i = pod_pos[pod]
            stack = stacks[i]
            if not all(p == pod for p in stack): continue
            stack_pos = (i + 1) * 2 + 1
            if not all(q == "." for q in
                       (hallway[spot + 1:stack_pos] if spot < stack_pos else hallway[stack_pos:spot])):
                continue
            c = ((2 if part == 1 else 4) - len(stack) + abs((i + 1) * 2 + 1 - spot)) * costs[pod]
            add(queue, done,
                cost + c,
                (*stacks[:i], (*stack, pod), *stacks[i + 1:]),
                (*hallway[:spot], ".", *hallway[spot + 1:]),
                )

print(f"Took {time.time()-starttime}s")
