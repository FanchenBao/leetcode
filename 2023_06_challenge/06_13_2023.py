# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict


class Solution1:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """LeetCode 2352

        Turn each row and col into string, and match string using Counter.

        O(N^2), 582 ms, faster than 42.69%
        """
        N = len(grid)
        row_counter = Counter(','.join(str(c) for c in row) for row in grid)
        res = 0
        for j in range(N):
            col_str = ','.join(str(grid[i][j]) for i in range(N))
            res += row_counter[col_str]
        return res


class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """LeetCode 2352

        Turn each row and col into Tuple, and match Tuple using Counter.

        O(N^2), 510 ms, faster than 60.81%
        """
        N = len(grid)
        row_counter = Counter(tuple(c for c in row) for row in grid)
        res = 0
        for j in range(N):
            col_str = tuple(grid[i][j] for i in range(N))
            res += row_counter[col_str]
        return res


class Solution3:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """Use Trie

        O(N^2), 565 ms, faster than 45.67%
        """
        N = len(grid)
        trie = lambda: defaultdict(trie)
        # build trie from all the rows
        root = trie()
        for row in grid:
            node = root
            for c in row:
                node = node[c]
            node['*'] = node.get('*', 0) + 1  # count the number of rows ending in the same node 
        # match col to trie
        res = 0
        for j in range(N):
            node = root
            for i in range(N):
                if grid[i][j] in node:
                    node = node[grid[i][j]]
                else:
                    break
            else:
                res += node.get('*', 0)
        return res


sol = Solution3()
tests = [
    ([[3,2,1],[1,7,6],[2,7,7]], 1),
    ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.equalPairs(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
