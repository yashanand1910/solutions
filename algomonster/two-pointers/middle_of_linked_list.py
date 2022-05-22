class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == '__main__':
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)

