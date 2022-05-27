from typing import List

def trapping_rain_water(elevations: List[int]) -> int:
    elevations.append(0)
    i = 0
    last_max = 0
    last_maxes = []
    pool = []
    water = 0

    while i < len(elevations):
        prev = i - 1
        last_elevation = elevations[prev] if i >= 0 else 0
        cur_elevation = elevations[i]

        if cur_elevation > last_elevation:
            last_max = i
        elif cur_elevation < last_elevation:
            if prev == last_max:
                if len(last_maxes):
                    # last_edge = last_max
                    # while elevations[last_edge - 1] == last_elevation:
                    #     last_edge -= 1
                    prev_max = last_maxes[-1]
                    if last_elevation > elevations[prev_max] and len(pool):
                        j = len(pool) - 1
                        while j >= 0 and elevations[pool[j][0]] < last_elevation:
                            if elevations[pool[j][0]] > elevations[prev_max]:
                                prev_max = pool[j][0]
                            j -= 1
                        if elevations[pool[j][0]] > elevations[prev_max]:
                            prev_max = pool[j][0]
                        height = min(elevations[prev_max], last_elevation)
                        if prev_max < last_maxes[-1]:
                            j = len(pool) - 1
                            while j >= 0 and pool[j][0] >= prev_max:
                                pool.pop()
                                j -= 1
                        pool.append([prev_max, last_max])
                    else:
                        pool.append([prev_max, last_max])
                last_maxes.append(last_max)
        else:
            if prev == last_max:
                last_max = i
        i += 1

    # fill water
    for a, b in pool:
        accum = 0
        height = min(elevations[a], elevations[b])
        for i in range(a, b):
            accum += max(0, height - elevations[i])
        water += accum
            
    return water

if __name__ == '__main__':
    elevations = [int(x) for x in input().split()]
    res = trapping_rain_water(elevations)
    print(res)

