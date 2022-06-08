from typing import List

def meeting_rooms(intervals: List[List[int]]) -> bool:
    intervals.sort(key = lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i-1][1] >= intervals[i][0]:
            return False
    return True

if __name__ == '__main__':
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = meeting_rooms(intervals)
    print('true' if res else 'false')

