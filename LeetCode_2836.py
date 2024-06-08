# from pudb import set_trace; set_trace()
from typing import List, Deque, Tuple
import math
from collections import defaultdict, deque


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        """
        Not able to solve this problem on my own. The following is implementation
        of all SIX hints.

        lr is the last receiver, where lr[i][j] = the index of the last receiver
        when we start from i and proceed for 2^j steps

        s is the sum, where s[i][j] = the sum of all the indices when we start
        from i and proceed for 2^j steps

        We use the DP relationship to populate the lr and s matrices.

        To find the answer, we break down k into its binary representation.
        And starting from the least significant bit, if the j0th bit is 1, we go
        from some starting point and proceed 2^j0 steps. The s matrix allows us
        to find the sum of all the indices along the way, and the lr matric
        allows us to find the last receiver of the current round. Then for the
        next j1th bit which is 1, we start from the previous last receiver and
        proceed for 2^j1 steps. So on and so forth. We can compute the total
        score of going from some starting point and proceed for k steps.

        We go through this process for each index in receiver, and return the
        max score.

        O(Mlog(K)), where M = len(receiver), 5826 ms, faster than 44.87%
        """
        bink_rev = bin(k)[2:][::-1]
        M, N = len(receiver), len(bink_rev)
        lr = [[0] * N for _ in range(M)]  # last receiver
        s = [[0] * N for _ in range(M)]  # sum
        # Populate the last receiver matrix
        for i in range(M):
            lr[i][0] = receiver[i]
        for j in range(1, N):
            for i in range(M):
                lr[i][j] = lr[lr[i][j - 1]][j - 1]
        # Populate the sum matrix
        for i in range(M):
            s[i][0] = receiver[i]
        for j in range(1, N):
            for i in range(M):
                s[i][j] = s[i][j - 1] + s[lr[i][j - 1]][j - 1]
        pos = [i for i in range(N) if bink_rev[i] == "1"]
        res = 0
        for st in range(M):
            # compute the score of starting from st and go k steps
            # pr is the previous receiver
            cur = pr = st
            for p in pos:
                cur += s[pr][p]
                pr = lr[pr][p]
            res = max(res, cur)
        return res


sol = Solution()
tests = [
    ([1, 1, 1, 2, 3], 3, 10),
]

for i, (receiver, k, ans) in enumerate(tests):
    res = sol.getMaxFunctionValue(receiver, k)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
