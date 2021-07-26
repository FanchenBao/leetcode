# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
from functools import lru_cache


class Solution1:
    max_len = len(bin(10**9)) - 2
    dp = [0] * (max_len + 1)
    dp[2] = 1
    for i in range(3, max_len + 1):
        dp[i] = 1 << (i - 2)
        for j in range(2, i - 2 + 1):
            dp[i] += dp[j]
    dp_acc = list(accumulate(dp))

    def findIntegers(self, n: int) -> int:
        """LeetCode 600.

        First of all, we create a dp table such that dp[k] gives us the total
        number of values with consecutive ones (let's call it targets) from
        2^(k - 1) to 2^k - 1, which is from 1000..0 with k zeros to 1111...1
        with k ones. We can divide this problem into subproblems. We know every
        alue that starts with 11xxx...x is valid. So we at least have 2^(k - 2)
        targets. Then, given 10xxx...x, then the total number of targets is
        dp[k - 2]. Given 100xx...x, the total number of targets is dp[k - 3],
        etc. Thus we can compute dp[k] = 2^(k - 2) + dp[k - 2] + dp[k - 3] + ...
        + dp[1]

        After computing the dp table, we perform prefix sum to obtain a dp_acc
        for future use.

        Then, given any n, we can write its binary form as 10xxx...x or 11xxx...x
        with M number of digits. If it's 10xxx...x, then the total number of
        targets from 10000...0 (M - 1 zeros) to 10xxx.xx (M - 2 x's) is the same as
        from 0 to xxx...x (M - 2 x's). So the total number of targets from 0 to
        10xxx...x (M - 2 x's) is dp_acc[M - 1] + findIntegers(xxx...x)

        If it's 11xxx...x, then we split the number up into two parts:
        11000...0 to 11xxx...x and 10000...0 to 10111...1. The first split has
        total number of targets xxx...x + 1 (M - 2 x's), and the second split
        has total number of targets dp_acc[M - 2].

        Thus the total number of targets from 0 to n is
        dp_acc[M - 1] + one of the two scenarios described above.

        O(log(N)), 32 ms, 84% ranking.
        """

        @lru_cache(maxsize=None)
        def count_consec(num: int) -> int:
            if num <= 2:
                return 0
            if num == 3:
                return 1
            bin_str = bin(num)[2:]
            bin_rem = int(bin_str[2:], 2)
            if bin_str[1] == '1':
                return self.dp_acc[len(bin_str) - 1] + self.dp_acc[len(bin_str) - 2] + bin_rem + 1
            return self.dp_acc[len(bin_str) - 1] + count_consec(bin_rem)

        return n + 1 - count_consec(n)


class BIT:
    def __init__(self, N: int):
        """Initialize a binary indexed tree.

        :param N: The size of the range, including min and max.
        """
        # use 1-based BIT, thus array size must be one larger than the range.
        self.bit = [0] * (N + 1)

    def update(self, pos: int, delta: int) -> None:
        """Update the value at `pos` by adding `delta`.

        Also update all the other ranges that contain `pos`.

        :param pos: The position inside a range whose value needs to be
            updated. Note that this position is one less than the index
            of the self.bit array.
        :param delta: The additional value that needs to be added to
            the value at the given position, and all the other ranges
            including the given position.
        """
        # KEY POINT: BIT index is 1-based, thus its index is one larger
        # than the given position.
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += (i & -i)

    def query(self, max_r: int) -> int:
        """Query the sum of values in the range 0 to `max_r`.

        The meaning of "values" us defined by the `delta` parameter
        in self.update(). It is not necessarily prefix sum.

        :param max_r: The end of the range which we want to query.
        :return: Sum of values in the range 0 to `max_r`.
        """
        # KEY POINT: Bit index is 1-based, thus its index is one larger
        # than the given max range.
        i, res = max_r + 1, 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res


class Solution2:
    def findIntegers(self, n: int) -> int:
        """For fun, I tried BIT, but it TLE because the runtime is O(NlogN) for
        building up the BIT.
        """
        bit = BIT(n + 1)
        for i in range(3):
            bit.update(i, 0)
        bit.update(3, 1)
        for i in range(4, n + 1):
            bin_str = bin(i)[2:]
            if bin_str[1] == '1':
                bit.update(i, 1)
            else:
                rem = int(bin_str[2:], 2)
                bit.update(i, bit.query(rem) - bit.query(rem - 1))
        return n + 1 - bit.query(n)


class Solution3:
    def findIntegers(self, n: int) -> int:
        """Official solution with bit manipulation.

        https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/solution/

        It's a similar idea as mine, but with much better implementation.
        We use dp array to represent the total number of valid values (not a
        valid value is one without consecutive ones). It can be proved that given
        k bits, dp[k] = dp[k -1] + dp[k - 2]

        After acquiring dp, we consider the given n from the MSB to LSB. Say n
        has M bits, if the Mth bit (MSB) is 1, then result += dp[M - 1]. Then
        we move to M - 1th bit. If M -1th is a 0, we decrement M and keep going.
        If M - 1th is a 1, we are still able to do result += dp[M - 2], but since
        now we have consecutive 1s at M and M - 1, there is no point moving on.
        """
        dp = [0] * 32
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]
        bin_str = bin(n)[2:]
        res = 0
        for i, b in enumerate(bin_str):
            if b == '1':
                res += dp[len(bin_str) - i - 1]
                # have consecutive 1s, no point continuing
                if i > 0 and bin_str[i - 1] == '1':
                    return res
        return res + 1  # have to add the given n as well.


sol = Solution3()
tests = [
    (5, 5),
    (1, 2),
    (2, 3),
    (3, 3),
    (4, 4),
    (6, 5),
    (7, 5),
    (8, 6),
    (20, 12),
]

for i, (n, ans) in enumerate(tests):
    res = sol.findIntegers(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
