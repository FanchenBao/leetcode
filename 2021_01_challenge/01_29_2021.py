# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, deque
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """Not too difficult a problem, as long as the correct data structure
        is used. We traverse through the entire tree, either BFS or DFS.
        We also record the coordinates of each node. And each node we
        visit, we place the node in a mapping (res_dict) according to
        the node's coordinates. We use the x coordinate as the key
        in the mapping, and the value is a tuple of -y coordiate and the
        node's value. Note that it is crucial to put minus y coordinate, i.e.
        to make the y coordinate positive.

        After traversing the tree, we continue to process the mapping.
        For each value, which is a list of tuples, we need to sort based on
        -y coordinates and node values. Since we use the -y coordinate, we
        can sort based on both in ascending order.

        Finally, we take the values out of the mapping into a new list
        according to the order in the keys.

        O(N + Nlog(N)) = O(Nlog(N)), 32 ms, 80% ranking.
        """
        res_dict = defaultdict(list)
        queue = deque([(0, 0, root)])
        while queue:
            x, y, node = queue.popleft()
            if node.left is not None:
                queue.append((x - 1, y - 1, node.left))
            if node.right is not None:
                queue.append((x + 1, y - 1, node.right))
            res_dict[x].append((-y, node.val))
        res = []
        for k in sorted(res_dict.keys()):
            res_dict[k].sort(key=lambda tup: (tup[0], tup[1]))
            res.append([tup[1] for tup in res_dict[k]])
        return res


class Wrapper():
    def __init__(self, node: TreeNode, x: int, y: int):
        self.val = node.val
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return self.val < other.val
            return self.y > other.y
        return self.x < other.x

    def __repr__(self):
        return f'({self.val}, {self.x}, {self.y})'


class Solution2:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """Pure priority queue method. Refer to here:
        https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231425/Java-Solution-using-Only-PriorityQueue

        There is no improvement in runtime, but I think this is a smart
        use of priority. The implementation of the __lt__ method got me into
        some trouble but luckily I eventually figured out, after taking a
        grocery trip.

        O(Nlog(N)), 36 ms.
        """
        pq = []

        def dfs(node: TreeNode, x: int, y: int):
            if node:
                heapq.heappush(pq, Wrapper(node, x, y))
                dfs(node.left, x - 1, y - 1)
                dfs(node.right, x + 1, y - 1)

        dfs(root, 0, 0)
        res, lst = [], []
        pre_x = None
        while pq:
            wrapper = heapq.heappop(pq)
            if pre_x is None or pre_x != wrapper.x:
                if lst:
                    res.append(lst)
                lst = []
                pre_x = wrapper.x
            lst.append(wrapper.val)
        return res + [lst]


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
