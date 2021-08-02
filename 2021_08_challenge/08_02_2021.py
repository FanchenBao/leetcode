# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """LeetCode 1

        I don't understand why I have to use such a convoluted method. It feels
        like there got to be an easier solution.

        About O(N), 68 ms, 53% ranking.
        """
        val_idx = defaultdict(list)
        for i, n in enumerate(nums):
            val_idx[n].append(i)
        for i, n in enumerate(nums):
            if target - n in val_idx:
                for j in val_idx[target - n]:
                    if j != i:
                        return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """One pass

        56 ms, 89% ranking.
        """
        val_idx = {}
        for i, n in enumerate(nums):
            if target - n in val_idx:
                return [val_idx[target - n], i]
            val_idx[n] = i


sol = Solution2()
tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.twoSum(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
