from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def dfs(path, start_index, list):
        list.append(path[:])
        for i in range(start_index, len(nums)):
            path.append(nums[i])
            dfs(path, i + 1, list)
            path.pop()
    list = []
    dfs([], 0, list)
    return list

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = subsets(nums)
    res = [' '.join(str(x) for x in sorted(subset)) for subset in res]
    res.sort()
    for row in res:
        print(row)
