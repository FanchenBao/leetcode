# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def checkRecord(self, n: int) -> int:
        """LeetCode 552

        What a problem!

        We focus on two scenarios given an n. One is that there is no
        restriction on the choices of P, A, and L. We call the number of arange-
        ments in this scenario all_in.

        The other is that we cannot use A, which we name it no_a.

        We can manually construct all_in and no_a for n = 1, 2, or 3. These are
        the base cases. While doing so, we realize that using three previous
        results, we can compute the fourth result. Here is how it goes.

        To compute the new_all_in with length n (n > 3),
            * Put P in the 1st position, then the total arrangments is
            all_in[n - 1].
            * Put A in the 1st position, then the total arrangements is
            no_a[n - 1].
            * Put L in the 1st position
                * Put P in the 2nd position, then the total arrangements is
                all_in[n - 2]
                * Put A in the 2nd position, then the total arrangements is
                no_a[n - 2]
                * Put L in the 2nd position
                    * Put P in the 3rd position, then the total arrangements is
                    all_in[n - 3]
                    * Put A in the 3rd position, then the total arrangements is
                    no_a[n - 3]
        Thus, new_all_in = (all_in[n - 1] + all_in[n - 2] + all_in[n - 3]) +
                            (no_a[n - 1] + no_a[n - 2] + no_a[n - 3])
        Since we only need the past three values, we can restrict all_in and
        no_a to an array of size three. Then

            new_all_in = sum(all_in) + sum(no_a)

        Similarly we can obtain the formula to produce new_no_a.
            * Put P in the 1st position => no_a[n - 1]
            * Put L in the 1st position
                * Put P in the 2nd position => no_a[n - 2]
                * Put L in the 2nd position
                    * Put P in the 3rd position => no_a[n - 3]

        Thus, new_no_a = no_a[n - 1] + no_a[n - 2] + no_a[n - 3], or we can
        write it as

            new_no_a = sum(no_a)

        Using these two formulas, we can obtain the values for each number from
        1 to n. Once we reach n, we return all_in[-1].

        O(N), 1276 ms, 54% ranking.
        """
        MOD = 1000000007
        all_in = [3, 8, 19]
        no_a = [2, 4, 7]
        for i in range(3, n):
            new_all_in = (sum(all_in) + sum(no_a)) % MOD
            all_in[0], all_in[1], all_in[2] = all_in[1], all_in[2], new_all_in
            new_no_a = sum(no_a) % MOD
            no_a[0], no_a[1], no_a[2] = no_a[1], no_a[2], new_no_a
        return all_in[min(n - 1, 2)]


sol = Solution()
tests = [
    (1, 3),
    (2, 8),
    (3, 19),
    (4, 43),
    (5, 94),
    (6, 200),
    (7, 418),
    (8, 861),
    (9, 1753),
    (10, 3536),
    (10101, 183236316),
]

for i, (n, ans) in enumerate(tests):
    res = sol.checkRecord(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
