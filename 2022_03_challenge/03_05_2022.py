# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """LeetCode 740

        DP for the win. Two tricks. First is to use a counter and realize that
        repeated numbers doesn't matter, because they can always be taken
        without harming the other copies. Once duplicated numbers are delt with
        we have the second step, which is to sort the unique values. Then, we
        arrive at the final step, which is DP. The idea is that if the current
        value is 2 or more larger than the one in front, then removing the
        current or removing any of the numbers in front will not have any
        effect. Thus, the max value is simply adding the current value times
        its frequency. If the current value is one larger than the one in front,
        then we need to make a choice. Either remove the current, which will
        also remove the one in front, so our result is the value obtained from
        removing the current and the max value of removing every number until
        two numbers in front. Or, we do not remove the current, and we also
        know that the current will be removed when the number in front is
        removed. Thus, in this case, the value is the same as the max value
        up till the number in front.

        O(NlogN), 85 ms, 52% ranking.
        """
        counter = Counter(nums)
        sn = sorted(counter)
        dp = [0] * len(sn)
        dp[0] = sn[0] * counter[sn[0]]
        for i in range(1, len(sn)):
            if sn[i] - sn[i - 1] > 1:
                dp[i] = dp[i - 1] + sn[i] * counter[sn[i]]
            else:
                dp[i] = max(
                    sn[i] * counter[sn[i]] + dp[i - 2] * (i > 1),
                    dp[i - 1],
                )
        return dp[-1]


class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """Space optimized

        67 ms, 74% ranking.
        """
        counter = Counter(nums)
        sn = sorted(counter)
        two_back, one_back = 0, sn[0] * counter[sn[0]]
        for i in range(1, len(sn)):
            if sn[i] - sn[i - 1] > 1:
                two_back, one_back = one_back, one_back + sn[i] * counter[sn[i]]
            else:
                two_back, one_back = one_back, max(
                    sn[i] * counter[sn[i]] + two_back,
                    one_back,
                )
        return one_back
        

sol = Solution2()
tests = [
    ([3, 4, 2], 6),
    ([2, 2, 3, 3, 3, 4], 9),
    ([2], 2),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.deleteAndEarn(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
