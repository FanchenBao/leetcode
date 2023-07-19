# from pudb import set_trace; set_trace()
from typing import List
import math

class ListNode:
    def __init__(self, key: int = -1, val: int = -1, prev_=None, next_=None):
        self.key = key
        self.val = val
        self.prev = prev_
        self.next = next_


class LRUCache:
    """LeetCode 146

    Use doubly-linked list.

    838 ms, faster than 55.50%
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.node_map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _append(self, node: ListNode):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
    
    def _pop(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    def _move_to_end(self, node: ListNode):
        self._pop(node)
        self._append(node)

    def get(self, key: int) -> int:
        if key in self.node_map:
            self._move_to_end(self.node_map[key])
            return self.node_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.node_map[key].val = value
            self._move_to_end(self.node_map[key])
        else:
            if len(self.node_map) == self.cap:
                popped_node = self.head.next
                self._pop(popped_node)
                del self.node_map[popped_node.key]
            self._append(ListNode(key=key, val=value))
            self.node_map[key] = self.tail.prev
            



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
