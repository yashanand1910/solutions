from typing import List

def remove_duplicates(arr: List[int]) -> int:
    slow, fast = 0, 0
    while fast < len(arr) - 1:
        if arr[fast + 1] == arr[fast]:
            fast += 1
            continue
        slow += 1
        fast += 1
        arr[slow] = arr[fast]
    return slow + 1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))

