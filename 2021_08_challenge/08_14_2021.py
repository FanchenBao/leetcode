# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import defaultdict
from functools import lru_cache


class Solution1:
    def removeBoxes(self, boxes: List[int]) -> int:
        """LeetCode 546

        We have redeemed ourselves from the slump of last weekend. The first
        insight is that if we have a color with all its boxes already arranged
        consecutively, they can be removed deterministically. After they are
        removed, the arrangement of the boxes changes, and we can try removing
        the consecutive boxes again, until we cannot anymore.

        Then we are left with a list of boxes with repeated colors that are also
        intertwining with each other. Since it is always better to remove the
        boxes of the same color after they are combined into a consecutive
        arrangement (this can be proved mathematically), we will combine each
        color by itself and see what score we can get. We use recursion to
        handle this part. For any color to combine, we recursively compute the
        max score from removing all the other boxes jammed in between. And then
        we compute the max score of the remaining boxes after the target color
        is removed. We do this for all colors, and pick the largest score as our
        result.

        In order to speed up the computation, we use caching. Since our input
        is a list, we have to turn it into a tuple for caching purpose before
        recursive calls.

        I don't know the time complexity. Runtime 940 ms, 77% ranking.
        """

        @lru_cache(None)
        def helper(boxes: Tuple) -> int:
            score = 0
            boxes = list(boxes)
            # remove boxes that all of them are arranged consecutively
            while len(boxes):
                init_len = len(boxes)
                color_idx = defaultdict(list)
                for i, b in enumerate(boxes):
                    color_idx[b].append(i)
                for k, v in color_idx.items():
                    if v[0] + len(v) - 1 == v[-1]:
                        score += len(v) * len(v)
                        for j in v:
                            boxes[j] = 0
                boxes = [b for b in boxes if b]
                if len(boxes) == init_len:
                    break
            if not boxes:
                return score
            next_score = 0
            # Combine each color, and compute what score can we get. Pick the
            # highest score among them.
            for c, v in color_idx.items():
                temp = 0
                for i in range(len(v) - 1):
                    if v[i + 1] != v[i]:
                        temp += helper(tuple(boxes[v[i] + 1:v[i + 1]]))
                temp += len(v)**2 + helper(tuple(boxes[:v[0]] + boxes[v[-1] + 1:]))
                next_score = max(next_score, temp)
            return score + next_score

        return helper(tuple(boxes))


class Solution2:
    def removeBoxes(self, boxes: List[int]) -> int:
        """Very smart and good explanation from here:

        https://leetcode.com/problems/remove-boxes/discuss/1402561/C%2B%2BJavaPython-Top-down-DP-Clear-explanation-with-Picture-Clean-and-Concise
        """

        @lru_cache(None)
        def helper(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            while l < r and boxes[l + 1] == boxes[l]:
                l += 1
                k += 1
            res = helper(l + 1, r, 0) + (k + 1)**2
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    res = max(res, helper(l + 1, i - 1, 0) + helper(i, r, k + 1))
            return res

        return helper(0, len(boxes) - 1, 0)


sol = Solution2()
tests = [
    ([1, 1, 1], 9),
    ([1], 1),
    ([1, 3, 2, 2, 2, 3, 4, 3, 1], 23),
    ([4, 3, 3, 4, 3, 4, 3, 4], 22),
    ([6, 10, 1, 7, 1, 3, 10, 2, 1, 3], 16),
    ([1, 2, 3, 4, 3, 1, 4, 3, 2, 1], 20),
    ([14, 25, 39, 54, 14, 95, 22, 79, 77, 91, 7, 59, 21, 1, 67, 73, 65, 60, 47, 24, 73, 42, 70, 44, 22, 68, 27, 13, 39, 63, 66, 23, 82, 87, 9, 19, 78, 11, 6, 74, 52, 62, 66, 81, 75, 40, 38, 75, 53, 61, 4, 76, 10, 44, 56, 69, 50, 78, 88, 70, 27, 77, 66, 50, 45, 18, 6, 57, 82, 64, 61, 38, 34, 43, 56, 73, 19, 97, 64, 39, 98, 52, 100, 91, 65, 14, 39, 25, 13, 32, 27, 30, 54, 11, 26, 67, 32, 55, 20, 24], 130),
]

for i, (boxes, ans) in enumerate(tests):
    res = sol.removeBoxes(boxes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
