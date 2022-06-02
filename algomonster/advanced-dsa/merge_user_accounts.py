from typing import List

class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)

def merge_accounts(accounts: List[List[str]]) -> List[List[str]]:
    dsu = UnionFind()

    # to populate the sets
    for name, first_email, *emails in accounts:
        for email in emails:
            dsu.union((name, first_email), (name, email))

    # for preparing results
    new_accounts = {}
    for name, *emails in accounts:
        for email in emails:
            parent = dsu.find((name, email))
            if parent not in new_accounts: new_accounts[parent] = set()
            new_accounts[parent].add((name, email))

    res = []
    for (name, _), emails in new_accounts.items():
        res.append([name])
        email_list = []
        for _, email in emails:
            email_list.append(email)
        email_list.sort()
        res[-1] += email_list

    res.sort()
    return res

if __name__ == '__main__':
    accounts = [input().split() for _ in range(int(input()))]
    res = merge_accounts(accounts)
    for row in res:
        print(' '.join(row))

