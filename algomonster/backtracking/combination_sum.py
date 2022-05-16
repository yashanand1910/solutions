from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(path, target, start_index, list):
        if target <= 0:
            if target == 0:
                list.append(path[:])
            return
        for i in range(start_index, len(candidates)):
            path.append(candidates[i])
            dfs(path, target-candidates[i], start_index, list)
            start_index += 1
            path.pop()
        
    list = []
    dfs([], target, 0, list)
    return list

if __name__ == '__main__':
    candidates = [int(x) for x in input().split()]
    target = int(input())
    res = combination_sum(candidates, target)
    for row in res:
        print(' '.join(map(str, row)))
