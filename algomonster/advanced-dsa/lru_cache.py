from typing import List

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, size):
        self.size = int(size)
        self.keys = {}
        self.head = None
        self.tail = None

    def put(self, key, value):
        if not self.head:
            self.keys[key] = self.head = self.tail = Node((key, value))
            return
        self.keys[key] = Node((key, value))
        self.head.next = self.keys[key]
        self.keys[key].prev = self.head
        self.head = self.keys[key]
        if len(self.keys) > self.size:
            del self.keys[self.tail.value[0]]
            self.tail = self.tail.next
            self.tail.prev = None

    def get(self, key):
        if key in self.keys:
            node = self.keys[key]
            if node is self.head:
                return node.value[1]
            if node is self.tail:
                self.tail = self.tail.next
                self.tail.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.head.next = node
            node.prev = self.head
            self.head = node
            node.next = None
            return node.value[1]
        else:
            return -1

def exec(operations: List[List[str]]) -> List[int]:
    res = []
    cache = None

    for operation, *data in operations:
        if operation == 'LRUCache':
            cache = LRUCache(*data)
        elif operation == 'put':
            cache.put(*data)
        elif operation == 'get':
            res.append(cache.get(*data))

    return res

if __name__ == '__main__':
    operations = [input().split() for _ in range(int(input()))]
    res = exec(operations)
    print(' '.join(map(str, res)))

