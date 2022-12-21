import functools
import re

f = open('./input', 'r')


regex = re.compile(r'[^\d]+(\d+)'*7)
# blueprint_id, ore_cost_ore, ore_cost_clay, ore_cost_obsidian, clay_cost_obsidian, ore_cost_geode, obsidian_cost_geode

results = {}
for line in f.readlines()[:3]:
    print(line)
    blueprint_id, ore_cost_ore, ore_cost_clay, ore_cost_obsidian, clay_cost_obsidian, ore_cost_geode, obsidian_cost_geode = list(map(int, regex.match(line).groups()))
    max_ore_cost = max(ore_cost_ore, ore_cost_clay, ore_cost_obsidian, ore_cost_obsidian)


    @functools.cache
    def get_max_geo(item):
        time_left, (orep, ore, core), (clayp, clay, cclay), (obsp, obs, cobs), (geop, geo, cgeo) = item

        if time_left == 0:
            return geo

        ncore = ore_cost_ore <= ore
        ncclay = ore_cost_clay <= ore
        ncobs = ore_cost_obsidian <= ore and clay_cost_obsidian <= clay
        ncgeo = ore_cost_geode <= ore and obsidian_cost_geode <= obs

        if ncgeo and not cgeo:
            return get_max_geo((
                time_left-1,
                (orep, orep+ore-ore_cost_geode, False),
                (clayp, clayp+clay, False),
                (obsp, obsp+obs-obsidian_cost_geode, False),
                (geop+1, geop+geo, False)
            ))

        max_geo = get_max_geo((
            time_left-1,
            (orep, orep+ore, ncore),
            (clayp, clayp+clay, ncclay),
            (obsp, obsp+obs, ncobs),
            (geop, geop+geo, ncgeo)
        ))

        if ncore and not core and orep < max_ore_cost:
            max_geo = max(max_geo, get_max_geo((
                time_left-1,
                (orep+1, orep+ore-ore_cost_ore, False),
                (clayp, clayp+clay, False),
                (obsp, obsp+obs, False),
                (geop, geop+geo, False)
            )))

        if ncclay and not cclay and clayp < clay_cost_obsidian:
            max_geo = max(max_geo, get_max_geo((
                time_left-1,
                (orep, orep+ore-ore_cost_clay, False),
                (clayp+1, clayp+clay, False),
                (obsp, obsp+obs, False),
                (geop, geop+geo, False)
            )))

        if ncobs and not cobs and obsp < obsidian_cost_geode:
            max_geo = max(max_geo, get_max_geo((
                time_left-1,
                (orep, orep+ore-ore_cost_obsidian, False),
                (clayp, clayp+clay-clay_cost_obsidian, False),
                (obsp+1, obsp+obs, False),
                (geop, geop+geo, False)
            )))

        return max_geo


    max_geo = get_max_geo((32, (1, 0, False), (0, 0, False), (0, 0, False), (0, 0, False)))
    results[blueprint_id] = max_geo
    print(max_geo)

print(results)
print(results[1]*results[2]*results[3])

if __name__ == "__main__":
    pass
