# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right, bisect_left
from collections import Counter


class MyCalendarThree1:
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


class MyCalendarThree2:
    """This idea finally worked.

    The basic idea is that we sort all the previous intervals by their start
    value. Given the current start, we can use binary search to find where to
    insert it.

    The number of intervals that overlap with the current interval is equal to
    the number of previous intervals (after sort) with their starts smaller or
    equal to the current start AND their end larger than the current start.

    After computing this, we save the count of overlap for the current start in
    a hashmap.

    We proceed to process the previous intervals with start larger than
    the current start. Note that the previous intervals with start smaller or
    equal to the current start will not get any more overlaps. For those
    intervals with larger start, we only need to check whether their start is
    smaller than the current end. If it is, we can produce one more overlap for
    it. Another important thing to note is that for this to work, we must use
    unique starts to avoid double counting.

    1160 ms, faster than 75.86%
    Time complexity of book() is O(NlogN)
    """

    def __init__(self):
        self.data = []
        self.count = Counter()

    def book(self, start: int, end: int) -> int:
        self.data.sort()
        idx = bisect_right(self.data, start, key=lambda tup: tup[0])
        res = 1  # the current interval
        for i in range(idx):
            res += int(self.data[i][1] > start)
        self.count[start] = res
        # check all the starts that are larger than the current start
        for s in set(self.data[j][0] for j in range(idx, len(self.data))):
            self.count[s] += int(s < end)
        self.data.append((start, end))
        return max(self.count.values())

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
