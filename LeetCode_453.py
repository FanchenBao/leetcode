# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def minMoves(self, nums: List[int]) -> int:
        """The idea is greedy.

        We always want to match the second biggest value to the biggest value.
        Because, if we match the second biggest value to any other value, that
        would always cause more moves.

        Say the biggest value is x and the second biggest value is y, and there
        are n biggest values. Then it can be shown that the min moves needed
        to make all the xs and ys the same value (not necessarily x, but
        something bigger) is n * (x - y). After this, we will have n + 1
        biggest value z. We repeat the same procedure with the current second
        biggest value, until all the numbers converge to the same value.

        O(NlogN), 490 ms, 5% ranking.
        """
        counter = Counter(nums)
        su = sorted(counter, reverse=True)  # sorted uniques
        psum = counter[su[0]]  # the number of the biggest values at the moment
        res = 0
        for i in range(1, len(su)):
            res += psum * (su[i - 1] - su[i])
            psum += counter[su[i]]
        return res


class Solution2:
    def minMoves(self, nums: List[int]) -> int:
        """Math solution

        Ref: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93817/It-is-a-math-question

        Suppose after minMoves all the numbers in nums reaches x. Since each
        move add n - 1 to the total sum of nums (n is the length of nums), we
        have

        minMoves * (n - 1) = x * n - sum(nums)

        And since we always have to move the smallest value at each move, we
        have

        x = minMoves + min(nums)

        Thus

        minMoves * (n - 1) = (minMoves + min(nums)) * n - sum(nums)
        => minMoves = sum(nums) - min(nums) * n

        O(N), 428 ms

        A better explanation is that increment n - 1 element is equivaluent
        to decrement one element. So the problem is equivalent to decrementing
        one element at a time, how many moves are needed for all the values
        to be the same. The answer is obviously decrementing everyone towards
        min(nums).
        """
        return sum(nums) - len(nums) * min(nums)


sol = Solution2()
tests = [
    ([1, 2, 3], 3),
    ([1, 1, 1], 0),
    ([1, 2, 5], 5),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minMoves(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
