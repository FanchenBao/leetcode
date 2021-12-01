# from pudb import set_trace; set_trace()
from typing import List
from collections import namedtuple


class Solution1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """LeetCode 85

        This is one is pretty bad. I knew it had to be DP. And I also realized
        that for each dp[i][j], I needed to record the max reach vertically and
        horizontally. What I lacked was the realization of the procedure that
        computed the max area. I had an idea very close to this solution, but
        I dismissed it for being too slow. In reality, it does take
        O(MN * min(MN)) for the current solution.

        I did check my solution two years ago.

        460 ms, 17% ranking.
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        Ele = namedtuple('Ele', 'w,h')
        dp = [[Ele(0, 0)] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                w, h = 1, 1
                if i > 0:
                    h += dp[i - 1][j].h
                if j > 0:
                    w += dp[i][j - 1].w
                dp[i][j] = Ele(w, h)
                width = n
                for height in range(1, h + 1):
                    width = min(width, dp[i - height + 1][j].w)
                    res = max(res, height * width)
        return res


class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """This is the faster solution also from my previous attempt more than
        2 years ago.

        The idea is for each row, we find the max vertical reach at each
        cell. Then we find the max range to the left and right of the cell that
        also has the same max vertical reach. We can compute this rectangle's
        area easily. It's easy to find the max vertical reach at each cell. It
        is tricky to find the left and right boundaries that also have the same
        max vertical reach. To find the boundaries, we use DP. The key is to
        ask the left and right boundaries of the cell above the current cell.
        Since we are asking the cells right above us, we are essentially
        computing the max left and right boundaries that support the max
        vertical reach.
            
        This runs in O(MN)

        228 ms, 52% ranking.
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, right, height = [-1] * n, [n] * n, [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            cur_bound = 0
            for j in range(n):
                if matrix[i][j] == '0':
                    cur_bound = j + 1
                    left[j] = -1
                else:
                    if j > 0 and if matrix[i][j - 1] == '1':
                        # look for left bound of the cell above me
                        left[j] = max(left[j], cur_bound)
                    else:
                        left[j] = cur_bound
            cur_bound = n - 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '0':
                    cur_bound = j - 1
                    right[j] = n
                else:
                    if j < n and if matrix[i][j + 1] == '1':
                        # look for right bound of the cell above me
                        right[j] = min(right[j], cur_bound)
                    else:
                        right[j] = cur_bound
            for j in range(n):
                res = max(res, height[j] * (right[j] - left[j] + 1))
        return res


class Solution3:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """This solution comes from
        https://leetcode.com/problems/maximal-rectangle/discuss/1603766/Python-O(mn)-solution-explained

        It is hte same idea as Solution2, but uses the monotonic stack to handle
        the computation of rectangles for each row. In fact, this computation
        process is exactly the same as problem 84 where we have to find the
        maximum rectangle across a histogram. For each row, we can compute the
        height of each cell, i.e. obtain a histogram. Then we use a monotonic
        stack to process each hight. If the new hight is smaller than the top of
        the stack, we pop the stack. Let's call it H. After the pop, the current
        top of stack is the first height that is smaller than H to the left of
        H. In other words, if there exist other heights between current top of
        stack and H, they must all be larger than H (this is true because should
        these in-between heights exist, H must have popped them when it first
        shows up). Also, if there exist any heights between H and the current
        height, they must also be heigher than H. Thus, in any case, the
        histograms from current top of the stack to the current height must all
        be larger or equal to H. This is the width of the rectangle with the
        height H.

        O(MN), 200 ms, 79% ranking.
        """

        def histogram(heights: List[int]) -> int:
            """Find the rectangle with max area over a histogram of heights"""
            stack, res = [], 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] >= h:
                    H = heights[stack.pop()]
                    W = i - stack[-1] - 1 if stack else i
                    res = max(res, H * W)
                stack.append(i)
            return res

        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for row in matrix:
            for j in range(n):
                heights[j] = 0 if row[j] == '0' else heights[j] + 1
            res = max(res, histogram(heights))
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
