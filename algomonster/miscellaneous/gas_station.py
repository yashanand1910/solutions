from typing import List

def starting_station(gas: List[int], dist: List[int]) -> int:
    n = len(gas)
    i = 0
    start = 0
    count = 0
    cur_count = 0
    cur_gas = 0
    while count < 2 * n:
        cur_gas += gas[i] - dist[i]
        count += 1
        cur_count += 1
        i = (i + 1) % n
        if cur_gas < 0:
            start = i
            cur_gas = 0
            cur_count = 0
        if cur_count == n:
            return start

    return -1

if __name__ == '__main__':
    gas = [int(x) for x in input().split()]
    dist = [int(x) for x in input().split()]
    res = starting_station(gas, dist)
    print(res)

