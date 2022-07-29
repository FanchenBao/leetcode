# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution1:
    def totalStrength(self, strength: List[int]) -> int:
        """O(N^2), TLE
        """
        dp = {strength[0]: [1, strength[0]]}
        res = strength[0] * strength[0]
        for i in range(1, len(strength)):
            cur = strength[i]
            tmp = {cur: [1, cur]}
            for k, v in dp.items():
                if k >= cur:
                    tmp[cur][0] += v[0]
                    tmp[cur][1] += v[1] + v[0] * cur
                else:
                    tmp[k] = [v[0], v[1] + v[0] * cur]
            dp = tmp
            for k, v in dp.items():
                res += k * v[1]
        return res


class Solution2:
    def totalStrength(self, strength: List[int]) -> int:
        """Step 1: build a prefix sum that allows us to compute the sum of all
        subarrays in range (i, j) that ends in strength[i] in O(1) time. To do
        so go from right to left to build a prefix sum, which is called psum1
        in the solution.

        Step 2: build a regular prefix sum such that we can compute the sum of
        range (i, j) in O(1). This is psum2.

        With psum1 and psum2, the sum of all the subarrays in (i, j) ending in
        strenght[i] can be expressed as:

        psum1[i] - psum[j + 1] - (psum2[-1] - psum[j]) * (j - i + 1)

        Step 3: we use a dp array to keep track of the contribution from
        strength[i] that counts all the subarrays that end in strength[i]. We
        can compute dp[i] from dp[i - 1] and a monotonic array.

        For instance, let's say we have a monotonic array:

            ..a0....a1...a2...

        where a0 < a1 < a2. Now we have a3 coming in. It first pops everything
        out until a2. All the elements between a3 and a2 can be computed using
        the method in Step 1 and 2 to find their contribution based on a3.

        Now, with a2, we know

            dp[2] = a2 * (s1 + s2 + ...) + a1 * (s4 + s5 + ...) + a0 * (s6 + s7 + ...)

        where s1, s2, ... are subarrays ending in a2, a1, and a0.

        Let's also assume that the subarray between a2 and a3 (ending in a3)
        has the sum s (this can be computed from psum2 in O(1)), then we can
        write dp[3] = a2 * (s1 + s + s2 + s + ...) + a1 * (s4 + s + s5 + s + ...) + a0 * (s6 + s + s7 + s + ...)
        = a2 * (s1 + s2 + ...) + a2 * c2 * s + a1 * (s4 + s5 + ...) + a1 * c1 * s + a0 * (s6 + s7 + ...) + a0 * c0 * s
        = dp[2] + s * (a2 * c2 + a1 * c1 + a0 * c0 + ...)

        Thus, we just need to use yet another prefix sum to keep track the
        value of a2 * c2 + a1 * c1 + a0 * c0 + ... And this can be done in each
        element of the monotonic array.

        O(N) with 5 passes. 2891 ms, faster than 25.58%
        """
        N = len(strength)
        psum1 = [0] * N
        psum1[-1] = strength[-1]
        ps = strength[-1]
        for i in range(N - 2, -1, -1):
            ps += strength[i]
            psum1[i] = psum1[i + 1] + ps
        psum2 = list(accumulate(strength))
        stack = [[-1, 0]]  # [index, presum of count * val]
        dp = [0] * N
        for i in range(N):
            while stack[-1][0] >= 0 and strength[i] <= strength[stack[-1][0]]:
                stack.pop()
            # handle all the elements in between the current strength and the
            # largest strength that is smaller than it
            s_between = psum1[stack[-1][0] + 1] - (psum1[i + 1] if i + 1 < N else 0) - (psum2[-1] - psum2[i]) * (i - stack[-1][0])
            dp[i] += s_between * strength[i]
            if stack[-1][0] >= 0:
                dp[i] += dp[stack[-1][0]] + (psum2[i] - psum2[stack[-1][0]]) * stack[-1][1]
            stack.append([i, stack[-1][1] + (i - stack[-1][0]) * strength[i]])
        return sum(dp) % 1000000007


class Solution3:
    def totalStrength(self, strength: List[int]) -> int:
        """Combination of lee215's method and mine.

        Ref: https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2061985/JavaC%2B%2BPython-One-Pass-Solution

        He uses two monotonic stack to find a range where all the subarrays in
        the range has the current element as the smallest value. Thus, the
        problem becomes finding the sum of all the subarrays in this range that
        includes the current value. Then my method comes in to solve this
        problem, which to me is much easier to reason with than his.
        """
        A = strength
        n = len(A)
        psum1 = list(accumulate(accumulate(A[::-1])))[::-1]
        psum2 = list(accumulate(A))
        
        # next small on the right. This bound is tight, does not count equals
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] >= A[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left. This bound is loose, extending beyond equals
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                left[stack.pop()] = i
            stack.append(i)
        # the reason for different tightness on bound is that we still think of
        # subarray as all the subarrays ending at A[i]. Thus, we want a tight
        # bound on the right, but loose bound on the left.
        res = 0
        for i in range(n):
            l, r = left[i], right[i]
            # sum all subarray ending at A[i] that starts between A[l + 1] and A[i]
            l_sum = psum1[min(l + 1, n - 1)] - (psum1[i + 1] if i + 1 < n else 0) - (psum2[-1] - psum2[i]) * (i - l)
            # sum all subarray ending at A[r - 1] that also includes A[i]
            r_strip = (psum2[r - 1] - psum2[i]) * (i - l)
            r_sum = (l_sum + r_strip) if r_strip else 0
            res += A[i] * (l_sum + r_sum)
        return res % 1000000007




sol = Solution3()
tests = [
    ([1,3,1,2], 44),
    ([5,4,6], 213),
    ([13,13,12,12,13,12], 8441),
    ([1, 2, 3, 4], 98),
]

for i, (strength, ans) in enumerate(tests):
    res = sol.totalStrength(strength)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
