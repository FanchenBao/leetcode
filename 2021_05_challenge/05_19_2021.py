# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution1:
    def minMoves2(self, nums: List[int]) -> int:
        """LeetCode 462

        It's a greedy solution. We sort the numbers, and we want the final
        converging value to be in the center of nums. Given two values a and b,
        it is always better to converge to c such that a <= c <= b
        This is because any c will lead to the number of moves being b - a. If
        we converge to a value outside, such as d > b or d < a, then the number
        of moves will be b - a + |d - a| + |d - b|, which is always larger than
        b - a. Therefore, for any pair of numbers, the best strategy is to
        converge to somewhere in between them.

        Considering the entire nums list, the best strategy would be to converge
        to a value in the middle of the list. If there are even number of
        elements in nums, the converging value doesn't matter, just somewhere
        in between the center pair. If there are odd number of elements, the
        converging value would be the median. However, neither of these cases
        matter in terms of the total number of moves, which will be the sum of
        all the differences from the end and start of nums.

        O(NlogN), 76 ms, 50% ranking.
        """
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1
        while l < r:
            res += nums[r] - nums[l]
            l += 1
            r -= 1
        return res


class Solution2:
    def minMoves2(self, nums: List[int]) -> int:
        """This is Mr. Pochmann's two liners. The use of ~i needs to be learned

        https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways
        """
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))


sol = Solution2()
tests = [
    ([1, 2, 3], 2),
    ([1, 10, 2, 9], 16)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minMoves2(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
