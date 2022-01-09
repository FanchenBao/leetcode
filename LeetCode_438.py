# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Create a counter for all 26 letters, and then use sliding window to
        keep track of the counter of the current window. If the current counter
        is the same as the pattern, we have a match.

        O(N), where N = len(s). 96 ms, 97% ranking.
        """
        N, M = len(s), len(p)
        if M > N:
            return []
        pcnt = [0] * 26
        for le in p:
            pcnt[ord(le) - 97] += 1
        scnt = [0] * 26
        for i in range(M):
            scnt[ord(s[i]) - 97] += 1
        res = []
        for i in range(N - M + 1):
            if scnt == pcnt:
                res.append(i)
            scnt[ord(s[i]) - 97] -= 1
            if i + M < N:
                scnt[ord(s[i + M]) - 97] += 1
        return res
        

sol = Solution()
tests = [
    ('cbaebabacd', 'abc', [0, 6]),
    ('abab', 'ab', [0, 1, 2]),
]

for i, (s, p, ans) in enumerate(tests):
    res = sol.findAnagrams(s, p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
