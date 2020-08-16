# from pudb import set_trace; set_trace()
from typing import List, Set, Tuple
from copy import deepcopy
import math


class Solution1:
    def __init__(self):
        self.res = math.inf

    def has_overlap(self, interval1: Tuple, interval2: Tuple) -> bool:
        l1, h1 = interval1
        l2, h2 = interval2
        return not (h1 <= l2 or h2 <= l1)

    def recursion(self, intervals: List[List[int]], no_overlap: Set[Tuple[int]], num_remove: int):
        if not intervals:
            self.res = min(self.res, num_remove)
        else:
            cur_interval = tuple(intervals.pop())
            no_overlap_copy = deepcopy(no_overlap)
            num_remove_copy = num_remove
            for interval in no_overlap:
                if self.has_overlap(interval, cur_interval):
                    no_overlap_copy.remove(interval)
                    num_remove_copy += 1
            if num_remove_copy > num_remove:
                no_overlap_copy.add(cur_interval)
                self.recursion(intervals[:], no_overlap_copy, num_remove_copy)
                self.recursion(intervals[:], no_overlap, num_remove + 1)
            else:
                no_overlap.add(cur_interval)
                self.recursion(intervals, no_overlap, num_remove)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Timed out"""
        self.res = math.inf
        self.recursion(intervals, set(), 0)
        return self.res


class Solution2:
    """Passed OJ, but very poor performance (196 ms)"""
    def has_overlap(self, interval1: Tuple, interval2: Tuple) -> bool:
        l1, h1 = interval1
        l2, h2 = interval2
        return not (h1 <= l2 or h2 <= l1)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """This is the best DP solution I can muster. It first removes all
        the duplicates and turn intervals from list to tuple for hashing
        purpose. Then we sort the intervals based on the start time. Following
        that, we compute the max number of intervals each interval can
        have from itself till the end. Here we have a little trick to further
        speed things up: each cached interval contains the max number of
        intervals of itself and its next overlapped interval. This way, we can
        guarantee that the first non-overlapping interval encountered contains
        the max number of intervals for all the intervals that remain.

        This algo runs in O(n^2) time.
        """
        no_dup_intervals = list(set(tuple(inter) for inter in intervals))
        no_dup_intervals.sort(key=lambda inter: inter[0])
        length = len(no_dup_intervals)
        cache = {}
        # DP
        for i in range(length - 1, -1, -1):
            addition = 0
            for j in range(i + 1, length):
                if not self.has_overlap(no_dup_intervals[i], no_dup_intervals[j]):
                    addition = cache[no_dup_intervals[j]]
                    break
            cache[no_dup_intervals[i]] = 1 + addition
            if i < length - 1:
                cache[no_dup_intervals[i]] = max(
                    cache[no_dup_intervals[i]], cache[no_dup_intervals[i + 1]],
                )
        return len(intervals) - max(cache.values()) if cache else len(intervals)


class Solution3:
    """Greedy"""
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Greedy solution. The left most interval must has the least end time
        in order to allow max capacity for the remaining intervals. Therefore,
        we choose only the non-overlapping intervals that have the least end
        time.

        Run in O(nlog(n)) time 
        """
        remove = 0
        pre_end = -math.inf
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start < pre_end:
                remove += 1
            else:
                pre_end = end
        return remove


        

sol = Solution3()
tests = [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0)
]

for i, (test, ans) in enumerate(tests):
    res = sol.eraseOverlapIntervals(test)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}: FAIL. Expected: {ans}, Received: {res}')

        