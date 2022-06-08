from typing import List

def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    x, y = new_interval
    inserted = False
    res = []
    if not intervals or y < intervals[0][0]:
        res.append(new_interval)
        inserted = True

    i = 0
    while i < len(intervals):
        p, q = intervals[i]
        if q < x or inserted:
            res.append(intervals[i])
            i += 1
            continue
        elif p > x:
            res.append(new_interval)
            inserted = True
            continue
        x_min = min(x, p)
        while i < len(intervals) and p <= y:
            y_max = max(y, q)
            i += 1
            p, q = intervals[i] if i < len(intervals) else (float('inf'), float('inf'))
        res.append([x_min, y_max])
        inserted = True

    if not inserted:
        res.append(new_interval)

    return res

if __name__ == '__main__':
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    new_interval = [int(x) for x in input().split()]
    res = insert_interval(intervals, new_interval)
    for row in res:
        print(' '.join(map(str, row)))

