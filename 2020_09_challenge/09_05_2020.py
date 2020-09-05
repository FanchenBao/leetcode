# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root: TreeNode, sorted_lst: List[int]) -> None:
        if root:
            self.inorder(root.left, sorted_lst)
            sorted_lst.append(root.val)
            self.inorder(root.right, sorted_lst)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        sorted_lst1, sorted_lst2 = [], []
        self.inorder(root1, sorted_lst1)
        self.inorder(root2, sorted_lst2)
        inf = 10**6
        sorted_lst1.append(inf)
        sorted_lst2.append(inf)
        res = []
        i1, i2 = 0, 0
        while sorted_lst1[i1] != inf or sorted_lst2[i2] != inf:
            if sorted_lst1[i1] <= sorted_lst2[i2]:
                res.append(sorted_lst1[i1])
                i1 += 1
            else:
                res.append(sorted_lst2[i2])
                i2 += 1
        return res
