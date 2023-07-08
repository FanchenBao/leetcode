# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """LeetCode 2024

        Two rounds of sliding window.

        O(N), 609 ms, faster than 12.80%
        """

        def slide(tgt: str) -> int:
            i = res = cnt = 0
            for j in range(len(answerKey)):
                cnt += int(answerKey[j] == tgt)
                while cnt > k:
                    cnt -= int(answerKey[i] == tgt)
                    i += 1
                # we can swap as long as the count is not bigger than k
                res = max(res, j - i + 1)
            return res

        return max(slide('F'), slide('T'))


class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """One round of sliding window. All we need to do is to shrink the
        window when the smaller of the T or F count is larger than k.

        O(N), 457 ms, faster than 47.86%
        """
        i = res = 0
        cnt = {'T': 0, 'F': 0}
        for j in range(len(answerKey)):
            cnt[answerKey[j]] += 1
            while min(cnt.values()) > k:
                cnt[answerKey[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
        

sol = Solution2()
tests = [
    ("TTFF", 2, 4),
    ("TFFT", 1, 3),
    ("TTFTTFTT", 1, 5),
    ("TF", 2, 2),
]

for i, (answerKey, k, ans) in enumerate(tests):
    res = sol.maxConsecutiveAnswers(answerKey, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
