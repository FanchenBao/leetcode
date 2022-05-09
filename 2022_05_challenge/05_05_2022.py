# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class MyStack:

    def __init__(self):
        """LeetCode 225

        O(1) pop, O(N) push. 28 ms, faster than 95.09%
        """
        self.q = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.temp.append(x)
        while self.q:
            self.temp.append(self.q.popleft())
        self.q, self.temp = self.temp, self.q
        
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


class MyStack:

    def __init__(self):
        """LeetCode 225

        O(1) pop, O(N) push. Use only one queue
        """
        self.q = deque()

    def push(self, x: int) -> None:
        size = len(self.q)
        self.q.append(x)
        for _ in range(size):
            self.q.append(self.q.popleft())
        
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

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
