# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """This is O(N^2), not the O(N) alluded in the question, and definitely
        not the O(1) hinted. But this is the best I can get at the moment. The
        idea is to continuously produce gcd for each adjacent pair, until a
        gcd of 1 shows up.

        62 ms, faster than 37.77%
        """
        num_ones = nums.count(1)
        if num_ones > 0:
            return len(nums) - num_ones
        queue = nums
        steps = 0
        while queue:
            tmp = []
            for i in range(len(queue) - 1):
                tmp.append(math.gcd(queue[i], queue[i + 1]))
                if tmp[-1] == 1:
                    return steps + len(nums)
            queue = tmp
            steps += 1
        return -1
        

sol = Solution()
tests = [
    ([2,6,3,4], 4),
    ([2,10,6,14], -1),
    ([1,1], 0),
    ([6,10,15], 4),
    ([10,5,10,30,70,4,2,6,8,4], 13),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minOperations(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
