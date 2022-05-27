from heapq import heappop, heappush

def nth_ugly_number(n: int) -> int:
    pq = []
    heappush(pq, 1)
    i = 1
    base = (2, 3, 5)
    res = 0
    while i <= n:
        num = heappop(pq)
        if num > res:
            i += 1
            res = num
        for j in base:
            heappush(pq, j * num)
    return res

if __name__ == '__main__':
    n = int(input())
    res = nth_ugly_number(n)
    print(res)

