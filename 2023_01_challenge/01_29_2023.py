# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class DLNode:
    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LFUCache:

    def __init__(self, capacity: int):
        """LeetCode 460

        Use a list to represent a doubly linked list for each number of
        frequency.

        I did this on 2022-02-27. I knew LRU Cache is doubly linked list. I
        initially forgot how to incorporate LFU. I knew the heap was not going
        to cut it due to time complexity. The trick is to use a doubly linked
        list for EACH FREQUENCY, as implemented below.

        Amortized O(1) for both get and put. 989 ms, faster than 50.06%

        UPDATE: we can keep track of min frequency instead of searching for it.
        And in that case, self.freqs only need to keep tail.

        True O(1) for both get and put. 916 ms, faster than 68.24%
        """
        self.cap = capacity
        self.count = 0
        self.map = {}  # {key: [node, freq]}
        self.freqs = []  # [[head, tail]]
        self.min_freq = 0

    def _add(self, node: DLNode, tail: DLNode) -> None:
        tail.pre.next = node
        node.pre = tail.pre
        node.next = tail
        tail.pre = node

    def _del(self, node: DLNode) -> None:
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = node.next = None

    def _add_to_freq(self, node: DLNode, new_freq: int) -> None:
        if new_freq > 1:
            if self.min_freq == new_freq - 1 and node.pre.pre is None and node.next.next is None:
                # node is the last one in the min frequency
                self.min_freq = new_freq
            self._del(node)

        if len(self.freqs) < new_freq:
            head = DLNode()
            tail = DLNode()
            head.next = tail
            tail.pre = head
            self.freqs.append([head, tail])
        self._add(node, self.freqs[new_freq - 1][1])

    def get(self, key: int) -> int:
        if self.cap == 0 or key not in self.map:
            return -1
        node = self.map[key][0]
        self.map[key][1] += 1
        self._add_to_freq(node, self.map[key][1])
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.map:
            node = self.map[key][0]
            self.map[key][1] += 1
            self._add_to_freq(node, self.map[key][1])
            node.value = value
        else:
            if self.count == self.cap:
                head, tail = self.freqs[self.min_freq]
                self._del(head.next)
                self.count -= 1
            node = DLNode(key=key, value=value)
            self.map[key] = [node, 1]
            self._add_to_freq(node, 1)
            self.count += 1
            self.min_freq = 1










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
