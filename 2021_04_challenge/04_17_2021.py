# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """This is following lee215's solution, as shown here:
        https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum

        However, his code is cryptic. Therefore, I used DBabichev's solution to
        help me understand:
        https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/1162611/Python-cumulative-sum-%2B-dp-explained

        The idea is to fix two columns, and find all submatrices within these
        two columns that satisfy the target. To find these submatrices, we can
        consider each row as one entity. If we know the sum of that particular
        row (restricted by the two fixed columns), this problems turns into
        finding subarray that sums to the target, except here the array is
        actually a combined column. Then we use all possible combinations of
        fixing two columns, and the problem is solved. For example:

        1 2 3
        4 5 6
        7 8 9

        If we fix the first and second columns, we have

        1 2
        4 5
        7 8

        We want to find the total number of submatrices in these two columns
        that has sum to target. We then combine the two columns into one like
        this (combine means to compute the sum of each row):

        3
        9
        15

        This is a prefix sum on the combined column. Then all we need to know is
        whether a prefix sum minus the target is another prefix sum in this
        combined column.

        Apparently, we also need to use prefix sum on each row in the original
        matrix to find the sum of row demarcated by any fixed columns.

        O(MN^2) where M is the number of rows and N columns.
        988 ms, 37% ranking.
        """
        m, n = len(matrix), len(matrix[0])
        # prefix sum on all the rows
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        # for each pair of columns, find the total number of submatrices that
        # sum up to target
        res = 0
        for p in range(n):
            for q in range(p, n):
                counter = defaultdict(int)
                counter[0] = 1  # If a prefix sum is equal to target, we must count it
                # the prefix sum of the rows demarcated by columns p, q
                pre_sum = 0
                for k in range(m):
                    pre_sum += matrix[k][q] - (matrix[k][p - 1] if p > 0 else 0)
                    res += counter[pre_sum - target]
                    counter[pre_sum] += 1
        return res


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
