# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class MyCalendarThree:
    """LeetCode 732

    Remarkably, it passes on the first try. Really really convoluted and a lot
    of analysis. I do not like intervals.

    Will check the solution tomorrow. I am dead tired.

    1369 ms, faster than 76.31%
    """

    def __init__(self):
        self.map = {}
        self.k = 0

    def book(self, start: int, end: int) -> int:
        if not self.map:
            self.map[start] = 1
            self.map[end] = 0
            self.k = 1
            return 1
        sorted_start = sorted(map)
        i = bisect_right(sorted_start, start)
        if i == 0:
            self.map[start] = 1
            j = bisect_right(sorted_start, end)
            if j == 0:
                self.map[end] = 0
            else:
                for p in range(j - 1):
                    self.map[sorted_start[p]] += 1
                    self.k = max(self.k, self.map[sorted_start[p]])
                if j == len(sorted_start):
                    self.map[sorted_start[j - 1]] += 1
                    self.k = max(self.k, self.map[sorted_start[j - 1]])
                    self.map[end] = 0
                else:
                    lo, hi = sorted_start[j - 1], sorted_start[j]
                    if lo < end < hi:
                        if self.map[lo] == 0:
                            self.map[lo] = 1
                            self.map[end] = 0
                        else:
                            self.map[end] = self.map[lo]
                            self.map[lo] += 1
                            self.k = max(self.k, self.map[lo])
        elif i == len(sorted_start):
            self.map[start] = 1
            self.map[end] = 0
        else:
            lo, hi = sorted_start[i - 1], sorted_start[i]
            if end < hi:
                if start == lo:
                    if self.map[lo] == 0:
                        self.map[lo] = 1
                        self.map[end] = 0
                    else:
                        self.map[end] = self.map[lo]
                        self.map[lo] += 1
                        self.k = max(self.k, self.map[lo])
                else:
                    if self.map[lo] == 0:
                        self.map[start] = 1
                        self.map[end] = 0
                    else:
                        self.map[start] = self.map[lo] + 1
                        self.map[end] = self.map[lo]
                        self.k = max(self.k, self.map[start])
            else:
                if start == lo:
                    self.map[lo] += 1
                    self.k = max(self.k, self.map[lo])
                else:
                    self.map[start] = self.map[lo] + 1
                    self.k = max(self.k, self.map[start])
                j = bisect_right(sorted_start, end)
                for p in range(i, j - 1):
                    self.map[sorted_start[p]] += 1
                    self.k = max(self.k, self.map[sorted_start[p]])
                if j == len(sorted_start):
                    self.map[sorted_start[j - 1]] += 1
                    self.k = max(self.k, self.map[sorted_start[j - 1]])
                    self.map[end] = 0
                else:
                    lo, hi = sorted_start[j - 1], sorted_start[j]
                    if lo < end < hi:
                        if self.map[lo] == 0:
                            self.map[lo] = 1
                            self.map[end] = 0
                        else:
                            self.map[end] = self.map[lo]
                            self.map[lo] += 1
                            self.k = max(self.k, self.map[lo])
        return self.k


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
