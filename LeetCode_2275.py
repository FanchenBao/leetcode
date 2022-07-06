# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        Just to count the max occurrences of '1' at each bit in the binary
        version of all numbers

        O(24N), 2397 ms, faster than 56.97%
        """
        sums = [0] * 24
        for cand in candidates:
            for i, b in enumerate(format(cand, '024b')):
                sums[i] += b == '1'
        return max(sums)


sol = Solution()
tests = [
    ([16,17,71,62,12,24,14], 4),
    ([8,8], 2)
]

for i, (candidates, ans) in enumerate(tests):
    res = sol.largestCombination(candidates)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
