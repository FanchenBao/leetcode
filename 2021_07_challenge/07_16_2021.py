# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """The basics is still 3Sum, the same that we learned from yesterday's
        challenge. The idea is to isolate the first value (sort nums first of
        course), and we run 3Sum for the remaining values. The trick is to skip
        all the repeated values once we have recorded one version of the repeats.
        This allows us to only save unique quadruplets without having to use
        a hash function.

        O(N^3), 1032 ms, 42% ranking.

        UPDATE: with additional pre-checking, we shrink the runtime down to
        396 ms, 64% ranking.
        """
        nums.sort()
        n, res = len(nums), []
        if n < 4 or nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip repeats
            for j in range(n - 1, i + 2, -1):
                if j < n - 1 and nums[j] == nums[j + 1]:
                    continue  # skip repeats
                two_sum = target - nums[i] - nums[j]
                lo, hi = i + 1, j - 1
                while lo < hi:
                    if nums[lo] + nums[hi] == two_sum:
                        res.append([nums[i], nums[lo], nums[hi], nums[j]])
                        lo += 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1  # skip repeats
                        hi -= 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1  # skip repeats
                    elif nums[lo] + nums[hi] > two_sum:
                        hi -= 1
                    else:
                        lo += 1
        return res


class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Another implementation. But pretty bad.

        1392 ms
        """
        nums.sort()
        n, res, counter = len(nums), [], Counter(nums)
        if n < 4 or nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip repeats
            for j in range(n - 1, i + 2, -1):
                if j < n - 1 and nums[j] == nums[j + 1]:
                    continue  # skip repeats
                for k in range(i + 1, j - 1):
                    if k > i + 1 and nums[k] == nums[k - 1]:
                        continue  # skip repeats
                    v = target - nums[i] - nums[j] - nums[k]
                    if nums[k] <= v <= nums[j]:
                        c = sum([1, nums[k] == v, nums[j] == v, nums[i] == v])
                        if c <= counter[v]:
                            res.append([nums[i], nums[k], v, nums[j]])
        return res


class Solution3:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """The generic version from the official solution.
        https://leetcode.com/problems/4sum/solution/

        The generic version is very fast. 92 ms, 89% ranking.
        """
        n = len(nums)
        nums.sort()

        def ksum(idx: int, tgt: int, k: int) -> List[List[int]]:
            res, size = [], n - idx
            if size < k or nums[idx] * k > tgt or nums[-1] * k < tgt:
                return []
            if k == 2:
                lo, hi = idx, n - 1
                while lo < hi:
                    s = nums[lo] + nums[hi]
                    if s < tgt or (lo > idx and nums[lo] == nums[lo - 1]):
                        lo += 1
                    elif s > tgt or (hi < n - 1 and nums[hi] == nums[hi + 1]):
                        hi -= 1
                    elif s == tgt:
                        res.append([nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                return res
            for i in range(idx, n - k + 1):
                if i > idx and nums[i] == nums[i - 1]:
                    continue  # skip repeats
                for lst in ksum(i + 1, tgt - nums[i], k - 1):
                    res.append([nums[i]] + lst)
            return res

        return ksum(0, target, 4)


sol = Solution3()
tests = [
    ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ([2, 2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ([-3, -1, 0, 2, 4, 5], 0, [[-3, -1, 0, 4]]),
    ([-3, -2, -1, 0, 0, 1, 2, 3], 0, [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.fourSum(nums, target)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
