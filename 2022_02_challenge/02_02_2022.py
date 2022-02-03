# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """LeetCode 438

        Sliding window, with a counter.

        O(N), 212 ms, 34% ranking.
        """
        counter = [0] * 26
        target = [0] * 26
        S, P = len(s), len(p)
        if S < P:
            return []
        for i, le in enumerate(p):
            target[ord(le) - 97] += 1
            counter[ord(s[i]) - 97] += 1
        res = [0] if counter == target else []
        for i in range(P, S):
            counter[ord(s[i - P]) - 97] -= 1
            counter[ord(s[i]) - 97] += 1
            if counter == target:
                res.append(i - P + 1)
        return res


sol = Solution()
tests = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
]

for i, (s, p, ans) in enumerate(tests):
    res = sol.findAnagrams(s, p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
