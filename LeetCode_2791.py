# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution1:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        """
        Boy is this a good problem with fairly complicated implementation.

        First, we need to have the bitmask insight, which luckily I do.

        Second, we need to figure out the trick of using XOR for all the paths
        ending at each node. This I did not come up with.

        Then we need to use topologicla sort-based BFS. This I realized after
        going through a failed case.

        O(N), 2836 ms, faster than 44.44% 
        """
        N = len(parent)
        adj = defaultdict(list)
        num_children = [0] * N
        for i in range(1, N):
            adj[parent[i]].append((i, s[i]))
            num_children[parent[i]] += 1
        
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
                    # consider path from root 0 to i
                    res += 1
                path_counter[cur] -= 1  # do not double count the current path
                num_children[parent[i]] -= 1
                for ap in allowed_parities:
                    res += max(0, path_counter[ap ^ cur])
                if parent[i] != 0 and num_children[parent[i]] == 0:
                    tmp.add(parent[i])
            queue = tmp
        return res


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        """
        This solution is inspired by https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/discuss/3804246/Simple-DFS-solution-in-C%2B%2B-java-and-python

        The general idea is the same as Solution1, but we only need to do one
        round of DFS. As we perform DFS, we also keep track of the counter of
        all the bitmasks, and count the number of palindrome paths ending at
        each node.

        The beauty of counting while DFS is that we can easily avoid duplicates
        because the paths are created gradually, which means an earlier path
        never has access to a later path to even offer the opportunity for
        duplcation.

        O(N) 1709 ms, faster than 87.81% 
        """
        adj = defaultdict(list)
        N = len(parent)
        for i in range(1, N):
            adj[parent[i]].append(i)
        path_counter = Counter()
        path_counter[0] = 1  # this allows the detection of palindrome path from root to a node
        allowed_parities = [(1 << i) for i in range(26)]
        allowed_parities.append(0)

        def dfs(node: int, path: int) -> int:
            res = 0
            if node:
                path ^= (1 << (ord(s[node]) - 97))
                for ap in allowed_parities:
                    res += path_counter[path ^ ap]
                path_counter[path] += 1
            for child in adj[node]:
                res += dfs(child, path)
            return res

        return dfs(0, 0)





sol = Solution()
tests = [
    ([-1,0,0,1,1,2], 'acaabc', 8),
    ([-1,0], 'pi', 1),
    ([-1,2,6,2,5,2,7,0], "pipfippl", 15),
]

for i, (parent, s, ans) in enumerate(tests):
    res = sol.countPalindromePaths(parent, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
