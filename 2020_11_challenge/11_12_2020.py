# from pudb import set_trace; set_trace()
from typing import List
import collections


class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """26% ranking

        This is an old question. I must have done this before, but I don't
        remember. The solution below is naive. It lists all permutations first
        and then trim out the duplication.
        """

        def permute(idx: int):
            if idx == len(nums) - 1:
                return [[nums[idx]]]
            res = []
            for perm in permute(idx + 1):
                for i in range(len(perm) + 1):
                    res.append(perm[:i] + [nums[idx]] + perm[i:])
            return res

        return [list(q) for q in set(tuple(p) for p in permute(0))]


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """86% ranking

        This method performs duplication elimination at each recursion step.
        Since each recursion call result is a unique set of permutation, the
        work needed to remove duplicates is much reduced compared to the first
        solution.
        """

        def permute(idx: int):
            if idx == len(nums) - 1:
                return {(nums[idx],)}
            res = set()
            for perm in permute(idx + 1):
                for i in range(len(perm) + 1):
                    res.add(tuple(perm[:i] + (nums[idx],) + perm[i:]))
            return res

        return [list(p) for p in permute(0)]


class Solution3:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """70% ranking.

        This is the standard solution using backtracking and avoiding duplicates
        at each addition.
        """
        counter = collections.Counter(nums)
        res = []

        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
            else:
                for n in counter.keys():
                    if counter[n]:
                        comb.append(n)
                        counter[n] -= 1
                        backtrack(comb)
                        comb.pop()
                        counter[n] += 1

        backtrack([])
        return res


# sol = Solution()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
