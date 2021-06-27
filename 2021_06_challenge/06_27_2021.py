# from pudb import set_trace; set_trace()
from typing import List
from collections import deque
import math


class Solution1:
    def candy(self, ratings: List[int]) -> int:
        """LeetCode 135

        I feel very lucky that we solved this problem in fairly short period
        of time. My thought process is like this. For any child, there are four
        situations for his/her rating relative to the two neighbors on the left
        and right.

        1. left > cur <= right
        2. left > cur > right
        3. left <= cur <= right
        4. left <= cur > right

        For situation 1, it is guaranteed that the current child has 1 candy,
        because his/her rating is not bigger than any of his/her neighbors. So
        1 candy suffices.

        For situation 3, current child's candy is only determined by the candy
        of the left child. It has to have one more candy than the left child.

        For situation 2, current child's candy is only determined by the candy
        of the right child. However, if we go from left to right, at the moment
        we do not know how many candies the right child has. Therefore, we need
        to run recursion on the right child. Afterwards, the current child's
        candy will be one more than the right child.

        For situation 4, current child's candy is determined by both the left
        and right children. We already know the left child, but we have to
        recurse on the right child. Afterwards, the current child's candy is one
        more than the max of the left and riht childrens candies.

        O(N), 180 ms, 33% ranking.
        """
        n = len(ratings)
        candies = [0] * n

        def helper(idx: int) -> None:
            if idx == n:
                return
            if idx == n - 1 or ratings[idx] <= ratings[idx + 1]:
                if idx == 0 or ratings[idx] <= ratings[idx - 1]:
                    candies[idx] = 1
                else:
                    candies[idx] = candies[idx - 1] + 1
                helper(idx + 1)
            else:
                helper(idx + 1)
                if idx == 0 or ratings[idx] <= ratings[idx - 1]:
                    candies[idx] = candies[idx + 1] + 1
                else:
                    candies[idx] = max(candies[idx - 1], candies[idx + 1]) + 1

        helper(0)
        return sum(candies)


class Solution2:
    def candy(self, ratings: List[int]) -> int:
        """This is the two-pass solution, going left to right to satisfy the
        left neighbor requirement, and then right to left. We use the 1D array
        version.

        Ref: https://leetcode.com/problems/candy/solution/
        """
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(
                    candies[j - 1] if j > 0 and ratings[j] > ratings[j - 1] else 0,
                    candies[j + 1],
                ) + 1
        return sum(candies)


sol = Solution1()
tests = [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([3, 2, 1], 6),
    ([1, 3, 2, 1], 7),
    ([1], 1),
    ([1, 3, 4, 5, 2], 11),
]

for i, (ratings, ans) in enumerate(tests):
    res = sol.candy(ratings)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
