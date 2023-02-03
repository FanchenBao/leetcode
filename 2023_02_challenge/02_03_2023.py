# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """LeetCode 6

        Down and up, repeat this pattern. No need to create a full matrix, we
        just need to add new letter to each row as needed.

        O(N), 59 ms, faster than 76.82% 
        """
        rows = [[] for _ in range(numRows)]
        i = 0
        N = len(s)
        while i < N:
            for row in rows:
                if i < N: 
                    row.append(s[i])
                    i += 1
                else:
                    break
            for j in range(numRows - 2, 0, -1):
                if i < N:
                    rows[j].append(s[i])
                    i += 1
                else:
                    break
        return ''.join(rowstr for rowstr in (''.join(row) for row in rows))


sol = Solution()
tests = [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
]

for i, (s, numRows, ans) in enumerate(tests):
    res = sol.convert(s, numRows)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
