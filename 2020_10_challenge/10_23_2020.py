# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def find132pattern(self, nums: List[int]) -> bool:
        """9.7% ranking. This is O(N^2) in worst case.
        But it passed OJ.

        It finds all adjacent valley-peak pairs, and
        for each number, check whether any valley-peak
        pair fits the pattern. Since there are fewer
        than n pairs of valley-peak pairs, this algo
        runs faster than true O(N^2). Hence it passed
        OJ.
        """
        v, p = math.inf, -math.inf
        vps = set()  # valley and peaks
        prev = nums[0]
        for n in nums[1:]:
            if n < prev and p < -10**9:
                p = prev
            elif n > prev and v > 10**9:
                v = prev
                p = -math.inf  # reset p
            prev = n
            if v < p:
                vps.add((v, p))
                v, p = math.inf, -math.inf
            for v_, p_ in vps:
                if v_ < n < p_:
                    return True
        return False


class Solution2:
    def find132pattern(self, nums: List[int]) -> bool:
        """Simple O(N^2). However, this does not pass
        OJ, get TLE.
        """
        size = len(nums)
        for i in range(size):
            v, p = nums[i], nums[i]
            for j in range(i + 1, size):
                if nums[j] > p:
                    p = nums[j]
                elif v < nums[j] < p:
                    return True
        return False


class Solution3:
    def find132pattern(self, nums: List[int]) -> bool:
        """Had to read the solution to get the O(N) approach
        99% ranking.
        """
        vs = [nums[0]]  # valley corresponding to each num
        for n in nums[1:]:
            vs.append(n if n < vs[-1] else vs[-1])
        stack = []  # post-peak values
        for i in range(len(nums) - 1, -1, -1):
            # remove post-peak values that are smaller or eqaul to valleys
            while stack and stack[-1] <= vs[i]:
                stack.pop()
            # check potential post-peak value. If too big, we put the smaller
            # post-peak value (i.e. nums[i]) on top which might be useful
            # for a peak before the current one. If appropriate, we return True
            if not stack or stack[-1] >= nums[i]:
                stack.append(nums[i])
            else:
                return True
        return False


sol = Solution3()
tests = [
    ([-2, 1, -2], False),
    ([1, 2, 3, 4], False),
    ([3, 1, 4, 2], True),
    ([-1, 3, 2, 0], True),
    ([1, 0, 1, -4, -3], False),
    ([1, 0, 1, -4, -3, 1, 0], True),
    ([3, 5, 0, 3, 4], True),
    ([1, 0, -1, 3, 5, 2], True),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.find132pattern(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
