# from pudb import set_trace; set_trace()
from typing import List
import math


class SegmentTree:
    def __init__(self, s: str):
        self.lst = list(s)
        # each node is [lstr, lcont, rstr, rcont, maxcont]
        self.tree = [[0] * 5 for _ in range(4 * len(s))]  # 4 * len is magic code
        self.build(0, 0, len(s) - 1)

    def merge_left_right_child(self, ni: int, lrange: int, rrange: int) -> None:
        li, ri = ni * 2 + 1, ni * 2 + 2
        cross = (
            self.tree[li][2] == self.tree[ri][0]
        ) * (
            self.tree[li][3] + self.tree[ri][1]
        )
        self.tree[ni][0] = self.tree[li][0]
        self.tree[ni][2] = self.tree[ri][2]
        self.tree[ni][1] = cross if cross and self.tree[li][0] == self.tree[li][2] and self.tree[li][1] == self.tree[li][3] == lrange else self.tree[li][1]
        self.tree[ni][3] = cross if cross and self.tree[ri][0] == self.tree[ri][2] and self.tree[ri][1] == self.tree[ri][3] == rrange else self.tree[ri][3]
        self.tree[ni][4] = max(self.tree[li][4], self.tree[ri][4], cross)

    def build(self, ni: int, l: int, r: int) -> None:
        if l == r:
            self.tree[ni] = [self.lst[l], 1, self.lst[r], 1, 1]
        else:
            mid = (l + r) // 2
            self.build(ni * 2 + 1, l, mid)
            self.build(ni * 2 + 2, mid + 1, r)
            self.merge_left_right_child(ni, mid - l + 1, r - mid)

    def update(self, ni: int, idx: int, new_le: str, l: int, r: int) -> None:
        if idx == l == r:
            self.lst[idx] = new_le
            self.tree[ni][0] = new_le
            self.tree[ni][2] = new_le
        else:
            mid = (l + r) // 2
            if idx > mid:
                self.update(ni * 2 + 2, idx, new_le, mid + 1, r)
            else:
                self.update(ni * 2 + 1, idx, new_le, l, mid)
            self.merge_left_right_child(ni, mid - l + 1, r - mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        """After several days of failure, finally I passed with the help from
        discussion. I was able to code the segment tree, but the discussion
        helped with converting a node-based segment tree to list representation
        which speeds things up. Also, the size of the list needs to be
        magically set to 4 * len(s), otherwise still time out.

        O(Nlog(N)), 9820 ms, 5% ranking.
        """
        tree = SegmentTree(s)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(0, idx, ch, 0, len(s) - 1)
            res.append(tree.tree[0][4])
        return res


sol = Solution()
tests = [
    ("babacc", "bcb", [1,3,3], [3, 3, 4]),
    ("abyzz", "aa", [2,1], [2, 3]),
    ("geuqjmt", "bgemoegklm", [3,4,2,6,5,6,5,4,3,2], [1,1,2,2,2,2,2,2,2,1]),
]

for i, (s, queryCharacters, queryIndices, ans) in enumerate(tests):
    res = sol.longestRepeating(s, queryCharacters, queryIndices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
