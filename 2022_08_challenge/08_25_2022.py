# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """LeetCode 383

        O(N), 77 ms, faster than 68.29%
        """
        return len(Counter(ransomNote) - Counter(magazine)) == 0


sol = Solution()
tests = [
    ('a', 'b', False),
    ('aa', 'ab', False),
    ('aa', 'aab', True),
]

for i, (ransomNote, magazine, ans) in enumerate(tests):
    res = sol.canConstruct(ransomNote, magazine)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
