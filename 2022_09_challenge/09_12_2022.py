# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """LeetCode 948

        Greedy. Always deduct power from the smallest token. If that is not
        possible and there is score left, add the largest token to have the
        best chance of further acquiring points.

        One thing to note is that whenever there is no way to earn any point
        and the current score remains zero, we cannot progress, because with
        zero score, we cannot add more power.

        O(N), 51 ms, faster than 98.58%
        """
        tokens.sort()
        res, score = 0, 0
        i, j = 0, len(tokens) - 1
        while i <= j:
            while i <= j and power >= tokens[i]:
                score += 1
                power -= tokens[i]
                i += 1
            if not score:  # we cannot play any token to get at least one score
                break
            res = max(res, score)
            power += tokens[j]
            j -= 1
            score -= 1
        return res


sol = Solution()
tests = [
    ([100], 50, 0),
    ([100,200], 150, 1),
    ([100,200,300,400], 200, 2),
    ([71,55,82], 54, 0),
    ([26], 51, 1),
]

for i, (tokens, power, ans) in enumerate(tests):
    res = sol.bagOfTokensScore(tokens, power)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
