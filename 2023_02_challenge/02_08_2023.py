# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def jump(self, nums: List[int]) -> int:
        """LeetCode 45

        I don't like this. This is O(MN) where N = len(nums), M = max(nums).
        It's DP but very poorly.

        6516 ms, faster than 23.01%
        """
        N = len(nums)
        dp = [math.inf] * N
        dp[-1] = 0
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, N)):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]


class Solution2:
    def jump(self, nums: List[int]) -> int:
        """BFS

        O(NM), 4224 ms, faster than 28.43%
        """
        N = len(nums)
        queue = set([0])
        visited = set()
        steps = 0
        while queue:
            tmp = set()
            for i in queue:
                if i == N - 1:
                    return steps
                visited.add(i)
                for nex in range(i + 1, min(i + nums[i] + 1, N)):
                    if nex not in visited:
                        tmp.add(nex)
            queue = tmp
            steps += 1


class Solution3:
    def jump(self, nums: List[int]) -> int:
        """1-pass BFS

        The idea is to find the max reach from nums[0]. Then as we iterate from
        0 + 1 to 0 + nums[0], we are always on the same level. We update the
        max reach. When we go beyond 0 + nums[0], we are at the second level.
        Keep doing this until the first time that max reach goes beyond len(nums)

        O(N), 126 ms, faster than 90.62%
        """
        N = len(nums)
        if N == 1:
            return 0
        steps = 0
        max_reach = cur_level_end = 0
        for i in range(N):
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= N - 1:
                return steps + 1
            if i >= cur_level_end:
                # finish traversing the current level, update the level end for
                # the next level
                cur_level_end = max_reach
                steps += 1


sol = Solution3()
tests = [
    ([2,3,1,1,4], 2),
    ([2,3,0,1,4], 2),
    ([0], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.jump(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
