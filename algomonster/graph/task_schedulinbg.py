from typing import List
from collections import deque

def count_parents(tasks, requirements):
    count = { node: 0 for node in tasks }
    for i in requirements:
        count[i[-1]] += len(i) - 1
    return count

def count_children(tasks, requirments):
    count = { node: [] for node in tasks }
    for i in requirements:
        count[i[0]].append(i[-1])
    return count

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    parents_count = count_parents(tasks, requirements)
    children_count = count_children(tasks, requirements)
    queue = deque()
    for task, count in parents_count.items():
        if count == 0:
            queue.append(task)
    res = []
    while queue:
        task = queue.popleft()
        res.append(task)
        for child in children_count[task]:
            parents_count[child] -= 1
            if parents_count[child] == 0:
                queue.append(child)
    return res

if __name__ == '__main__':
    tasks = input().split()
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f'output size {len(res)} does not match input size {len(tasks)}')
        exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            exit()
    print('ok')

