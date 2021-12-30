# from pudb import set_trace; set_trace()
from typing import List



# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution1:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """LeetCode 116

        Recursion solution.

        O(N), 102 ms, 8% ranking.
        """

        def helper(node: Optional[Node]) -> None:
            if node and node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                helper(node.left)
                helper(node.right)

        helper(root)
        return root


class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """BFS

        O(N), 121 ms, 5% ranking.
        """
        queue = [root]
        while queue:
            temp = []
            N = len(queue)
            for i, node in enumerate(queue):
                if i < N - 1:
                    node.next = queue[i + 1]
                if node and node.left:
                    temp.append(node.left)
                if node and node.right:
                    temp.append(node.right)
            queue = temp
        return root


class Solution3:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """This is the solution I recorded more than a year ago when I first
        encountered this problem. It is also recursion, but handles the linking
        a bit more uniformly.
        """

        def helper(node: 'Optional[Node]') -> None:
            if node:
                left, right = node.left, node.right
                while left:
                    left.next = right
                    left = left.right
                    right = right.left
                helper(node.left)
                helper(node.right)

        helper(root)
        return root



        

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
