from math import floor, sqrt

memo = {}
def perfect_squares(n: int) -> int:
    if n in memo: return memo[n]
    if n < 0:
        return float('inf')
    if n == 0:
        return 0
    minimum = float('inf')
    for i in range(1, floor(sqrt(n)) + 1):
        ans = perfect_squares(n - i**2)
        if ans not in memo: memo[n - i**2] = ans
        minimum = min(minimum, 1 + ans)

    return minimum

if __name__ == '__main__':
    n = int(input())
    res = perfect_squares(n)
    print(res)

