# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """LeetCode 1423.

        We start from taking all k elements from the front. Then we swap out
        one from the front with one from the end. We do this until all k
        elements are from the end. We record the max sum along the way and
        return it as a result.

        O(k), 404 ms, 85% ranking.

        Another way to think is to find the min sum of a subarray using sliding
        window. The result will be the difference between the total sum and the
        min subarray sum. Reference:
        https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray
        """
        res = sum(cardPoints[:k])
        s = res
        i, j = k - 1, len(cardPoints) - 1
        while i >= 0:
            s = s - cardPoints[i] + cardPoints[j]
            res = max(res, s)
            i -= 1
            j -= 1
        return res


sol = Solution()
tests = [
    ([1, 2, 3, 4, 5, 6, 1], 3, 12),
    ([2, 2, 2], 2, 4),
    ([9, 7, 7, 9, 7, 7, 9], 7, 55),
    ([1, 1000, 1], 1, 1),
    ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202),
    ([1, 100, 1, 2, 3, 10, 90], 2, 101),
]

for i, (cardPoints, k, ans) in enumerate(tests):
    res = sol.maxScore(cardPoints, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
