# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def arrayNesting(self, nums: List[int]) -> int:
        """LeetCode 565

        The key insight is that once a set is found, it does not change. This
        means no other number can enter this set. Therefore, we can easily find
        all such sets in nums without having to repeatedly check every number.
        Once a number has been checked, we don't have to check it again. As we
        go through nums and figure out each set, we also keep track of the max
        size of the set. Eventually we can return the max size.

        O(N) time complexity because each value is visited at most twice.
        O(N) space due to the auxilary array "sets"
        143 ms, 29% ranking.
        """
        sets = [0] * len(nums)
        res = 0
        for n in nums:
            if not sets[n]:
                sets[n] = 1
                idx, temp = n, 1
                while not sets[nums[idx]]:
                    sets[nums[idx]] = 1
                    idx = nums[idx]
                    temp += 1
                res = max(res, temp)
        return res


class Solution2:
    def arrayNesting(self, nums: List[int]) -> int:
        """Same idea as Solution1 but O(1) extra space

        108 ms, 92% ranking.
        """
        res = 0
        for i, n in enumerate(nums):
            idx, size = i, 0
            while nums[idx] != -1:
                size += 1
                # This syntax requires a, b = c, a
                # This is to say the left left variable must be the same as the
                # right right variable, because Python creates an intermediate
                # value for the left left.
                nums[idx], idx = -1, nums[idx]
            res = max(res, size)
        return res


sol = Solution2()
tests = [
    ([5, 4, 0, 3, 1, 6, 2], 4),
    ([0, 1, 2], 1),
    ([0, 2, 1, 4, 3], 2)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.arrayNesting(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
