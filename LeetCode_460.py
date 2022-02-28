# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import defaultdict


class Node(object):
    def __init__(self, key: int, val: int, tick: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.tick = tick

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.tick < other.tick
        return self.freq < other.freq


class LFUCache:
    """TLE. Since the capacity can grow to 10^4, O(logN) for get() and put()
    becomes too costly.
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.heap = []
        self.tick = 0

    def get(self, key: int) -> int:
        self.tick += 1
        if key not in self.cache:
            return -1
        self.cache[key].freq += 1
        self.cache[key].tick = self.tick
        heapq.heapify(self.heap)
        return self.cache[key].val        

    def put(self, key: int, value: int) -> None:
        self.tick += 1
        if self.cap == 0:
            return
        if key in self.cache:
            self.cache[key].val = value
            self.cache[key].freq += 1
            self.cache[key].tick = self.tick
            heapq.heapify(self.heap)
        else:
            if len(self.heap) == self.cap:
                node_to_rm = heapq.heappop(self.heap)
                del self.cache[node_to_rm.key]
            node = Node(key=key, val=value, tick=self.tick)
            heapq.heappush(self.heap, node)
            self.cache[key] = node


class DLNode(object):
    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        self.freq = 1


class DoubleLinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, node: DLNode) -> None:
        self.tail.pre.next = node
        node.pre = self.tail.pre
        self.tail.pre = node
        node.next = self.tail
        self.length += 1

    def remove(self, node: DLNode) -> None:
        assert self.length > 0
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = node.next = None
        self.length -= 1


class LFUCache:
    """The key for this solution is to creat a frequency hashmap, where
    freqmap[f] is a doubly-linked list that contains nodes of frequency f. The
    doubly-linked list is used to handle the LRU cache when the frequency is
    the same. freqmap is used to obtain the smallest frequency by finding the
    min of its keys. As long as the operation is not designed to create a long
    list of distinct frequencies, it is not likely that there are a lot of
    keys in freqmap. get() is always O(1), put() is O(N) depending on the
    different frequencies currently present.

    1095 ms, 66% ranking.

    UPDATE:

    https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list

    This solution uses a very smart way to maintain minimum frequency in O(1).
    The trick is to realize that when a new node is added, minfreq is always
    set to 1. When a node is popped from a frequency, if there are still nodes
    left, we don't have to change minfreq. If there are no node left in that
    frequency and it is not the same as minfreq, we don't have to change
    minfreq. If it is the same as minfreq, it is guaranteed that this type of
    popping will result in the popped node to be inserted into the linked list
    marked with frequency plus 1, so we simply update minfreq to plus one.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.cache = {}
        self.freqmap = {}
        self.minfreq = 0

    def get(self, key: int) -> int:
        """O(1)
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.freqmap[node.freq].remove(node)
        if self.freqmap[node.freq].length == 0:
            del self.freqmap[node.freq]
            if node.freq == self.minfreq:
                self.minfreq += 1
        node.freq += 1
        if node.freq not in self.freqmap:
            self.freqmap[node.freq] = DoubleLinkedList()
        self.freqmap[node.freq].add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """O(1)
        """
        if self.cap == 0:
            return 
        if self.get(key) < 0:
            if self.length == self.cap:
                node_to_rm = self.freqmap[self.minfreq].head.next
                self.freqmap[self.minfreq].remove(node_to_rm)
                if self.freqmap[self.minfreq].length == 0:
                    del self.freqmap[self.minfreq]
                del self.cache[node_to_rm.key]
                self.length -= 1
            node = DLNode(key=key, val=value)
            if 1 not in self.freqmap:
                self.freqmap[1] = DoubleLinkedList()
            self.freqmap[1].add(node)
            self.cache[key] = node
            self.length += 1
            self.minfreq = 1
        else:
            self.cache[key].val = value
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
