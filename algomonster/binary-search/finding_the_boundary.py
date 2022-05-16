from typing import List

def find_boundary(arr: List[bool]) -> int:
    index = 0
    while index < len(arr) and not arr[index]:
        index += 1
    return index if index < len(arr) else -1

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
