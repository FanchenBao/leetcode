# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """LeetCode 413

        A straightforward sliding window technique. We start with a left and
        right indices. Left at 0, right at 2. We have a dif standard at A[1] -
        A[0]. We are going to compare A[right] - A[right - 1]. If it is equal
        to the dif, then we can expand the arithmetic slice by incrementing
        right. If not, we have found the maximum length of the current
        arithmetic slice, and its size is right - left. We can compute the total
        number of arithmetic slices with size larger or equal to 3 with a
        formula like this:

        supose the length of the maximum arithmetic slice is n, we have the
        total number of slices equal to 1 + 2 + ... + n - 4 + 1 + n - 3 + 1
        = 1 + 2 + ... + n - 3 + n - 2 = (n - 2)(n - 1) / 2

        Therefore, once we found a maximum arithmetic slice, we can immediately
        compute the total number of legal slices contained within. We keep
        moving the sliding window until we hit the end.

        O(N), 36 ms, 77% ranking.

        UPDATE: the solution also provides an algo similar to this one. But
        instead of an obvious use of sliding window, it simply iterates and
        count the number of elements that are in a longest arithmetic slice, and
        use a formula similar to ours to compute the total number of slices
        within the longest arithmetic slice.
        """
        res, N = 0, len(A)
        if N < 3:
            return 0
        left, right = 0, 2
        dif = A[1] - A[0]
        while right < N:
            if A[right] - A[right - 1] != dif:
                res += (right - left - 1) * (right - left - 2) // 2
                left = right - 1
                dif = A[right] - A[left]
            right += 1
        return res + (right - left - 1) * (right - left - 2) // 2


class Solution2:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """This is dynamic programming from the solution. It is pretty smart.
        The idea is that for each element i, if i - 2, i - 1, and i form an
        arithmetic slice, then the total number of arithmetic
        slices that ends in i is equal to total number of arithmetic slices that
        ends in i - 1 plus one. Think about this. If this makes to you, move on.

        Then the problem is a very straightforward DP. We start from position 2,
        and continue one by one until we reach the end. The only trick is when
        i - 2, i - 1, and i cannot form an arithmetic slice, that's when we need
        to reset the DP value before moving on.

        O(N)
        """
        res, pre = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                pre += 1
                res += pre
            else:
                pre = 0
        return res


class Solution3:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """Smart use of groupby to easily acquire the length of longest
        arithmetic slice. Notice also the use of the walrus operator.

        reference: https://leetcode.com/problems/arithmetic-slices/discuss/1071074/Python-Oneliner-using-groupby-explained/853344
        """
        return sum((n := len(list(g))) * (n - 1) // 2 for _, g in groupby(b - a for a, b in zip(A, A[1:])))


sol = Solution3()
tests = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 36),
    ([1, 2], 0),
    ([1, 2, 3], 1),
    ([1, 2, 3, 4, 6, 7, 8, 9], 6),
    ([1, 2, 3, 4, 6, 8, 10, 11, 12, 17, 19, 21], 8)
]

for i, (A, ans) in enumerate(tests):
    res = sol.numberOfArithmeticSlices(A)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
