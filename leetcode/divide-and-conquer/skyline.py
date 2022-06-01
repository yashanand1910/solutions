from typing import List

def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    n = len(buildings)
    if n < 2:
        if n == 0: return []
        return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

    mid = n // 2
    l_skyline = get_skyline(buildings[:mid])
    r_skyline = get_skyline(buildings[mid:])

    # merge skylines
    l, r, skyline = 0, 0, []
    l_max, r_max = 0, 0
    n_l, n_r = len(l_skyline), len(r_skyline)
    while l < n_l or r < n_r:
        l_x, l_h = l_skyline[l] if l < n_l else [float('inf'), 0]
        r_x, r_h = r_skyline[r] if r < n_r else [float('inf'), 0]
        max_h = max(l_max, r_max)

        if l_x < r_x:
            if l_h > max_h:
                max_h = l_h
                skyline.append([l_x, l_h])
            elif l_max == max_h:
                if l_h < max_h:
                    max_h = max(l_h, r_max)
                    skyline.append([l_x, max_h])
            l_max = l_h
            l += 1
        if r_x < l_x:
            if r_h > max_h:
                max_h = r_h
                skyline.append([r_x, r_h])
            elif r_max == max_h:
                if r_h < max_h:
                    max_h = max(r_h, l_max)
                    skyline.append([r_x, max_h])
            r_max = r_h
            r += 1
        if r_x == l_x:
            skyline.append([l_x, max_h])
            r += 1
            l += 1

    return skyline

if __name__ == '__main__':
    buildings = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = get_skyline(buildings)
    for row in res:
        print(' '.join(map(str, row)))

