# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """LeetCode 587

        I kind of remember how the official solution drew the outline. For me,
        I first find the top and bottom trees for each col. Then I draw the
        boundary at the top by connecting the top trees of each pair of adjacent
        cols. The only requirement is that the slope of the new pair must be
        smaller or equal to the previous pair. If this cannot be satisfied, we
        pop the previous tree. This popping continues until we have the current
        pair satisfies the slope requirement or if there is only one tree left
        for pairing.

        Similarly, we do the same for the bottom trees, except the slope
        requirement is that the new slope must be bigger or equal to the
        previous slope.

        O(NlogN), 520 ms, faster than 66.27%
        """
        coords = defaultdict(list)
        for x, y in trees:
            coords[x].append(y)
        for ys in coords.values():
            ys.sort()
        xs = sorted(coords)
        # handle the tops
        tops = [(xs[0], coords[xs[0]][-1])]
        for i in range(1, len(xs)):
            x, y = xs[i], coords[xs[i]][-1]
            while len(tops) > 1 and (y - tops[-1][1]) / (x - tops[-1][0]) > (tops[-1][1] - tops[-2][1]) / (tops[-1][0] - tops[-2][0]):
                tops.pop()
            tops.append((x, y))
        # handle the bottoms
        bots = [(xs[0], coords[xs[0]][0])]
        for i in range(1, len(xs)):
            x, y = xs[i], coords[xs[i]][0]
            while len(bots) > 1 and (y - bots[-1][1]) / (x - bots[-1][0]) < (bots[-1][1] - bots[-2][1]) / (bots[-1][0] - bots[-2][0]):
                bots.pop()
            bots.append((x, y))
        # handle the left and right extremes
        res = [[x, y] for x, y in set(tops).union(set(bots))]
        for i in range(1, len(coords[xs[0]]) - 1):
            res.append([xs[0], coords[xs[0]][i]])
        for i in range(1, len(coords[xs[-1]]) - 1):
            res.append([xs[-1], coords[xs[-1]][i]])
        return res


sol = Solution()
tests = [
    ([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]], [[1,1],[2,0],[3,3],[2,4],[4,2]]),
    ([[1,2],[2,2],[4,2]], [[4,2],[2,2],[1,2]]),
    ([[0,2],[1,1],[2,2],[2,4],[4,2],[3,3]], [[0,2],[4,2],[3,3],[1,1],[2,4]]),
]

for i, (trees, ans) in enumerate(tests):
    res = sol.outerTrees(trees)
    ans.sort()
    res.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
