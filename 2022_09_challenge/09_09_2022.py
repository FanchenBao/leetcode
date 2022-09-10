# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import Counter
import math


class SegTree:
    def __init__(self, N: int) -> None:
        self.nodes = [-math.inf] * (2**(math.ceil(math.log(N + 1) / math.log(2) + 1)))
        self.upper = N  # upper bound in the right range

    def _update(self, ni: int, pos: int, val: int, rl: int, rr: int) -> None:
        if rl == rr:
            self.nodes[ni] = max(self.nodes[ni], val)
        else:
            mid = (rl + rr) // 2
            if pos <= mid:
                self._update(2 * ni + 1, pos, val, rl, mid)
            else:
                self._update(2 * ni + 2, pos, val, mid + 1, rr)
            self.nodes[ni] = max(self.nodes[2 * ni + 1], self.nodes[2 * ni + 2])

    def _query(self, ni: int, lo: int, hi: int, rl: int, rr: int) -> int:
        if lo == rl and hi == rr:
            return self.nodes[ni]
        mid = (rl + rr) // 2
        if hi <= mid:
            return self._query(2 * ni + 1, lo, hi, rl, mid)
        if lo > mid:
            return self._query(2 * ni + 2, lo, hi, mid + 1, rr)
        return max(
            self._query(2 * ni + 1, lo, mid, rl, mid),
            self._query(2 * ni + 2, mid + 1, hi, mid + 1, rr),
        )

    def update(self, pos: int, val: int) -> None:
        self._update(0, pos, val, 0, self.upper)

    def query(self, lo: int, hi: int) -> int:
        return self._query(0, lo, hi, 0, self.upper)


class Solution1:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """LeetCode 1996

        This solution uses segment tree, but still TLE.
        """
        properties.sort()
        orders = []  # order of attack, not including the max attack
        for i, (a, d) in enumerate(properties):
            order = (orders[-1] + (a > properties[i - 1][0])) if orders else 0
            orders.append(order)
        seg_tree = SegTree(orders[-1])
        for order, (_, d) in zip(orders, properties):
            seg_tree.update(order, d)
        res = 0
        for order, (_, d) in zip(orders, properties):
            if order == orders[-1]:
                break
            if d < seg_tree.query(order + 1, orders[-1]):
                res += 1
        return res


class Solution2:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """Reference to https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445186/EASY-C%2B%2B-solution-with-great-explanation-and-comments-(nlogn)-sorting

        The trick is in the sort. We want to sort attack normally. But when the
        characters have the same attack, we need to sort defense in the reverse
        order.

        Let's say we sort attack descent. Then we must sort the defense of the
        same attack in ascent. This way, as we go from left to right, the
        attack goes down, but the defense under the same attack goes up. This
        way, the largest defense is always updated at the end of the previous
        streak of attack, which means we will always have the biggest attack
        and biggest defense with regard to the remaining properties.

        This is O(NlogN). Solution1 is also O(NlogN), but the overhead of
        segment tree makes it very slow.

        5180 ms, faster than 5.04%
        """
        properties.sort(reverse=True, key=lambda lst: (lst[0], -lst[1]))
        max_a, max_d = -math.inf, -math.inf
        res = 0
        for a, d in properties:
            if a < max_a and d < max_d:
                res += 1
            if d > max_d:
                max_a, max_d = a, d
        return res


sol = Solution2()
tests = [
    ([[5,5],[6,3],[3,6]], 0),
    ([[2,2],[3,3]], 1),
    ([[1,5],[10,4],[4,3]], 1),
    ([[1,1],[2,1],[2,2],[1,2]], 1),
    ([[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]], 6),
    ([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]], 2),
    ([[4,10],[2,2],[8,8],[10,2],[5,5],[9,10],[2,6]], 4),
]

for i, (properties, ans) in enumerate(tests):
    res = sol.numberOfWeakCharacters(properties)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
