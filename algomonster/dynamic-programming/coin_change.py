from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    def dp(coins, amount):
        if amount in memo: return memo[amount]
        if amount < 0:
            return -1
        n = []
        for i, c in enumerate(coins):
            res = dp(coins, amount - c)
            if amount - c not in memo: memo[amount - c] = res
            if res > -1: n.append(res) 
        if len(n) == 0:
            return -1
        return 1 + min(n)
    memo = {0: 0}
    return dp(coins, amount)

if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)

