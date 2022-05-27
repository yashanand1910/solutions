from math import ceil
from heapq import heappush, heappop
from typing import Counter

def reorganize_string(s: str) -> str:
    counts = [0] * 26
    for c in s:
        counts[ord(c) - 97] += 1
    pq = []
    for i, count in enumerate(counts):
        if count: heappush(pq, (-count, chr(i + 97)))
    n = len(s)
    res = [''] * n
    count, x = heappop(pq)
    if -count > ceil(n / 2): return ''
    i = 0
    while count:
        res[i] = x
        i += 2
        count += 1
    while pq:
        count, x = heappop(pq)
        while count:
            if i > n:
                i = 1
            res[i] = x
            i += 2
            count += 1
    return ''.join(res)

if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i+1}")
            exit()
    print("Valid")

