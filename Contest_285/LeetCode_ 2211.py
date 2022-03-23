# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countCollisions(self, directions: str) -> int:
        dlist = list(directions)
        res = 0
        for i in range(len(dlist) - 1):
            if dlist[i] == 'R' and dlist[i + 1] == 'L':
                dlist[i] = dlist[i + 1] = 'S'
                res += 2
        for i in range(len(dlist) - 1):
            if dlist[i] == 'S' and dlist[i + 1] == 'L':
                dlist[i + 1] = 'S'
                res += 1
        for i in range(len(dlist) - 1, 0, -1):
            if dlist[i] == 'S' and dlist[i - 1] == 'R':
                dlist[i - 1] = 'S'
                res += 1
        return res
        
        
sol = Solution()
tests = [
    ('RLRSLL', 5),
    ('LLRR', 0),
]

for i, (directions, ans) in enumerate(tests):
    res = sol.countCollisions(directions)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
