# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def jump(self, nums: List[int]) -> int:
        """LeetCode 45

        Standard DP problem. We use a dp array to record the min number of
        jumps needed to reach the end from each position. We go from right to
        left. For each new position, we loop through all possible end points
        that is reachable from the current position, and pick the min jumps
        among them.

        O(N^2), 36 ms, 33% ranking.
        """
        N = len(nums)
        dp = [1001] * N
        dp[-1] = 0
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, N)):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]


class Solution2:
    def jump(self, nums: List[int]) -> int:
        """BFS with a single pass. Reference:
        https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
        """
        res, N = 0, len(nums)
        next_end, cur_end = 0, 0
        for i in range(N - 1):  # this is the tricky part. Do not include last pos
            next_end = max(next_end, i + nums[i])
            if next_end >= N - 1:
                return res + 1
            if i >= cur_end:
                res += 1
                cur_end = next_end
        return res


sol = Solution2()
tests = [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
    ([0], 0)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.jump(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
