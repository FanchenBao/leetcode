# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """LeetCode 915

        The idea is to iterate through nums, and check the current n against
        the max value so far. If n < cur_max, then the left partition must start
        after n. If n >= cur_max, then the left partition MIGHT end right before
        n, yet we don't know that for sure yet. We keep track of the index of
        such n as a potential solution to the problem. Furthermore, we must
        track the next potential max. This is because if we encounter
        n1 >= cur_max and after that we encounter n2 < cur_max, then we must
        update cur_max with n1. In the algo we call such n1 as pot_max
        (potential max). We iterate through the entire array and the solution is
        the final recorded index.

        O(N), 176 ms, 92 % ranking.
        """
        cur_max, pot_max, idx = nums[0], nums[0], -1
        for i in range(1, len(nums)):
            if nums[i] < cur_max:
                idx = -1
                cur_max = pot_max
            else:
                if idx < 0:
                    idx = i
                if nums[i] > pot_max:
                    pot_max = nums[i]
        return idx


class Solution2:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """From https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/1354396/Python-From-O(N)-space-to-O(1)-space-Picture-explained-Clean-and-Concise

        Same idea as Solution1, but since the partition is tracked as the last
        element of the left array, the algo is simplified.
        """
        cur_max, glob_max, part = nums[0], nums[0], 0
        for i in range(1, len(nums)):
            glob_max = max(glob_max, nums[i])
            if nums[i] < cur_max:
                part = i
                cur_max = glob_max
        return part + 1


sol = Solution2()
tests = [
    ([5, 0, 3, 8, 6], 3),
    ([1, 1, 1, 0, 6, 12], 4),
    ([0, 0, 3, 8, 6], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.partitionDisjoint(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
