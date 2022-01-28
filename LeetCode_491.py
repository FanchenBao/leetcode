# from pudb import set_trace; set_trace()
from typing import List
from itertools import chain


class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """Use DP. DP[i] is a list of non-decreasing subsequences starting with
        nums[i]. We go from right to left, thus each time a new x is being
        considered, we check each y that is to the right and grab all the
        subsequence of y when x <= y. When duplicate happens, i.e. x == y, we
        shall stop, because if we keep moving forward, it will be a repeat.

        306 ms, 46% ranking.
        """
        N = len(nums)
        dp = [[] for _ in nums]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] <= nums[j]:
                    dp[i].extend([nums[i]] + l for l in dp[j])
                if nums[i] == nums[j]:
                    break
            else:
                dp[i].append([nums[i]])
        return [l for l in chain(*dp) if len(l) > 1]


class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """Backtracking solution.

        I don't know why, but I seem to always ignore the backtracking option.

        Ref https://leetcode.com/problems/increasing-subsequences/discuss/97147/Java-solution-beats-100
        """
        res = []
        N = len(nums)

        def dfs(idx: int, subseq: List[int]) -> None:
            if len(subseq) > 1:
                res.append(subseq[:])
            seen = set()
            for i in range(idx, N):
                if nums[i] not in seen and (not subseq or nums[i] >= subseq[-1]):
                    seen.add(nums[i])
                    subseq.append(nums[i])
                    dfs(i + 1, subseq)
                    subseq.pop()  # this may return subseq to empty array

        dfs(0, [])
        return res


sol = Solution2()
tests = [
    ([4,6,7,7], [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]),
    ([4,4,3,2,1], [[4, 4]]),
    ([1], []),
    ([1,1,1,1,1,1],[[1,1,1,1,1,1],[1,1,1,1,1],[1,1,1,1],[1,1,1],[1,1]]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findSubsequences(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
