# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int, idx: int = 0) -> List[List[int]]:
        """72% ranking. A middle-tier solution. Very naive recursion. It works,
        I think, because the restrictions on the input data: candidates is not
        too big.
        """
        if target < 0:
            return []
        elif target == 0:
            return [[]]
        res = []
        for i in range(idx, len(candidates)):
            partial = self.combinationSum(candidates, target - candidates[i], i)
            if partial:
                res += [[candidates[i], *p] for p in partial]
        return res


sol = Solution()
tests = [
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ([2], 1, []),
    ([1], 1, [[1]]),
    ([1], 2, [[1, 1]]),
]

for i, (candidates, target, ans) in enumerate(tests):
    res = sol.combinationSum(candidates, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
