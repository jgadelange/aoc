import re

f = open('./input', 'r')


regex = re.compile(r'[^\d]+(\d+)'*7)
# blueprint_id, ore_cost_ore, ore_cost_clay, ore_cost_obsidian, clay_cost_obsidian, ore_cost_geode, obsidian_cost_geode

# num_ore, num_ore_machine
results = {}
for line in f.readlines():
    print(line)
    blueprint_id, ore_cost_ore, ore_cost_clay, ore_cost_obsidian, clay_cost_obsidian, ore_cost_geode, obsidian_cost_geode = list(map(int, regex.match(line).groups()))

    stack = [
        (24, (1, 0, False), (0, 0, False), (0, 0, False), (0, 0, False))
    ]
    max_geo = 0
    while len(stack):
        # print(len(stack))
        time_left, (orep, ore, core), (clayp, clay, cclay), (obsp, obs, cobs), (geop, geo, cgeo) = stack.pop()
        # print(len(stack))
        if time_left == 0:
            if geo > max_geo:
                print(geo)
                max_geo = geo
            continue

        ncore = ore_cost_ore <= ore
        ncclay = ore_cost_clay <= ore
        ncobs = ore_cost_obsidian <= ore and clay_cost_obsidian <= clay
        ncgeo = ore_cost_geode <= ore and obsidian_cost_geode <= obs

        stack.append((
            time_left-1,
            (orep, orep+ore, ncore),
            (clayp, clayp+clay, ncclay),
            (obsp, obsp+obs, ncobs),
            (geop, geop+geo, ncgeo)
        ))

        if ncore and not core:
            stack.append((
                time_left-1,
                (orep+1, orep+ore-ore_cost_ore, False),
                (clayp, clayp+clay, False),
                (obsp, obsp+obs, False),
                (geop, geop+geo, False)
            ))

        if ncclay and not cclay:
            stack.append((
                time_left-1,
                (orep, orep+ore-ore_cost_clay, False),
                (clayp+1, clayp+clay, False),
                (obsp, obsp+obs, False),
                (geop, geop+geo, False)
            ))

        if ncobs and not cobs:
            stack.append((
                time_left-1,
                (orep, orep+ore-ore_cost_obsidian, False),
                (clayp, clayp+clay-clay_cost_obsidian, False),
                (obsp+1, obsp+obs, False),
                (geop, geop+geo, False)
            ))

        if ncgeo and not cgeo:
            stack.append((
                time_left-1,
                (orep, orep+ore-ore_cost_geode, False),
                (clayp, clayp+clay, False),
                (obsp, obsp+obs-obsidian_cost_geode, False),
                (geop+1, geop+geo, False)
            ))
    results[blueprint_id] = max_geo

print(sum(
    i*x for i, x in results.items()
))

if __name__ == "__main__":
    pass
