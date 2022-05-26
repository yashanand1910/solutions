from heapq import heappop, heappush
from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    pq = []
    for n in nums:
        heappush(pq, -n)
    res = 0
    for i in range(k):
        res = -heappop(pq)
    return res

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)

