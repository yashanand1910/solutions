from collections import deque
from typing import List

def daily_temperatures(t: List[int]) -> List[int]:
    queue = deque()
    n = len(t)
    res = [0] * n
    for i, temp in enumerate(t):
        count = 0
        while queue and t[queue[-1]] < temp:
            res[queue[-1]] = i - queue[-1]
            queue.pop()
        queue.append(i)
    return res

if __name__ == '__main__':
    t = [int(x) for x in input().split()]
    res = daily_temperatures(t)
    print(' '.join(map(str, res)))

