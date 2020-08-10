#! /usr/bin/env python3
from typing import List

"""07/28/2019

Not a hard problem. Iterative programming, but pay attention to letter 'z', as
its condition is different than others.

The discussion threw a very good point that in order to avoid the problem of
letter 'z', we shall do 'L' and 'U' before 'R' and 'D'. This is coded in solution2
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        preR, preC = 0, 0
        res: List[str] = []
        for le in target:
            index = ord(le) - 97
            r = index // 5
            c = index % 5
            if le == "z":
                if preC == 0:
                    res += ["D"] * (r - preR)
                else:
                    res += ["D"] * (r - preR - 1)
                    res += ["L"] * (preC - c)
                    res.append("D")
            else:
                if r > preR:
                    res += ["D"] * (r - preR)
                else:
                    res += ["U"] * (preR - r)
                if c > preC:
                    res += ["R"] * (c - preC)
                else:
                    res += ["L"] * (preC - c)
            res.append("!")
            preR, preC = r, c
        return "".join(res)


class Solution2:
    def alphabetBoardPath(self, target: str) -> str:
        preR, preC = 0, 0
        res: List[str] = []
        for le in target:
            index = ord(le) - 97
            r = index // 5
            c = index % 5
            if c < preC:
                res += ["L"] * (preC - c)
            if r < preR:
                res += ["U"] * (preR - r)
            if c >= preC:
                res += ["R"] * (c - preC)
            if r >= preR:
                res += ["D"] * (r - preR)

            res.append("!")
            preR, preC = r, c
        return "".join(res)


sol = Solution2()
print(sol.alphabetBoardPath("code"))
