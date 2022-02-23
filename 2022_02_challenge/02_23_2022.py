# from pudb import set_trace; set_trace()
from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """LeetCode 133

        Not sure if this is the best solution, but I don't think it is possible
        to clone the graph without preparing the cloned nodes in an addressable
        manner. Here, I use a dict to address the clined nodes, and use DFS
        to traverse the original graph. Basically, we create an adjacency list
        but without actually building a list, but building a new graph.

        O(N), 32 ms, 98% ranking.
        """
        if not node:
            return None
        copy = {}
        
        def dfs(node, seen) -> None:
            if node:
                seen.add(node.val)
                if node.val not in copy:
                    copy[node.val] = Node(val=node.val)
                for nei in node.neighbors:
                    if nei.val not in copy:
                        copy[nei.val] = Node(val=nei.val)
                    copy[node.val].neighbors.append(copy[nei.val])
                    if nei.val not in seen:
                        dfs(nei, seen)

        dfs(node, set())
        return copy[1]


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """This is the old solution from myself back in 2020-10-20. It uses
        the copy dict as the seen set. The trick is to not create new clones
        during the neighbor iteration process.
        """
        if not node:
            return None
        copy = {}
        
        def dfs(node) -> None:
            if node:
                copy[node.val] = Node(val=node.val)
                for nei in node.neighbors:
                    if nei.val not in copy:
                        dfs(nei)
                    copy[node.val].neighbors.append(copy[nei.val])

        dfs(node)
        return copy[1]


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
