# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedList
import heapq


class Solution1:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        Take advantage of SortedList and the problem become very doable.

        O(NlogN), 948 ms, faster than 89.47%
        """
        sorted_prefix = SortedList()
        N = len(nums)
        res = 10**9 + 7
        for i in range(x, N):
            sorted_prefix.add(nums[i - x])
            idx = sorted_prefix.bisect_right(nums[i])
            if idx > 0:
                res = min(res, nums[i] - sorted_prefix[idx - 1])
            if idx < len(sorted_prefix):
                res = min(res, sorted_prefix[idx] - nums[i])
        return res


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        This solution is inspired by https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/discuss/4007263/Python3-2-heaps-intuitive-answer

        It sorts nums first and then use a min heap and a max heap to ensure
        that we always compare the current number with the one that has the
        max distance to it. And since the numbers are sorted, each time we
        encounter a number that is eligible, we must record its difference,
        because that must create the minimal difference due to the sorted
        nature.

        O(NlogN) 1310 ms, faster than 19.71%
        """
        if x == 0:
            return 0
        sorted_nums = sorted([n, i] for i, n in enumerate(nums))
        min_heap: List[List[int]] = []
        max_heap: List[List[int]] = []
        res = 10**9 + 7
        for n, i in sorted_nums:
            while min_heap and abs(min_heap[0][0] - i) >= x:
                res = min(res, abs(n - heapq.heappop(min_heap)[1]))
            while max_heap and abs(-max_heap[0][0] - i) >= x:
                res = min(res, abs(n - heapq.heappop(max_heap)[1]))
            heapq.heappush(min_heap, [i, n])
            heapq.heappush(max_heap, [-i, n])
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
