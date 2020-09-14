# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
        """Standard DP, pass OJ"""
        if not nums:
            return 0
        max_rob = [0] * (len(nums) + 1)
        house_robbed = [0] * (len(nums) + 1)
        max_rob[1] = nums[0]
        house_robbed[1] = 1
        for i in range(1, len(nums)):  # index tracing nums
            if not house_robbed[i]:
                max_rob[i + 1] = max_rob[i] + nums[i]
                house_robbed[i + 1] = 1
            elif max_rob[i - 1] + nums[i] > max_rob[i]:
                max_rob[i + 1] = max_rob[i - 1] + nums[i]
                house_robbed[i + 1] = 1
            else:
                max_rob[i + 1] = max_rob[i]
        return max_rob[len(nums)]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """Space-efficient DP"""
        if not nums:
            return 0
        pp_rob, p_rob = 0, nums[0]
        p_robbed = True
        for n in nums[1:]:
            if not p_robbed:
                pp_rob, p_rob = p_rob, p_rob + n
                p_robbed = True
            elif pp_rob + n > p_rob:
                pp_rob, p_rob = p_rob, pp_rob + n
                p_robbed = True
            else:
                pp_rob, p_rob = p_rob, p_rob
                p_robbed = False
        return p_rob


class Solution3:
    def rob(self, nums: List[int]) -> int:
        """Best DP"""
        pp_rob, p_rob = 0, 0
        for n in nums:
            # only two situations for n. Either we rob n, in which case we take
            # pp_prob + n as the current gain; or we don't rob n, in which case
            # we take p_rob as the current gain.
            pp_rob, p_rob = p_rob, max(p_rob, pp_rob + n)
        return p_rob


sol = Solution3()
tests = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.rob(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
