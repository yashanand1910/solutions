from typing import List

def sum_subarray(weights: List[int]) -> int:
    stack = []
    total_sum = 0
    cur_sum = 0
    for i in weights:
        count = 1
        while stack and stack[-1][0] > i:
            temp = stack.pop()
            cur_sum -= temp[0] * temp[1]
            count += temp[1]
        stack.append([i, count])
        cur_sum += i * count
        total_sum += cur_sum
    return total_sum

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    res = sum_subarray(weights)
    print(res)

