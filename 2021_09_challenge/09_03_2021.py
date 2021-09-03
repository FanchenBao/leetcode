# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import defaultdict
import math


class Solution1:
    def connect(self, slopes: List, x: int, y: int, is_top: bool) -> None:
        while True:
            pre_x, pre_y = slopes[-1][1].real, slopes[-1][1].imag
            k = (y - pre_y) / (x - pre_x)  # current slope
            if math.isclose(k, slopes[-1][0]) or (is_top and k < slopes[-1][0]) or (not is_top and k > slopes[-1][0]):
                slopes.append([k, x + y * 1j])
                return
            else:
                slopes.pop()

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """LeetCode 587

        The idea is that we group all the trees by their x-axis. Then for
        each col of trees, we find the top and bottom tree. We want to draw a
        top fence and bottom fence to include all the trees. When we draw the
        top fence, we iterate on the x-axis from small to large, and if the
        slope of the new line is larger than that of the previous line, we have
        a concave case. Thus, we pop the previous tree, and try the same
        procedure again, until the previous slope is bigger than the current one.
        Similarly, we draw the bottom line and require that the new slope must
        be bigger than the previous one.

        After drawing the top and bottom lines, the left and right lines are
        trivial, as they consist of all the trees with the min and max x-axis.

        The final piece is to avoid duplicates. To do that, we turn all the
        coordinates into complex numbers and use set to eliminate duplicates.

        O(NlogN) time complexity, 219 ms, 89% ranking.
        """
        outposts = defaultdict(list)
        for x, y in trees:
            outposts[x].append(y)
        top_k, bot_k = [[math.inf, -1]], [[-math.inf, -1]]
        sorted_xs = sorted(outposts)
        for x in sorted_xs:
            max_y = max(outposts[x])
            min_y = min(outposts[x])
            if top_k[-1][1] == -1:
                top_k[-1][1] = x + max_y * 1j
            else:
                self.connect(top_k, x, max_y, True)
            if bot_k[-1][1] == -1:
                bot_k[-1][1] = x + min_y * 1j
            else:
                self.connect(bot_k, x, min_y, False)
        res_set = set([xy for _, xy in top_k[1:-1]] + [xy for _, xy in bot_k[1:-1]] + [sorted_xs[0] + y * 1j for y in outposts[sorted_xs[0]]] + [sorted_xs[-1] + y * 1j for y in outposts[sorted_xs[-1]]])
        return [[int(xy.real), int(xy.imag)] for xy in res_set]


class Solution2:
    def traverse(
        self,
        rest_trees: List[Tuple[int, int]],
        beg_tree: Tuple[int, int],
        end_tree: Tuple[int, int],
    ) -> List:
        fence = [beg_tree, rest_trees[0]]
        for x, y in rest_trees[1:] + [end_tree]:
            while len(fence) >= 2:
                v1 = [fence[-1][0] - fence[-2][0], fence[-1][1] - fence[-2][1]]
                v2 = [x - fence[-1][0], y - fence[-1][1]]
                if v1[0] * v2[1] - v1[1] * v2[0] < 0:
                    fence.pop()
                else:
                    break
            fence.append((x, y))
        return fence

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """Monotone Chain

        Ref: https://leetcode.com/problems/erect-the-fence/solution/

        It is similar to Solution1 except that we don't use slope to decide
        whether a previous point needs to be popped. We use cross product
        instead. Furthermore, we don't have to go through only the top and
        bottom trees. We can go through every tree. The bottom fence traverse
        requires cross product to be positive, as we are looking for a left
        turn. The top fence traverse is going from the right to left also looking
        for a left turn.

        cross product of two vector A (a1, a2, 0) and B (b1, b2, 0) is
        C (0, 0, a1b2 - a2b1)
        """
        # Get the left and right most trees
        min_x = min(x for x, _ in trees)
        max_x = max(x for x, _ in trees)
        left_most_ys = []
        right_most_ys = []
        rest_trees = []
        for x, y in trees:
            if x == min_x:
                left_most_ys.append(y)
            elif x == max_x:
                right_most_ys.append(y)
            else:
                rest_trees.append((x, y))
        if not rest_trees:
            return trees
        rest_trees.sort()
        bot_fence = self.traverse(rest_trees, (min_x, min(left_most_ys)), (max_x, min(right_most_ys)))
        top_fence = self.traverse(rest_trees[::-1], (max_x, max(right_most_ys)), (min_x, max(left_most_ys)))
        return [[x, y] for x, y in set(bot_fence + top_fence + [(min_x, y) for y in left_most_ys] + [(max_x, y) for y in right_most_ys])]


sol = Solution2()
tests = [
    ([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]], [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]]),
    ([[1, 2], [2, 2], [4, 2]], [[1, 2], [2, 2], [4, 2]]),
    ([[1, 1], [1, 2], [1, 3]], [[1, 1], [1, 2], [1, 3]]),
    ([[1, 1]], [[1, 1]]),
    ([[1, 1], [4, 4], [4, 1], [2, 3]], [[1, 1], [4, 4], [4, 1], [2, 3]]),
    ([[1, 1], [4, 4], [1, 4], [2, 3]], [[1, 1], [4, 4], [1, 4]]),
    ([[5, 5], [4, 8], [1, 3], [5, 9], [3, 0], [0, 4], [3, 2], [8, 9], [9, 3]], [[9, 3], [5, 9], [4, 8], [3, 0], [0, 4], [8, 9]]),
    ([[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [3, 3]], [[0, 1], [3, 0], [1, 0], [3, 2], [0, 0], [3, 1], [2, 0], [0, 2], [3, 3]]),
]

for i, (trees, ans) in enumerate(tests):
    res = sol.outerTrees(trees)
    res = sorted(res, key=lambda tup: (tup[0], tup[1]))
    ans = sorted(ans, key=lambda tup: (tup[0], tup[1]))
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
