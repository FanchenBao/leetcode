# from pudb import set_trace; set_trace()
from typing import List
import heapq


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

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.heap = []
        self.tick = 0

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        self.tick += 1
        if len(self.heap) < self.cap:
            node = Node(key=key, val=value, tick=self.tick)

        

sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
