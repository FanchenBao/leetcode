# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """Prefix sum.

        O(N), 660 ms, faster than 60.63%
        """
        presum = [0]
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                presum.append(presum[-1] + 1)
            else:
                presum.append(presum[-1])
        return [presum[r + 1] - presum[l] for l, r in queries]


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
