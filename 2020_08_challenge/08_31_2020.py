# from pudb import set_trace; set_trace()
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.deleted = False

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """This solution passed OJ, but compared to the sample code, it is
        quite shabby.
        """
        if root is None:
            return None
        if root.val != key:
            if not self.deleted:
                root.left = self.deleteNode(root.left, key)
            if not self.deleted:
                root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            else:
                most_left = root.right
                most_left_parent = root
                while most_left.left:  # find the smallest node on the right branch
                    most_left_parent = most_left
                    most_left = most_left.left
                root.val = most_left.val  # swap the smallest right-branch node with the deleted value
                if most_left_parent == root:
                    most_left_parent.right = most_left.right
                else:
                    most_left_parent.left = most_left.right
            self.deleted = True
        return root


class Solution2:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """A good solution from https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3443/discuss/93374/Simple-Python-Solution-With-Explanation"""
        if root is None:
            return None
        if root.val < key:
            root.left = self.deleteNode(root.left, key)
        elif root.val > key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                most_left = root.right
                min_val = most_left.val
                while most_left.left:  # find the smallest node on the right branch
                    most_left = most_left.left
                    min_val = most_left.val
                root.val = min_val  # swap the smallest right-branch node with the deleted value
                root.right = self.deleteNode(root.right, root.val)  # delete the mnin_val
        return root