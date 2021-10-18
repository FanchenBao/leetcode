# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """LeetCode 985

        This is not a medium question. It's a hard easy.

        There are four situations to evaluate.
            1. nums[idx] is even, delta is even => simply add delta
            2. nums[idx] is even, delta is odd => remove nums[idx] because this
            value will turn into odd
            3. nums[idx] is odd, delta is odd => add nums[idx] + delta because
            we have created a new even number
            4. nums[idx] is odd, delta is even => ignore, no change to sum

        O(N + M), where N is the length of nums and M is the length of queries.
        508 ms, 81% ranking.
        """
        s = sum(n for n in nums if n % 2 == 0)
        res = []
        for delta, idx in queries:
            if nums[idx] % 2 == 0 and delta % 2 == 0:
                s += delta
            elif nums[idx] % 2 == 0 and delta % 2:
                s -= nums[idx]
            elif nums[idx] % 2 and delta % 2:
                s += (nums[idx] + delta)
            res.append(s)
            nums[idx] += delta
        return res


class Solution2:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """This is the official solution, much clearner in logic.

        https://leetcode.com/problems/sum-of-even-numbers-after-queries/solution/
        """
        s = sum(n for n in nums if n % 2 == 0)
        res = []
        for delta, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += delta
            if nums[idx] % 2 == 0:
                s += nums[idx]
            res.append(s)
        return res


sol = Solution2()
tests = [
    ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
    ([1], [[4, 0]], [0]),
]

for i, (nums, queries, ans) in enumerate(tests):
    res = sol.sumEvenAfterQueries(nums, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
