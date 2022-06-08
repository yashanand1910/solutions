from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    res = []
    for idx, (x1, y1) in enumerate(intervals):
        if not res or x1 > res[-1][1]:
            res.append([x1, y1])
            continue
        res[-1][1] = max(y1, res[-1][1])
    return res

if __name__ == '__main__':
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_intervals(intervals)
    for row in res:
        print(' '.join(map(str, row)))

