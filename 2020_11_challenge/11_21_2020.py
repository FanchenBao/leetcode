# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """55% ranking.

        This question is very tricky in its edge cases. I missed two of them,
        one is when some combination of the digits happen to equal n. And the
        other is when all digits in digists are smaller than the digits in n.
        """
        digits.sort()
        dlen = len(digits)
        str_n = str(n)
        res = sum(dlen**i for i in range(1, len(str_n)))
        found_equal = False  # edge case where n and digits are equal
        for j, dn in enumerate(str_n, 1):
            for d in digits:
                if d < dn:
                    res += dlen**(len(str_n) - j)
                else:
                    break
            if d != dn:  # no need to continue the search if dn > n or dn < n
                break
            elif j == len(str_n):
                found_equal = True
        return res + 1 if found_equal else res


class Solution2:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """DP. From the official solution.
        """
        digits.sort()
        dlen = len(digits)
        str_n = str(n)
        res = sum(dlen**i for i in range(1, len(str_n)))
        dp = [0] * len(str_n) + [1]
        for i in range(len(str_n) - 1, -1, -1):
            dn = str_n[i]
            for d in digits:
                if d < dn:
                    dp[i] += dlen**(len(str_n) - 1 - i)
                elif d == dn:
                    dp[i] += dp[i + 1]
        return res + dp[0]


sol = Solution2()
tests = [
    (['1', '3', '5', '7'], 100, 20),
    (['1', '3', '5', '7'], 156, 31),
    (['1', '6', '5'], 156, 18),
    (['1', '4', '9'], 1000000000, 29523),
    (['7'], 8, 1),
    (['8', '9'], 7, 0),
    (['3', '4', '8'], 4, 2),
    (['1'], 834, 3),
]

for i, (digits, n, ans) in enumerate(tests):
    res = sol.atMostNGivenDigitSet(digits, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
