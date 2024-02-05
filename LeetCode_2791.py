# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        N = len(parent)
        adj = defaultdict(list)
        for i in range(1, N):
            adj[parent[i]].append((i, s[i]))
        
        self.res = 0
        allowed_parities = {1 << i for i in range(26)}
        allowed_parities.add(0)
        # the bitmask representation of each path from root to a node
        path_bitmask = [0] * N
        queue = set()

        def dfs(node: int, pb: int) -> None:
            """
            To find the path bitmask

            pb is the path bitmask from root to node
            """
            path_bitmask[node] = pb
            for child, letter in adj[node]:
                dfs(child, pb ^ (1 << (ord(letter) - 97)))
            if not adj[node]:
                queue.add(node)

        dfs(0, 0)
        path_counter = Counter(path_bitmask)
        path_counter[0] -= 1  # we do not count the path from root to root
        res = 0
        # BFS from leave to root and count all possible palindrome paths
        while queue:
            tmp = set()
            for i in queue:
                cur = path_bitmask[i]
                if cur in allowed_parities:
                    res += 1
                path_counter[cur] -= 1  # do not double count the current path
                for ap in allowed_parities:
                    res += path_counter[ap ^ cur]
                if parent[i]:
                    tmp.add(parent[i])
            queue = tmp
        return res


sol = Solution()
tests = [
    # ([-1,0,0,1,1,2], 'acaabc', 8),
    # ([-1,0], 'pi', 1),
    ([-1,2,6,2,5,2,7,0], "pipfippl", 15),
]

for i, (parent, s, ans) in enumerate(tests):
    res = sol.countPalindromePaths(parent, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
