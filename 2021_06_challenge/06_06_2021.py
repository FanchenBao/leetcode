# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        """LeetCode 128

        The idea is to start from any n in numns, and iterate upward and
        downward, and check whether any of the upward or downward values are in
        orginal nums. If it is, that means we have a consecutive sequence going
        that direction. After checking on both directions, we pool the number
        of values in each direction together to achieve the longest consecutive
        sequence that contains the current n. Also, along the way, we remove
        all the n that have been considered. This way, we shrink the search size
        and ensure that each n is visited at most twice.

        O(N), 184 ms, 39% ranking.
        """
        not_seen = set(nums)
        res = 0
        for n in nums:
            if n not in not_seen:
                continue
            x = n  # go lower
            while x in not_seen:
                not_seen.remove(x)
                x -= 1
            y = n + 1  # go higher
            while y in not_seen:
                not_seen.remove(y)
                y += 1
            res = max(res, n - x + y - n - 1)
        return res


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        """O(Nlog(N)) solution. This is against the requirement, but we do it
        just for the lolz

        180 ms.
        """
        if not nums:
            return 0
        nums.sort()
        res, cur_l = 0, 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                cur_l += 1
            elif nums[i + 1] - nums[i] > 1:
                res = max(res, cur_l)
                cur_l = 1
        res = max(res, cur_l)
        return res


sol = Solution2()
tests = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),
    ([1], 1),
    ([1, 1, 1, 1, 1], 1),
    ([1, 2, 2, 3, 3, 4], 4),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.longestConsecutive(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
