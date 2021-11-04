# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, deque


class LRUCache1:

    def __init__(self, capacity: int):
        """LeetCode 146

        We use a queue to monitor the time series of the keys used. We also use
        a counter to count the number of times a key is used. The front of the
        queue represents the potentially least used key. However, if a key has
        a counter larger than 1, that means this key has been used not only
        at the front of the queue, but also somewhere else in the queue. This
        makes the key NOT LRU. Thus, we shall pop this key and look for the
        next. The true LRU key is the one at the front of the queue and has
        counter value equal 1. When the LRU key needs to be evicted, we shall
        use that key.

        I encountered a bug that is quite difficult for me to resolve. The
        problem is that when a key is used in get() call but it is already NOT
        in the cache, we shall NOT record it in the queue or counter. I didn't
        realize that and got hit by a KeyError when trying to remove a key that
        is already not inside the cache.

        O(1) for get
        Worst case O(N) for put, where N is the number of consecutive get calls

        792 ms, 77% ranking.
        """
        self.counter = Counter()
        self.cache = {}
        self.lru = deque()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.counter[key] += 1
        self.lru.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.counter[key] += 1
        self.lru.append(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            while self.counter[self.lru[0]] > 1:
                self.counter[self.lru.popleft()] -= 1
            lru_key = self.lru.popleft()
            self.counter[lru_key] -= 1
            del self.cache[lru_key]



class DoubleLinkedNode:
    def __init__(self, key: int = -1, value: int = -1):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None

        
class LRUCache:

    def __init__(self, capacity: int):
        """Doublely linked list + hashtable solution. Courtesy of

        https://leetcode.com/problems/lru-cache/discuss/45911/Java-Hashtable-%2B-Double-linked-list-(with-a-touch-of-pseudo-nodes)

        With doubly linked list, it is O(1) to move any node in the linked list
        to the head. Thus, when a key is mentioned/used, we simply grab its node
        and move it to the head. Thus, the node at the tail of the linked list
        is the least recently used key.

        I followed the discussion post to use a dummy head and dummy tail, which
        drastically simplifies the logic of adding and removing nodes, because
        it is guaranteed that there exists a head and tail in front or behind
        any node.

        """
        # head and tail are static.
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.post = self.tail
        self.tail.pre = self.head
        self.cache = {}
        self.cap = capacity
        self.count = 0

    def _remove(self, node: DoubleLinkedNode)-> None:
        pre = node.pre
        post = node.post
        pre.post = post
        post.pre = pre

    def _add(self, node:DoubleLinkedNode) -> None:
        post = self.head.post
        self.head.post = node
        node.pre = self.head
        node.post = post
        post.pre = node

    def _move_to_head(self, node: DoubleLinkedNode) -> None:
        self._remove(node)
        self._add(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = DoubleLinkedNode(key=key, value=value)
            self._add(self.cache[key])
            self.count += 1
            if self.count > self.cap:
                del self.cache[self.tail.pre.key]
                self._remove(self.tail.pre)
                self.count -= 1
        else:
            self.cache[key].value = value
            self._move_to_head(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
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
