# from pudb import set_trace; set_trace()
from typing import List
from itertools import permutations


class SolutionTLE:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """TLE. But don't worry, this is expected"""
        N = len(A)
        if N <= 2:
            return True
        for d in range(2, N):
            for i in range(N - d):
                if A[i] > A[i + d]:
                    return False
        return True


class Solution1:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """LeetCode 775

        Recursion solution.

        First and most important intuition is that we return False if and only
        if there exist a global inversion that is NOT a local inversion.

        The second intuition is that if the start of the array is 2 or larger,
        then we always return False. This is because there will be at least one
        value smaller than the beginning that is in a global inversion position.

        If the first value is 0, or the first two values are 1 and 0, then we
        can proceed to check the next or the next next value, respectively.
        When we check, we can reduce that value by the number of values already
        checked, thus turning the problem into a recursive one. For instance,
        given A = [0, 2, 1], the first value is 0, which means we can proceed to
        the next value 2. However, since we have already checked one value, we
        must deduct one from 2. Therefore, when we check 2, we are actually
        looking at 2 - 1 = 1, and the next value is 1 - 1 = 0. So we are
        basically checking [1, 0], which is true. So we say [0, 2, 1] is true.

        The same applies to the 1, 0 situation, it's just that we have to deduct
        2 when checking the next value.

        O(N), 380 ms, 19% ranking.
        """
        N = len(A)

        def helper(idx: int, dec: int) -> bool:
            if idx >= N - 1:
                return True
            if A[idx] - dec > 1:
                return False
            if A[idx] - dec == 0:
                return helper(idx + 1, dec + 1)
            if A[idx] - dec == 1:
                return False if A[idx + 1] - dec != 0 else helper(idx + 2, dec + 2)

        return helper(0, 0)


class Solution2:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """Iterative

        Same solution as Solution1, but iterative.

        O(N), 364 ms, 29% ranking.
        """
        N = len(A)
        i, dec = 0, 0
        while i < N:
            if A[i] - dec > 1:
                return False
            if A[i] - dec == 0:
                dec += 1
                i += 1
                continue
            if A[i] - dec == 1:
                if i + 1 < N:
                    if A[i + 1] - dec != 0:
                        return False
                    i += 2
                    dec += 2
                else:
                    break
        return True


class Solution3:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """From lee215
        https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution

        The idea is that there exists no pair of max(A[...i]) and A[i + 2] such
        that max(A[...i]) > A[i + 2]
        """
        cur_max = 0
        for i in range(len(A) - 2):
            cur_max = max(cur_max, A[i])
            if cur_max > A[i + 2]:
                return False
        return True


class Solution4:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """From lee215
        https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution

        The idea is that for a number i, it can only be placed in positions
        A[i - 1], A[i], and A[i + 1] in order for the function to return True.

        Reason:
        * Place at A[i - 1], then the ideal situation is that the i - 2 values
        that are smaller than i is placed at A[0, ..., i - 2], and the last
        value that is smaller than i is placed at A[i].
        * Place at A[i], then the ideal situation is that all of the i - 1
        values that are smaller than i are placed at A[0, ..., i - 1]
        * Place at A[i + 1], then the ideal situation is that all of the i - 1
        values that are smaller than i are placed at A[0, ..., i - 1], and the
        value i + 1 is placed at A[i].

        Other than these three situations, the function shall return False.
        """
        return all((a - i) in {-1, 0, 1} for i, a in enumerate(A))


tle = SolutionTLE()
sol = Solution4()
inputs = permutations(range(6))
tests = [(A, tle.isIdealPermutation(A)) for A in inputs]

for i, (A, ans) in enumerate(tests):
    res = sol.isIdealPermutation(A)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
