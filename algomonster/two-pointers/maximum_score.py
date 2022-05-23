from typing import List

def maximum_score(arr1: List[int], arr2: List[int]) -> int:
    i, j = 0, 0
    sum1, sum2 = sum(arr1), sum(arr2)
    common = [[0, sum1, sum2, 0, 0]]
    x, y = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if i == 0 and j == 0:
                j += 1
                i += 1
                continue
            k = sum1 - x
            l = sum2 - y
            common.append([arr1[i], k, l, i, j])
            common[-2][1] -= k
            common[-2][2] -= l
            j += 1
            i += 1
        while i < len(arr1) and j < len(arr2) and arr1[i] < arr2[j]:
            x += arr1[i]
            i += 1
        while j < len(arr2) and i < len(arr1) and arr2[j] < arr1[i]:
            y += arr2[j]
            j += 1
    cur_sum = 0
    switch = False
    i = 0
    j = 0
    while (switch and i < len(arr2)) or (not switch and i < len(arr1)):
        if j < len(common) and (i == 0 or (not switch and arr1[i] == common[j][0]) or (switch and arr2[i] == common[j][0])):
            if common[j][1] < common[j][2]:
                if not switch:
                    i = common[j][4]
                    switch = not switch
            else:
                if switch:
                    i = common[j][3]
                    switch = not switch
            j += 1
        if not switch:
            cur_sum += arr1[i]
        else:
            cur_sum += arr2[i]
        i += 1
    return cur_sum % (10**9 + 7)

if __name__ == '__main__':
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    res = maximum_score(arr1, arr2)
    print(res)

