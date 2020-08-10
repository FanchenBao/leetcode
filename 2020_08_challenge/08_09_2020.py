# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution1:
    """Solution1 keeps track of the fresh ones, but it is not efficient because
    it requires update of the newly rotten oranges in the grid after each time
    tick. This pushes the algo to O(n^2)
    """

    def update_grid(self, grid):
        for r, _ in enumerate(grid):
            for c, _ in enumerate(grid[0]):
                if grid[r][c] == -1:
                    grid[r][c] = 2

    def has_rotten_neighbor(self, r, c, grid):
        res = False
        for r_delta, c_delta in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            adj_r, adj_c = r + r_delta, c + c_delta
            if adj_r < 0 or adj_r >= len(grid) or adj_c < 0 or adj_c >= len(grid[0]):
                continue
            else:
                res = res or grid[adj_r][adj_c] == 2
        return res

    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        freshes = [(r, c) for c in range(len_col) for r in range(len_row) if grid[r][c] == 1]
        time_tick = 0
        while True:
            has_rotten = False
            for i, (r, c) in enumerate(freshes):
                if self.has_rotten_neighbor(r, c, grid):
                    grid[r][c] = -1  # marked. To be turned to rotten next
                    freshes[i] = ()
                    has_rotten = True
            if not has_rotten:
                break
            freshes = [coord for coord in freshes if coord]
            time_tick += 1
            self.update_grid(grid)
        return -1 if freshes else time_tick


class Solution2:
    """Solution2 keeps track of the rotten ones. Since there is no need to
    update the grid, this solution is O(m*n)
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        rottens = deque()
        num_freshes = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    rottens.append((r, c))
                elif val == 1:
                    num_freshes += 1
        time_tick = 0
        while rottens and num_freshes:
            for _ in range(len(rottens)):
                rot_r, rot_c = rottens.popleft()
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    r = rot_r + dr
                    c = rot_c + dc
                    if 0 <= r < len_row and 0 <= c < len_col and grid[r][c] == 1:
                        rottens.append((r, c))
                        num_freshes -= 1
                        grid[r][c] = 2
            time_tick += 1
        return -1 if num_freshes else time_tick

# tests = [
#     (('catsanddog', ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"]),
#     (("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]),
#     (("catsandog", ["cats", "dog", "sand", "and", "cat"]), []),
#     # (("aaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), []),
#     (("catsandog", ["cats", "dog", "sandog", "and", "cat"]), ['cat sandog']),
#     (('bb', ["a","b","bbb","bbbb"]), ['b b'])
# ]


sol = Solution2()

print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
# for i, test in enumerate(tests):
#     (s, wordDict), ans = test
#     res = sol.wordBreak(s, wordDict)
#     if res == ans:
#         print(f'Test {i + 1}: PASS')
#     else:
#         print(f'Test {i + 1}: Fail. Received: {res}, Expected: {ans}')
