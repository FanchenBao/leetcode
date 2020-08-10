#! /usr/bin/env python3
from typing import Dict
from collections import Counter

"""09/14/2019

Solution1:
My original solution, very straightforward and simple, but since I didn't know
Counter would return 0 if a key has not been counted, this solution is a bit
more convoluted than Solution2. Solution 1 clocked in at 40 ms.

Solution2:
Fully leveraging Counter. It also clocked in at 40 ms.
"""


class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        count: Dict[str, int] = Counter(text)
        res = 10 ** 4
        for e in "balon":
            if e not in count:
                return 0
            else:
                if e in {"b", "a", "n"}:
                    res = min(res, count[e])
                elif e in {"l", "o"}:
                    res = min(res, count[e] // 2)
        return res


class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        count: Dict[str, int] = Counter(text)
        return min(
            count["b"],
            count["a"],
            count["l"] // 2,
            count["o"] // 2,
            count["n"],
        )


sol = Solution2()
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
