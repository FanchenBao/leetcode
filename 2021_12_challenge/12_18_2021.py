# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """LeetCode 902

        We have done this before, and it seems like it was not too big a
        challenge back then. The insight is that, say n has N digits. We only
        have to analyze the possibility of forming N-digit values. We don't have
        to worry about N - 1, N - 2, ..., 1 number of digits, because any
        formation of these digit numbers will be smaller than N.

        So, we evaluate n one digit at a time from left to right. If the current
        digit in n can be found in digits, then we must continue onto the next
        digit. Otherwise, we are done.

        Meanwhile, each time we analyze a digit, we find how many digits in the
        input array are smaller than the current digit. All of these smaller
        digits can form values smaller than n. Thus, at each digit, we will
        add a new count with the number of the smaller digits multiplied by
        any combinations of digits for the remaining positions.

        We continue this until either the current digit is bigger than all the
        digits in the input, or n is exhausted.

        The thing that caused us an error is that when n is exhausted, i.e. we
        can find some combinations of the input digits to form n, we need to
        add one to the final result.

        O(Nlog(M)), N is the number of digits in n, M = len(digits)
        34 ms, 32% ranking
        """
        nstr = str(n)
        res, M, N = 0, len(digits), len(nstr)
        for i, dig in enumerate(nstr):
            cont = False
            count = bisect_right(digits, dig)
            if count > 0 and digits[count - 1] == dig:
                cont = True
                count -= 1
            res += count * (M**(N - i - 1))
            if not cont:
                break
        else:
            res += 1  # we can form exactly n using digits
        return res + ((M**N - M) // (M - 1) if M > 1 else N - 1)



sol = Solution()
tests = [
    (["1","3","5","7"], 100, 20),
    (["1","4","9"], 1000000000, 29523),
    (['7'], 8, 1),
    (["3","4","8"], 4, 2),
]

for i, (digits, n, ans) in enumerate(tests):
    res = sol.atMostNGivenDigitSet(digits, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
