# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce


class Solution1:
    def optimalDivision(self, nums: List[int]) -> str:
        """This problem is a bit harder than a typical medium problem, because
        it involves two subproblems. One is the DP solution to find the optimal
        ways of putting parenthesis. Two is actually putting the parenthesis
        in the expression. The first problem is quite straightforward DP, where
        we consider two situations for each newly added number. Either the
        new number does not group with anyone; in this case the value is the
        dp[i - 1] / nums[i]. Or the new number groups with nums[i - 1],
        nums[i - 2], ..., or nums[0], which produces other possible values. We
        pick the max among them as the max value produced uptil i.

        In addition to save the max value, we also save the position where a
        left parenthesis must be added to allow the current grouping. The
        tricky is that during reconstruction of the expression, we cannot
        create a second left parenthesis if a number already has a left paren-
        thesis. This is because when a number already has a left paren, it is
        at the beginning of the operation contained within the paren. Hence,
        adding more left paren to the beginning of an expression is useless.

        O(N^2), 50 ms, 37% ranking. Also notice that I use a cumulative product
        to speed up the computation of the product of multiple numbers.
        """
        N = len(nums)
        if N == 1:
            return str(nums[0])
        if N == 2:
            return str(nums[0]) + '/' + str(nums[1])
        dp = [(nums[0], 0), (nums[0] / nums[1], 0)]
        cumprod = [nums[0], nums[0] * nums[1]]
        for i in range(2, N):
            cumprod.append(cumprod[-1] * nums[i])
            dp.append((dp[i - 1][0] / nums[i], 0))
            for j in range(i - 1, 0, -1):
                cur = dp[j - 1][0] / nums[j] * cumprod[i] / cumprod[j]
                if cur > dp[i][0]:
                    dp[i] = (cur, j)
        strnums = [str(n) for n in nums]
        strnums[0] = '(' + strnums[0]
        for i in range(N - 1, -1, -1):
            if strnums[dp[i][1]][0] != '(':
                strnums[dp[i][1]] = '(' + strnums[dp[i][1]]
                strnums[i] += ')'
        strnums[0] = strnums[0][1:]
        return '/'.join(strnums)


class Solution2:
    def optimalDivision(self, nums: List[int]) -> str:
        """Use reduce instead of cumulative product. See if this one gives
        better performance.
        """
        N = len(nums)
        if N == 1:
            return str(nums[0])
        if N == 2:
            return str(nums[0]) + '/' + str(nums[1])
        dp = [(nums[0], 0), (nums[0] / nums[1], 0)]
        for i in range(2, N):
            dp.append((dp[i - 1][0] / nums[i], 0))
            for j in range(i - 1, 0, -1):
                cur = dp[j - 1][0] / reduce(lambda pre, cur: pre / cur, nums[j:i + 1])
                if cur > dp[i][0]:
                    dp[i] = (cur, j)
        strnums = [str(n) for n in nums]
        strnums[0] = '(' + strnums[0]
        for i in range(N - 1, -1, -1):
            if strnums[dp[i][1]][0] != '(':
                strnums[dp[i][1]] = '(' + strnums[dp[i][1]]
                strnums[i] += ')'
        strnums[0] = strnums[0][1:]
        return '/'.join(strnums)


class Solution3:
    def optimalDivision(self, nums: List[int]) -> str:
        """This is my interpretation of the math solution in the official
        solution.

        We want to maximize 'a/b/c/d/...'. This is equivalent to minimize
        'b/c/d/...'. Since all numbers are larger than 1, any addition of
        paren in 'b/c/d...' would result in some values being multiplied once
        the paren is removed. Multiplying a number larger than 1 is always 
        larger than dividing the same value. Thus, the min 'b/c/d/...' can
        achieve is to not add any paren in this sequence. Therefore, the
        solution is always 'a/(b/c/d/...)'.

        O(N), 36 ms, 76% ranking.
        """
        N = len(nums)
        if N == 1:
            return str(nums[0])
        if N == 2:
            return str(nums[0]) + '/' + str(nums[1])
        strnums = [str(n) for n in nums]
        strnums[1] = '(' + strnums[1]
        strnums[-1] += ')'
        return '/'.join(strnums)



sol = Solution3()
tests = [
    ([1000,100,10,2], "1000/(100/10/2)"),
    ([2,3,4], "2/(3/4)"),
    ([2], "2"),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.optimalDivision(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
