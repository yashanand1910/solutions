from heapq import heapify, heappop, heappush

class MedianOfStream:
    def __init__(self):
        self.minh = []
        self.maxh = []
    def add_number(self, num: float) -> None:
        if num >= self.get_median():
            if len(self.minh) > len(self.maxh):
                heappush(self.maxh, -heappop(self.minh))
            heappush(self.minh, num)
        else:
            if len(self.maxh) == len(self.minh):
                heappush(self.minh, -heappop(self.maxh))
            heappush(self.maxh, -num)

    def get_median(self) -> float:
        if len(self.minh) == 0: return 0
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] - self.maxh[0]) / 2
        return self.minh[0]

if __name__ == '__main__':
    median_of_stream = MedianOfStream()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        if line == 'get':
            median = median_of_stream.get_median()
            print(f'{median:.1f}')
        else:
            num = float(line)
            median_of_stream.add_number(num)

