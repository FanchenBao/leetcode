# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        for i in range(len(s)):
            p, q = startPos
            j = i
            while j < len(s):
                if s[j] == 'R':
                    q += 1
                elif s[j] == 'L':
                    q -= 1
                elif s[j] == 'U':
                    p -= 1
                else:
                    p += 1
                if p < 0 or p >= n or q < 0 or q >= n:
                    break
                j += 1
            res.append(j - i)
        return res


sol = Solution()
tests = [
    (3, [0, 1], 'RRDDLU', [1, 5, 4, 3, 1, 0]),
    (2, [1, 1], 'LURD', [4, 1, 0, 0]),
    (1, [0, 0], 'LRUD', [0, 0, 0, 0]),
]

for i, (n, startPos, s, ans) in enumerate(tests):
    res = sol.executeInstructions(n, startPos, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
