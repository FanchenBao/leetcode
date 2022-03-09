# from pudb import set_trace; set_trace()
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: Node, quadTree2: Node) -> Node:
        """This problem might seem complicated, but once one understands how
        the quad-tree works, it's quite straightforward using recursion. One
        important observation is that if one of quadTree is leaf, we already
        hit the anchor case. If neither of the quadTrees are leaf, we need to
        evaluate each of the four substrees, and then combine the result. The
        combination is important to identify whether all children have the
        same value.

        O(logN), 83 ms, 58% ranking.
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val == 1 else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val == 1 else quadTree1
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            return Node(val=tl.val, isLeaf=True)
        return Node(val=-1, isLeaf=False, topLeft=tl, topRight=tr, bottomLeft=bl, bottomRight=br)


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
