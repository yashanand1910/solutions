from typing import List
from collections import deque

def construct_graph(tasks, requirements):
    graph = { task: [] for task in tasks }
    parents = { task: 0 for task in tasks }
    for req in requirements:
        graph[req[0]].append(req[1])
        parents[req[1]] += 1
    return graph, parents

def task_scheduling_2(tasks: List[str], times: List[int], requirements: List[List[str]]) -> int:
    times = { task: time for task, time in zip(tasks, times) }
    graph, parents = construct_graph(tasks, requirements)
    queue = deque()
    total_time = 0
    local_max = 0
    for task, count in parents.items():
        if count == 0:
            queue.append(task)
    while queue:
        task = queue.popleft()
        if times[task] > local_max:
            local_max = times[task]
        if len(queue) == 0:
            total_time += local_max
            local_max = 0
        for child in graph[task]:
            parents[child] -= 1
            if parents[child] == 0:
                queue.append(child)
    return total_time

if __name__ == '__main__':
    tasks = input().split()
    times = [int(x) for x in input().split()]
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)

