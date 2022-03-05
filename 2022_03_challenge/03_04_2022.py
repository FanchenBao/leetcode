# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """LeetCode 799

        Terrible performance. I solved this one two years ago, but couldn't
        solve it today. Granted, I was tight on time, but I was not on the
        right path. The way I was trying to simulate was not correct, because
        I tried to find out when the parent cup gets filled and analyze the
        filling situation per cup for child afterwards. This is vastly
        complicated. I had to see the solution, which uses another way to
        simulate. We keep track of the amount of fluid going through each cup.
        And since the amount spilled is deterministic based on the amount that
        goes through a cup, we can easily compute the amount the children will
        get.

        O(N^2), N is the number of glasses.
        """
        glasses = [[0] * c for c in range(1, 102)]
        glasses[0][0] = poured
        for r in range(query_row + 1):
            for j, g in enumerate(glasses[r]):
                if g > 1:
                    glasses[r + 1][j] += (g - 1) / 2
                    glasses[r + 1][j + 1] += (g - 1) / 2
                    glasses[r][j] = 1
        return glasses[query_row][query_glass]


class Solution2:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """1D DP to save our face.

        108 ms, 88% ranking
        """
        glasses = [0] * 100
        glasses[0] = poured
        for r in range(query_row):
            temp = 0
            for j in range(r + 1):
                spill = max((glasses[j] - 1) / 2, 0)
                glasses[j] = spill + temp
                temp = spill
            glasses[r + 1] = temp
        return min(glasses[query_glass], 1.0)



class Solution3:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """Smarter 1D DP
        """
        glasses = [0] * (query_row + 1)
        glasses[0] = poured
        for r in range(1, query_row + 1):
            for j in range(r, -1, -1):
                glasses[j] = max((glasses[j] - 1) / 2, 0) + max((glasses[j - 1] - 1) / 2, 0)
        return min(glasses[query_glass], 1.0)


sol = Solution3()
tests = [
    (1, 1, 1, 0.0),
    (2, 1, 1, 0.5),
    (100000009, 33, 17, 1.0),
    (1, 1, 0, 0),
]

for i, (poured, query_row, query_glass, ans) in enumerate(tests):
    res = sol.champagneTower(poured, query_row, query_glass)
    if math.isclose(res, ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
