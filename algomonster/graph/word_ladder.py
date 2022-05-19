from typing import List
from collections import deque

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    def word_adjacent(word1, word2):
        count = 0
        for i in range(len(word2)):
            if word1[i] != word2[i]:
                count += 1
        return count == 1

    def get_next_words(word, visited):
        for i in range(len(word_list)):
            if word_list[i] not in visited and word_adjacent(word, word_list[i]):
                yield word_list[i]

    def bfs():
        queue = deque([begin])
        steps = 1
        visited = set()
        visited.add(begin)
        while queue:
            n = len(queue)
            for _ in range(n):
                word = queue.popleft()
                for next in get_next_words(word, visited):
                    if next == end:
                        return steps
                    queue.append(next)
                    visited.add(next)
            steps += 1

    return bfs()

if __name__ == '__main__':
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)

