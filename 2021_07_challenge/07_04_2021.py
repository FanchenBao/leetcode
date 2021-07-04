# from pudb import set_trace; set_trace()
from typing import List
import numpy as np


class Solution1:
    def countVowelPermutation(self, n: int) -> int:
        """LeetCode 1220

        Very basic DP bottom up solution. We compute the total number of
        strings that can be constructed starting with each vowel for a given
        length. Then, to compute for the next length, we follow the rules. We
        do this until reaching length n, which gives us the total number of
        strings with length n that starts with each vowel. Sum them up and we
        have the solution.

        O(N), 840 ms, 13% ranking.
        """
        dp = [1] * 5  # a, e, i, o, u
        rules = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        for _ in range(n - 1):
            temp = []
            for j in range(5):
                temp.append(sum(dp[k] for k in rules[j]))
            dp = temp
        return sum(dp) % 1000000007


class Solution2:
    def countVowelPermutation(self, n: int) -> int:
        """Try to make it faster

        324 ms, 48% ranking.
        """
        dp = [1] * 5  # a, e, i, o, u
        for _ in range(n - 1):
            dp = [
                dp[1],
                dp[0] + dp[2],
                sum(dp) - dp[2],
                dp[2] + dp[4],
                dp[0]
            ]
        return sum(dp) % 1000000007


class Solution3:
    def countVowelPermutation(self, n: int) -> int:
        """Matrix power

        A couple of things. First, naively using np.linalg.matrix_power does not
        work because the intermediate integer overflows. Hence, we have to
        write our own power function with modulo built in it.

        Second, we have to cast to int before return.

        Third, strictly speaking, after we obtain the powered rule, we need to
        matmul the initial value of [1, 1, 1, 1, 1] as a column. Then we take
        the sum of each element in the product. However, this is not necessary,
        because it is equivalent to getting the sum of the powered rule itself.

        92 ms, 98% ranking. O(logN) due to the matrix power operation.
        """
        rule = np.array([
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0],
        ])

        modulo = 1000000007

        def power(mat, modulo, p):
            res = np.eye(mat.shape[0], dtype=int)
            while p:
                if p % 2:
                    res = (res @ mat) % modulo
                mat = (mat @ mat) % modulo
                p >>= 1
            return res

        return int(np.sum(power(rule, modulo, n - 1)) % modulo)


sol2 = Solution2()
sol = Solution3()
# tests = [
#     (1, 5),
#     (2, 10),
#     (5, 68),
# ]

# for i, (n, ans) in enumerate(tests):
#     res = sol.countVowelPermutation(n)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')

for n in range(1, 50):
    ans = sol2.countVowelPermutation(n)
    res = sol.countVowelPermutation(n)
    if res != ans:
        print(f'Fail. Ans: {ans}, Res: {res}, {n=}')
