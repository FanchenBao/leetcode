# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """LeetCode 581

        This is the naive solution where we sort nums and find out the index of
        the subarray that mismatch between the sorted and the unsorted version.

        O(NlogN), 427 ms, faster than 9.05%
        """
        sorted_nums = sorted(nums)
        N = len(nums)
        for i in range(N):
            if sorted_nums[i] != nums[i]:
                break
        if i == N - 1:
            return 0
        j = N - 1
        while j > i:
            if sorted_nums[j] != nums[j]:
                break
            j -= 1
        return j - i + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Monotonic stack
        
        O(N), 310 ms, faster than 38.06%
        """
        N = len(nums)
        s = []
        lo = N
        for i in range(N):
            while s and nums[i] < s[-1][1]:
                lo = min(lo, s.pop()[0])
            s.append((i, nums[i]))
        if lo == N:
            return 0
        s = []
        hi = -1
        for j in range(N - 1, -1, -1):
            while s and nums[j] > s[-1][1]:
                hi = max(hi, s.pop()[0])
            s.append((j, nums[j]))
        return hi - lo + 1


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """Similar to monotonic stack but without the need to push and
        pop operation.

        We go left to right, looking for the element that is smaller than
        the max on the left overall. This element must be wrongly placed. We
        record its index. Eventually, we will obtain the index of the right
        most element that is wrongly placed.

        Similarly, we go right to left, looking for the element that is larger
        than the min on the right overall. This is the first element that is
        wrongly placed.

        This method came from my previous attempt on this problem on 2021-02-25

        226 ms, faster than 79.45%
        """
        N = len(nums)
        hi, cur_max = -1, -math.inf
        for i in range(N):
            if nums[i] < cur_max:
                hi = i
            else:
                cur_max = nums[i]
        if hi == -1:
            return 0
        lo, cur_min = 0, math.inf
        for j in range(N - 1, -1, -1):
            if nums[j] > cur_min:
                lo = j
            else:
                cur_min = nums[j]
        return hi - lo + 1


sol = Solution3()
tests = [
    ([2,6,4,8,10,9,15], 5),
    ([1,2,3,4], 0),
    ([1], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findUnsortedSubarray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
