# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """LeetCode 764

        TLE.

        Anyhow, the logic is to find what plus signs at each rank cannot be
        formed by checking each mine. Once that is done, we have the total
        number of impossible plus signs at each rank. Then we can compare the
        impossible count to the total count at each rank. If the latter is
        larger than the former, we are sure a plus sign of that rank can be
        formed.

        It's too slow, because there are a lot of checks at each mine.
        """
        max_r = (n + 1) // 2
        impos = defaultdict(set)
        for x, y in mines:
            # check rows:
            rank_lim = min(x, n - 1 - x) + 1
            for pot_y in range(max(y - rank_lim + 1, 0), min(y + rank_lim - 1, n - 1) + 1):
                for rank in range(abs(pot_y - y) + 1, min(rank_lim, min(pot_y, n - 1 - pot_y) + 1) + 1):
                    impos[rank].add(x + pot_y * 1j)
            # check cols
            rank_lim = min(y, n - 1 - y) + 1
            for pot_x in range(max(x - rank_lim + 1, 0), min(x + rank_lim - 1, n - 1) + 1):
                for rank in range(abs(pot_x - x) + 1, min(rank_lim, min(pot_x, n - 1 - pot_x) + 1) + 1):
                    impos[rank].add(pot_x + y * 1j)
        size = 1 if n % 2 else 2
        for rank in range(max_r, 0, -1):
            if size**2 > len(impos[rank]):
                return rank
            size += 2
        return 0


class Solution2:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """Using the hint.

        We create four DP table to record the number of ones
        encountered before a 0 in four directions. Then the highest rank plus
        sign that can be forned at any location is the min value of the four
        directions.

        O(N^2), 3772 ms 
        """
        mines_set = set(x + y * 1j for x, y in mines)
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i + j * 1j not in mines_set:
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j - 1] + 1
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if i + j * 1j not in mines_set:
                    if j == n - 1:
                        right[i][j] = 1
                    else:
                        right[i][j] = right[i][j + 1] + 1
        for j in range(n):
            for i in range(n):
                if i + j * 1j not in mines_set:
                    if i == 0:
                        up[i][j] = 1
                    else:
                        up[i][j] = up[i - 1][j] + 1
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if i + j * 1j not in mines_set:
                    if i == n - 1:
                        down[i][j] = 1
                    else:
                        down[i][j] = down[i + 1][j] + 1
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, min(up[i][j], down[i][j], left[i][j], right[i][j]))
        return res


class Solution3:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """From the official solution. Use only one dp table.
        """
        mines_set = set(x + y * 1j for x, y in mines)
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            count = 0
            for j in range(n):  # looking to the left
                count = 0 if i + j * 1j in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if i + j * 1j in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if i + j * 1j in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if i + j * 1j in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, dp[i][j])
        return res


sol = Solution3()
tests = [
    (5, [[4, 2]], 2),
    (1, [[0, 0]], 0),
    (2, [[0, 0]], 1),
    (5, [[0, 2], [0, 4], [1, 2], [2, 0], [2, 3], [2, 4], [3, 4], [4, 2], [4, 4]], 2),
    (5, [[0, 0], [0, 3], [1, 1], [1, 4], [2, 3], [3, 0], [4, 2]], 1),
    (10, [[0, 0], [0, 1], [0, 2], [0, 4], [0, 5], [0, 8], [0, 9], [1, 0], [1, 1], [1, 3], [1, 5], [1, 6], [1, 7], [1, 9], [2, 0], [2, 1], [2, 2], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [3, 0], [3, 1], [3, 2], [3, 4], [3, 5], [3, 7], [3, 8], [4, 0], [4, 1], [4, 2], [4, 4], [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 5], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1], [7, 6], [7, 7], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 5], [8, 9], [9, 1], [9, 3], [9, 4], [9, 5], [9, 6], [9, 8]], 2),
]

for i, (n, mines, ans) in enumerate(tests):
    res = sol.orderOfLargestPlusSign(n, mines)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
