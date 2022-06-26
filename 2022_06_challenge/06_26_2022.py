# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """LeetCode 1423

        Wrap arpund cardPoints, then we are looking for the largest sum of
        subarray of length k.

        O(K), 639 ms, faster than 38.62%
        """
        res = s = sum(cardPoints[-k:])
        for i in range(-k + 1, 1):
            s += cardPoints[i + k - 1] - cardPoints[i - 1]
            res = max(res, s)
        return res


sol = Solution()
tests = [
    ([1,2,3,4,5,6,1], 3, 12),
    ([2,2,2], 2, 4),
    ([9,7,7,9,7,7,9], 7, 55),
    ([1], 1, 1),
    ([96,90,41,82,39,74,64,50,30], 8, 536),
]

for i, (cardPoints, k, ans) in enumerate(tests):
    res = sol.maxScore(cardPoints, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
