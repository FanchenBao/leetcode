# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findNthDigit(self, n: int) -> int:
        """This is not a difficult problem, because it can be solved via
        analysis. First of all, we need to pinpoint the number of digits the
        target value has. To do this, we run a loop to check at which number
        of digits, the total sum of digits exceed n.

        Then, after we obtain the number of digits k for the target value, we
        compute the number of digits going from 10^(k - 1) to our target value.
        Let's call that rem.

        After that, we compute divmod(rem, k) = q, r. This tells us how many
        k-digit numbers are there from 10^(k - 1) to our target values. In
        other words our target value is 10^(k - 1) + q. Finally, the target
        digit is the (r - 1)th digit in the str version of the target value.

        Two potholes. First is when rem == 0, and the second is when r == 0.
        They need to be treated separately. rem == 0 means the nth digit is the
        last digit of the last number of (k - 1)-digit number, which is always
        9. r == 0 means the nth digit is the last digit of 10^(k - 1) + q - 1.

        O(logN), 32 ms, 50% ranking.
        """
        k, s = 0, 0
        while s <= n:
            s += 9 * 10**k * (k + 1)
            k += 1
        rem = n - (s - 9 * 10**(k - 1) * k)
        if rem == 0:
            return 9
        q, r = divmod(rem, k)  # k is the number of digits for the current num
        return int(
            str(10**(k - 1) + q)[r - 1] if r else str(10**(k - 1) + q - 1)[-1],
        )


class Solution2:
    def findNthDigit(self, n: int) -> int:
        """Same idea but better implementation.

        Ref: https://leetcode.com/problems/nth-digit/discuss/88363/Java-solution
        """
        num_dig, start, count = 1, 1, 9
        while n > count * num_dig:
            n -= count * num_dig
            count *= 10
            num_dig += 1
            start *= 10
        q, r = divmod(n, num_dig)
        return int(str(start + q)[r - 1] if r else str(start + q - 1)[-1])


sol = Solution2()
tests = [
    (3, 3),
    (11, 0),
]

for i, (n, ans) in enumerate(tests):
    res = sol.findNthDigit(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
