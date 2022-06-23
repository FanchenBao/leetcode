# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
from collections import defaultdict
import heapq


class Solution1:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """MLE"""
        sc = [c for c in courses if c[0] <= c[1]]
        sc.sort(key=lambda tup: tup[1])
        N = len(sc)

        @lru_cache(maxsize=None)
        def helper(curTime: int, idx: int) -> int:
            if idx == N:
                return 0
            if curTime + sc[idx][0] > sc[idx][1]:
                return helper(curTime, idx + 1)
            return max(1 + helper(curTime + sc[idx][0], idx + 1), helper(curTime, idx + 1))

        return helper(0, 0)


class Solution2:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """LeetCode 630

        I wasn't able to solve it. There are two pieces of very important
        insight.

        1. Courses with smaller end day must be taken before those with larger
        end day, because of a exhaustive analysis on different sitautions of
        two courses. The solution gives a very good demonstration of that.
        2. Once we sort courses based on the end day, we must take classes in
        that order as much as we can. Whenever we encounter a situation where
        the cur_time exceeds the current end day, that means we either have
        taken a class before with too much duration, or the current class has
        too much duration. To identify which scenario it is, we use priority
        queue to record the duration of all taken classes. We pop out the
        largest one and compare it to the current class. If the current class
        has less duration, swapping guarantees to be legal (because the total
        time decreases in this case), and we reudce the total time, which means
        we are able to take on more classes. If the current class has more
        duration, then we skip it.

        Following this greedy approach, we have the following implementation.

        O(NlogN), 936 ms, faster than 54.69%
        """
        sc = sorted(
            [tuple(c) for c in courses if c[0] <= c[1]],
            key=lambda tup: tup[1],
        )
        if not sc:
            return 0
        N = len(sc)
        heap = [-sc[0][0]]
        cur_time = sc[0][0]
        for i in range(1, N):
            if cur_time + sc[i][0] <= sc[i][1]:
                heapq.heappush(heap, -sc[i][0])
                cur_time += sc[i][0]
            elif -heap[0] > sc[i][0]:
                heapq.heappush(heap, - sc[i][0])
                cur_time = cur_time + heapq.heappop(heap) + sc[i][0]
        return len(heap)



sol = Solution2()
tests = [
    ([[100,200],[200,1300],[1000,1250],[2000,3200]], 3),
    ([[1,2]], 1),
    ([[3,2],[4,3]], 0),
    ([[100,2],[32,50]], 1),
    ([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]], 5),
]

for i, (courses, ans) in enumerate(tests):
    res = sol.scheduleCourse(courses)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
