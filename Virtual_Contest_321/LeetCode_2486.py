# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """Try to match as much t in s as possible. Then the number of letters
        not matched in t must be appended to s

        O(N)
        """
        j = 0
        for le in s:
            if j == len(t):
                break
            if le == t[j]:
                j += 1
        return len(t) - j


sol = Solution()
tests = [
    ("coaching", "coding", 4),
    ("abcde", "a", 0),
    ("z", "abcde", 5),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.appendCharacters(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
