# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """LeetCode 3

        This problem is very similar to 2262. We record the index of the last
        appearance of each letter, and the length of the longest unique
        substring ending at the position right in front of the current one.
        Then we check if the last appearance of the current letter is within or
        outside the unique substring ending at the previous letter. If it is
        outside, then the length of the unique string ending at the current
        letter is one more than that of the string ending at the letter before.
        However, if it is inside, then the current max length must be from the
        current index to the index of the last appearance.

        O(N), 56 ms, faster than 95.75%
        """
        pre_occ = defaultdict(lambda: -1)
        res, cur = 0, math.inf
        for i, le in enumerate(s):
            if i - cur > pre_occ[le]:
                cur += 1
            else:
                cur = i - pre_occ[le]
            res = max(res, cur)
            pre_occ[le] = i
        return res


sol = Solution()
tests = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("a", 1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.lengthOfLongestSubstring(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
