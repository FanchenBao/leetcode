# from pudb import set_trace; set_trace()
from typing import List, Tuple, Optional


class MyHashMap1:

    def __init__(self):
        """
        LeetCode 706

        Initialize your data structure here.

        This is a list of list implementation of hash map. Very basic. Collision
        is handled by extending the internal list. Removal is handled by
        resetting the target key-value pair to [-1, -1]

        236 ms, 59% ranking.
        """
        self.size = 10000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        empty = []
        for i, [k, v] in enumerate(self.map[idx]):
            if k < 0:
                empty.append(i)
            if k == key:
                self.map[idx][i][1] = value
                break
        else:
            if empty:
                self.map[idx][empty[0]] = [key, value]
            else:
                self.map[idx].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        for i, [k, v] in enumerate(self.map[idx]):
            if k == key:
                return v
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        for i, [k, v] in enumerate(self.map[idx]):
            if k == key:
                self.map[idx][i] = [-1, -1]


class MyHashMap2:

    def __init__(self):
        """
        Initialize your data structure here.

        This is the same implementation as above, but with fewer lines of code
        and more memory usage, because we use an additional list of list to
        handle empty spaces.
        """
        self.size = 10000
        self.map = [[] for _ in range(self.size)]
        self.empty = [[] for _ in range(self.size)]

    def _find_target(self, key: int) -> Tuple[int]:
        idx = key % self.size
        for i, [k, _] in enumerate(self.map[idx]):
            if k == key:
                return idx, i
        return idx, -1

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx, i = self._find_target(key)
        if i >= 0:
            self.map[idx][i][1] = value
        else:
            if self.empty[idx]:
                self.map[idx][self.empty[idx].pop()] = [key, value]
            else:
                self.map[idx].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx, i = self._find_target(key)
        return self.map[idx][i][1] if i >= 0 else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx, i = self._find_target(key)
        if i >= 0:
            self.map[idx][i] = [-1, -1]


class ListNode:
    def __init__(self, key: int = -1, value: int = -1, next_=None):
        self.key = key
        self.value = value
        self.next = next_


class MyHashMap3:

    def __init__(self):
        """
        Initialize your data structure here.

        This is the same implementation as above, but with fewer lines of code
        and more memory usage, because we use an additional list of list to
        handle empty spaces.
        """
        self.size = 1000
        self.map = [None] * self.size

    def _find_target(self, key: int) -> Tuple[int, Optional[ListNode]]:
        idx = key % self.size
        cur = self.map[idx]
        pre = ListNode(next_=cur)  # a dummy node
        while cur:
            if cur.key == key:
                break
            pre = pre.next
            cur = cur.next
        return idx, cur, pre

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx, node, _ = self._find_target(key)
        if node:
            node.value = value
        else:
            self.map[idx] = ListNode(key=key, value=value, next_=self.map[idx])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx, node, _ = self._find_target(key)
        return node.value if node else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx, cur, pre = self._find_target(key)
        if cur:
            pre.next = cur.next
        # this is a check to see if the head of the linked list is removed
        if pre.key < 0:
            self.map[idx] = pre.next


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
