# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, defaultdict
import heapq


class Node:
    def __init__(self, val: int, freq: int, tick: int):
        self.val = val
        self.freq = freq
        self.tick = tick

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.tick > other.tick
        return self.freq > other.freq


class FreqStack:

    def __init__(self):
        """LeetCode 895

        Using an auxilary node, we take advantage of a heap to keep the node
        with the highest frequency on top of the heap. If the frequency is the
        same, the secondary comparison is on time tick (i.e. when the node is
        pushed to the heap).

        It's a very simple implementation. But it's not the fastest.

        O(logN) per operation. 818 ms, 5% ranking.
        """
        self.counter = Counter()
        self.heap = []
        self.tick = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.tick += 1
        heapq.heappush(self.heap, Node(val, self.counter[val], self.tick))

    def pop(self) -> int:
        node = heapq.heappop(self.heap)
        self.counter[node.val] -= 1
        return node.val


class FreqStack:

    def __init__(self):
        """I read the title of the solution, but did not read its
        implementation. Hence, this is my intepretation of stack of stack.

        This is O(1) per operation. 632 ms, 12% ranking.

        UPDATE: the solution recorded a year ago is better. No need to use a
        hashmap, and no need to keep track of the max frequency.

        296 ms, 95% ranking.
        """
        self.counter = Counter()
        self.stackstack = [[]]

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.counter[val] == len(self.stackstack):
            self.stackstack.append([])
        self.stackstack[self.counter[val]].append(val)

    def pop(self) -> int:
        val = self.stackstack[-1].pop()
        self.counter[val] -= 1
        if not self.stackstack[-1]:
            self.stackstack.pop()
        return val


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
