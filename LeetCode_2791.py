# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        adj = defaultdict(list)
        for i in range(1, len(parent)):
            adj[parent[i]].append((i, s[i]))
        
        self.res = 0
        allowed_parities = [1 << i for i in range(26)]
        allowed_parities.append(0)
        
        def dfs(node: int):
            """
            We will return (
                array of bitmasks from node to all the leaves in the subtree,
                array of counters where each counter's key is the bitmask of all subpaths from any child to the leaves,
            )
            """
            cur_dir_paths = []
            cur_counters = []
            for child, letter in adj[node]:
                child_dir_paths, child_counters = dfs(child)
                for i in range(len(child_dir_paths)):
                    cp = child_dir_paths[i]
                    cc = child_counters[i]
                    bitmask = cp ^ (1 << (ord(letter) - 97))
                    cur_dir_paths.append(bitmask)
                    cc[bitmask] += 1
                    cur_counters.append(cc)
            # Count the number of palindrome paths starting from node and end
            # on one of its path towards some leaf
            for i in range(len(cur_dir_paths)):
                cp = cur_dir_paths[i]
                cc = cur_counters[i]
                for pos in allowed_parities:
                    self.res += cc[pos ^ cp]
            # Count the number of palindrom paths connecting some path on one
            # subtree and some path on the other subtree














                    




sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
