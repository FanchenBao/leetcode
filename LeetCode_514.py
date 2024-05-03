# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
import heapq


class Solution1:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        O(M^2N). DP(ri, ki) is the number of steps to reach the end of key
        when the current indices on ring and key are ri and ki.

        537 ms, faster than 10.84%
        """
        M = len(ring)
        N = len(key)
        MAX = 1000000000

        @lru_cache(maxsize=None)
        def solve(ri: int, ki: int) -> int:
            if ki == N:
                return 0
            res = MAX
            for i, r in enumerate(ring):
                steps = min((i - ri + M) % M, (ri - i + M) % M)
                if r == key[ki]:
                    res = min(res, steps + 1 + solve(i, ki + 1))
            return res

        return solve(0, 0)


class Solution2:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        This is also from the official solution. It uses a Dijkstra-ish method

        Each node is a tuple of (ri, ki). Then we Dijkstra this.

        544 ms, faster than 10.79%
        """
        M = len(ring)
        N = len(key)
        MAX = 1000000000
        min_steps = [[MAX] * (N + 1) for _ in range(M)]
        queue = [(0, 0, 0)]  # (step, ri, ki)
        while queue:
            steps, ri, ki = heapq.heappop(queue)
            if steps > min_steps[ri][ki]:
                continue
            if ki == N:
                return steps
            for i, r in enumerate(ring):
                cur = min((i - ri + M) % M, (ri - i + M) % M)
                if ki < N and r == key[ki]:
                    next_step = steps + cur + 1
                    if next_step < min_steps[i][ki + 1]:
                        min_steps[i][ki + 1] = next_step
                        heapq.heappush(queue, (next_step, i, ki + 1))
        return -1


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
