# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lst = []
        N = len(spaces)
        for i, idx in enumerate(spaces):
            if i == 0:
                lst.append(s[:idx])
            else:
                lst.append(s[spaces[i - 1]:idx])
            if i == N - 1:
                lst.append(s[idx:])
        return ' '.join(lst)


sol = Solution()
tests = [
    ("LeetcodeHelpsMeLearn", [8,13,15], "Leetcode Helps Me Learn"),
    ("icodeinpython", [1,5,7,9], "i code in py thon"),
    ("spacing", [0,1,2,3,4,5,6], " s p a c i n g"),
    ("p", [0], " p"),
]

for i, (s, spaces, ans) in enumerate(tests):
    res = sol.addSpaces(s, spaces)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
