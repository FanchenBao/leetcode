# from pudb import set_trace; set_trace()
from typing import List


class TreeNode:
    def __init__(self):
        self.l_cont = ['', 0]
        self.r_cont = ['', 0]
        self.max_cont = 0
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, s: str):
        self.lst = list(s)
        self.root = self.build(0, len(s) - 1)

    def merge_left_right_child(self, node: TreeNode, lrange: int, rrange: int) -> None:
        is_l_all_same = node.left.l_cont[0] == node.left.r_cont[0] and node.left.l_cont[1] == node.left.r_cont[1] == lrange
        is_r_all_same = node.right.l_cont[0] == node.right.r_cont[0] and node.right.l_cont[1] == node.right.r_cont[1] == rrange
        # left all the same, right all the same
        if is_l_all_same and is_r_all_same:
            if node.left.r_cont[0] != node.right.l_cont[0]:
                cross = 0
                node.l_cont = node.left.l_cont[:]
                node.r_cont = node.right.r_cont[:]
            else:
                cross = node.left.r_cont[1] + node.right.l_cont[1]
                node.l_cont = [node.left.l_cont[0], cross]
                node.r_cont = [node.right.r_cont[0], cross]
        elif is_l_all_same and not is_r_all_same:
            if node.left.r_cont[0] != node.right.l_cont[0]:
                cross = 0
                node.l_cont = node.left.l_cont[:]
            else:
                cross = node.left.r_cont[1] + node.right.l_cont[1]
                node.l_cont = [node.left.l_cont[0], cross]
            node.r_cont = node.right.r_cont[:]
        elif not is_l_all_same and is_r_all_same:
            if node.left.r_cont[0] != node.right.l_cont[0]:
                cross = 0
                node.r_cont = node.right.r_cont[:]
            else:
                cross = node.left.r_cont[1] + node.right.l_cont[1]
                node.r_cont = [node.right.r_cont[0], cross]
            node.l_cont = node.left.l_cont[:]
        else:  # left not all the same, right not all the same
            if node.left.r_cont[0] != node.right.l_cont[0]:
                cross = 0
            else:
                cross = node.left.r_cont[1] + node.right.l_cont[1]
            node.l_cont = node.left.l_cont[:]
            node.r_cont = node.right.r_cont[:]
        node.max_cont = max(node.left.max_cont, node.right.max_cont, cross)

    def build(self, l: int, r: int) -> TreeNode:
        node = TreeNode()
        if l == r:
            node.l_cont = [self.lst[l], 1]
            node.r_cont = [self.lst[r], 1]
            node.max_cont = 1
        else:
            mid = (l + r) // 2
            node.left, node.right = self.build(l, mid), self.build(mid + 1, r)
            self.merge_left_right_child(node, mid - l + 1, r - mid)
        return node

    def update(self, node: TreeNode, idx: int, new_le: str, l: int, r: int) -> None:
        if idx == l == r:
            self.lst[idx] = new_le
            node.l_cont[0] = new_le
            node.r_cont[0] = new_le
        else:
            mid = (l + r) // 2
            if idx > mid:
                self.update(node.right, idx, new_le, mid + 1, r)
            else:
                self.update(node.left, idx, new_le, l, mid)
            self.merge_left_right_child(node, mid - l + 1, r - mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        """TLE.
        """
        tree = SegmentTree(s)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(tree.root, idx, ch, 0, len(s) - 1)
            res.append(tree.root.max_cont)
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
