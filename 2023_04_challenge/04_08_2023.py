# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """LeetCode 133

        Got a bit confused in the middle of it. Didn't realize that we have to
        set up a cache for nodes already created.

        O(N), 35 ms, faster than 89.00%
        """
        visited = {}

        def dfs(node):
            if node and node.val not in visited:
                new_n = Node(val=node.val)
                visited[node.val] = new_n
                for nn in node.neighbors:
                    new_nn = visited.get(nn.val, dfs(nn))
                    new_n.neighbors.append(new_nn)
                return new_n
            return None

        return dfs(node)
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
