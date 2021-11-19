# from pudb import set_trace; set_trace()
from typing import List, Set
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """I went through quite a few iterations on this. The final solution is
        much simpler than the one envisioned initially. The idea is to build
        graphs based on prerequisites, and then check whether any graph contains
        loop. If loop exists, it's impossible to take all the classes.

        Initially, I created another class to represent each node in the graph.
        But later on I realized that this is not necessary, because the node
        value is the same as the index I assign for each node. Thus, all nodes
        can be represented by a list of list (i.e. each element list is the node
        ). Furthermore, we can use DP caching to simplify the logic of checking
        loops. DP[i] represents whether there is a loop if we start from
        nodes[i]. We also keep a set of all posible roots. We will go through
        each potential root and if any one leads to a loop, it's impossible to
        take all the classes.

        """
        root_indices = set()
        nodes = defaultdict(list)
        dp = defaultdict(lambda: None)

        def check_loop(idx: int, path: Set[int]) -> bool:
            if dp[idx] is None:
                if idx in path:
                    dp[idx] = False
                else:
                    path.add(idx)
                    for ci in nodes[idx]:
                        if not check_loop(ci, path):
                            dp[idx] = False
                            break
                    else:
                        dp[idx] = True
                    path.remove(idx)
            return dp[idx]

        for a, b in prerequisites:
            root_indices.add(b)
            nodes[b].append(a)
        return all(check_loop(ri, set()) for ri in root_indices)


sol = Solution()
tests = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (2, [[0, 0], [1, 1]], False),
    (4, [[0, 1], [2, 3]], True),
    (5, [[1, 0], [3, 0], [2, 1], [4, 3], [2, 4]], True),
    (5, [[1, 0], [3, 0], [2, 1], [4, 3], [1, 4]], True),
    (5, [[1, 0], [3, 0], [2, 1], [4, 3], [0, 4]], False),
    (20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]], False),
    (1, [], True),
]

for i, (numCourses, prerequisites, ans) in enumerate(tests):
    res = sol.canFinish(numCourses, prerequisites)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
