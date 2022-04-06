# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """LeetCode 11

        I still remember how this problem is solved. Two pointers from both
        ends. Which ever points to the lower height determines the amount of
        water that can be held. Keep moving the pointers towards the center
        when the height being pointed is smaller than the other.

        O(N), 931 ms, 54% ranking.
        """
        lo, hi = 0, len(height) - 1
        res = 0
        while lo < hi:
            res = max(res, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
        return res


sol = Solution()
tests = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1, 1], 1),
]

for i, (height, ans) in enumerate(tests):
    res = sol.maxArea(height)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
