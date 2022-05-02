# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """LeetCode 844

        Use stack

        56 ms, faster than 18.09%
        """
        ss, st = [], []
        for l in s:
            if l != '#':
                ss.append(l)
            elif ss:
                ss.pop()
        for l in t:
            if l != '#':
                st.append(l)
            elif st:
                st.pop()
        return ss == st


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """O(1) space, O(N) time solution.

        48 ms, faster than 35.59% 
        """
        i, j = len(s) - 1, len(t) - 1
        cs, ct = 0, 0

        def helper(string, i, c) -> int:
            while i >= 0 and (string[i] == '#' or c > 0):
                if string[i] == '#':
                    c += 1
                else:
                    c -= 1
                i -= 1
            return i, c

        while i >= 0 and j >= 0:
            i, cs = helper(s, i, cs)
            j, ct = helper(t, j, ct)
            if i >= 0 and j >= 0 and s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                break
        i, cs = helper(s, i, cs)
        j, ct = helper(t, j, ct)
        return i == j == -1


sol = Solution2()
tests = [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a#c", "b", False),
    ("y#fo##f", "y#f#o##f", True),
    ("nzp#o#g", "b#nzp#o#g", True),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.backspaceCompare(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
