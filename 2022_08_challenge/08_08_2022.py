# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """LeetCode 300
        
        Naive DP solution. O(N^2), 7226 ms, faster than 10.13%
        """
        N = len(nums)
        dp = [1] * N
        for i, n in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """My ability definitely dropped. I was able to figure out the O(NlogN)
        solution last time, but not this time. Mind you, I have solved this
        problem three time before. Yet the fourth try not does not seem to be
        any better than the previous ones.

        The key is to understand that we must use binary search, yet we do not
        have a sorted array at hand. Nor is it possible for us to sort any
        array along the way. Therefore, the only way to obtain a sorted array
        is to build one. As we build an sorted array, an important observation
        is that if we want the sorted array to be as small as possible, such
        that it is more likely that we can append more values. To make that
        happen, each time a new value is smaller than the some value in the
        array that it can replace without changing the structure of the array,
        we shall do it. For instance, given array = [2, 3, 5, 7] and that is
        the current longest increasing subsequence. If we encounter 1 now, we
        can replace 2 with 1. Does this change the fact that the length of the
        current LIS is four? No it doesn't. But what it does is that it lowers
        the barrier to create longer LIS in the future. Let's say we have
        values 2, 3, 4, 5 happening after 1. By replacing 2 with 1, we open the
        door to accepting 2, 3, 4, 5, and thus creating an even longer LIS.
        This won't happen if we do not do that swap.

        O(NlogN), 126 ms, faster than 83.43% 
        """
        aux = [nums[0]]
        for i in range(1, len(nums)):
            idx = bisect_right(aux, nums[i])
            if idx and aux[idx - 1] == nums[i]:
                continue
            if idx == len(aux):
                aux.append(nums[i])
            else:
                aux[idx] = nums[i]
        return len(aux)


sol = Solution2()
tests = [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.lengthOfLIS(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
