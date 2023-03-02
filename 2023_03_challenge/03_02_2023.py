# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def compress(self, chars: List[str]) -> int:
        """LeetCode 443

        Not particularly hard, but there is one condition that I initially
        forgot to consider, which is when we iterate through chars, we have to
        check the count again to decide whether we need to compress the last
        series of repeated chars.

        O(N), 58 ms, faster than 83.76%
        """
        i, j, c = 0, 1, 1
        while j < len(chars):
            if chars[j] == chars[j - 1]:
                c += 1
            else:
                chars[i] = chars[j - 1]
                if c > 1:
                    for d in str(c):
                        i += 1
                        chars[i] = d
                i += 1
                c = 1
            j += 1
        chars[i] = chars[j - 1]
        if c > 1:
            for d in str(c):
                i += 1
                chars[i] = d
        i += 1
        return i


sol = Solution()
tests = [
    (['a','b'], 2),
    (["a","a","b","b","c","c","c"], 6),
    (["a"], 1),
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4),
]

for i, (chars, ans) in enumerate(tests):
    res = sol.compress(chars)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
