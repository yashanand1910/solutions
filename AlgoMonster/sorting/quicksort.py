from typing import List

def sort_list_interval(unsorted_list: List[int], a, b) -> None:
    # set pivot
    if a>=b: return;
    pivot = b;
    
    # swaps to segregate 2 groups
    start, end = a, pivot
    while start < end:
        if unsorted_list[start] <= unsorted_list[pivot]:
            start += 1
        elif unsorted_list[end] >= unsorted_list[pivot]:
            end -= 1
        else:
            unsorted_list[start], unsorted_list[end] = unsorted_list[end], unsorted_list[start]
    
    unsorted_list[start], unsorted_list[pivot] = unsorted_list[pivot], unsorted_list[start]
    pivot = start
    
    # sort the groups
    sort_list_interval(unsorted_list, a, pivot-1)
    sort_list_interval(unsorted_list, pivot, b)

def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list)-1)
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
