# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """LeetCode 1306

        DFS with backtracking and caching.

        O(N), 452 ms, 13% ranking.

        UPDATE: I checked my solution a year ago, and udpated the current
        solution. The main difference is that the checking for the validity of
        an index happens when dfs() is called on this index. Previously, we
        made the check before calling dfs().

        With this update, we hit 341 ms, 28% ranking.
        """
        N = len(arr)
        
        @lru_cache(maxsize=None)
        def dfs(idx: int) -> bool:
            if 0 <= idx < N and arr[idx] >= 0:
                if arr[idx] == 0:
                    return True
                temp = arr[idx]
                arr[idx] = -1
                res = dfs(idx + temp) or dfs(idx - temp)
                arr[idx] = temp
                return res
            return False

        return dfs(start)


sol = Solution()
tests = [
    ([4,2,3,0,3,1,2], 5, True),
    ([4,2,3,0,3,1,2], 0, True),
    ([3,0,2,1,2], 2, False),
]

for i, (arr, start, ans) in enumerate(tests):
    res = sol.canReach(arr, start)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
