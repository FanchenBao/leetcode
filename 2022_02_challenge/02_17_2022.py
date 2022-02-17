# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """LeetCode 39

        What a coincidence! I was kinda struggling with 518 last night, and
        this problem is almost the same as 518. I use the same method and this
        one has a good result. The idea is to exhaust each element by taking 0,
        1, 2, ... number of such element away, and then moving on to the next
        element. We can cache the result with the state set to the index of
        the candidate and the remaining target value.

        108 ms, 53% ranking.
        """
        res = []
        N = len(candidates)

        @lru_cache(None)
        def dp(idx: int, tgt: int) -> List[List[int]]:
            if tgt == 0:
                return [[]]
            if idx < N:
                res = []
                i = 0
                while tgt - candidates[idx] * i >= 0:
                    for r in dp(idx + 1, tgt - candidates[idx] * i):
                        res.append([candidates[idx]] * i + r)
                    i += 1
                return res
            return []

        return dp(0, target)


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Inspired by 518. Again, we don't have to remove candidates[idx] one
        by one. We just need to call dp(idx, tgt - candidates[idx]) to grab
        all possible repeats of candidates[idx] for a smaller target value.

        O(MNK), M = target, N = len(candidates), K is the overhead of array
        cancatenation

        100 ms, 60% ranking.
        """
        res = []
        N = len(candidates)

        @lru_cache(None)
        def dp(idx: int, tgt: int) -> List[List[int]]:
            if tgt == 0:
                return [[]]
            if tgt < 0 or idx >= N:
                return []
            return dp(idx + 1, tgt) + [[candidates[idx]] + r for r in dp(idx, tgt - candidates[idx])]

        return dp(0, target)


sol = Solution2()
tests = [
    ([2,3,6,7], 7, [[2,2,3],[7]]),
    ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ([2], 3, []),
    ([3,5,8], 11, [[3,3,5],[3,8]]),
]

for i, (candidates, target, ans) in enumerate(tests):
    res = sol.combinationSum(candidates, target)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
