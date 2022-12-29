# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """LeetCode 1834

        Sort tasks by enqueue time, and use a heap to prioritize smallest
        processing time.

        The tricky part is that the current tick might be smaller than the next
        enqueue time. If this happens, we simply progressing the tick to that
        next enqueue time.

        O(NlogN), 1951 ms, faster than 94.92%
        """
        sorted_tasks = sorted([(t, i, p) for i, (t, p) in enumerate(tasks)], reverse=True)
        tick = 0
        res = []
        heap = []
        while sorted_tasks or heap:
            while sorted_tasks and tick >= sorted_tasks[-1][0]:
                _, i, p = sorted_tasks.pop()
                heapq.heappush(heap, (p, i))
            if heap:
                p, i = heapq.heappop(heap)
                res.append(i)
                tick += p
            else:
                tick = sorted_tasks[-1][0]  # the next task doesn't start until later
        return res


sol = Solution()
tests = [
    ([[1,2],[2,4],[3,2],[4,1]], [0,2,3,1]),
    ([[7,10],[7,12],[7,5],[7,4],[7,2]], [4,3,2,0,1]),
    ([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]], [5,0,1,3,2,4]),
]

for i, (tasks, ans) in enumerate(tests):
    res = sol.getOrder(tasks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
