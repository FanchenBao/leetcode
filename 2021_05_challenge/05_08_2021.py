# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution1:
    # Cache for all palindromes of different number of digits
    bases = {
        0: [0],  # necessary to compute 2-digit
        1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    }
    # Cache for the palindromes of different number of digits that can produce
    # superpalindromes. We obtain the solution by counting this dict.
    good_bases = {
        1: [1, 2, 3],
    }

    def superpalindromesInRange(self, left: str, right: str) -> int:
        """LeetCode 906

        This solution is very straightforward. We find all the palindrome
        bases first, compute their squares, and record which base can produce
        a superpalindrome. And record all of this information as cache. The
        trick lies in how to produce palindrom of higher number of digits based
        on palindromes already created in lower number of digits. The one that
        I blundered on is that I forgot to include 0.

        Another trick is to consider that the base for left and right can have
        the same number of digits.

        Once these two hurdles are cleared, we are good to go.

        We use cache heavily, which lands us at 288 ms, 94% ranking. Memory
        usage is 7% ranking.
        """
        lint, rint = int(left), int(right)
        # left base limit and right base limit
        llim, rlim = math.ceil(math.sqrt(lint)), math.floor(math.sqrt(rint))
        len_l, len_r = len(str(llim)), len(str(rlim))
        res = 0
        for num_dig in range(len_l, len_r + 1):
            # Generate all palindromes that have length of num_dig, if it is not
            # in the cache.
            if num_dig not in self.bases:
                for i in range(max(self.bases.keys()) + 1, num_dig + 1):
                    self.bases[i] = [mid * 10 + j + j * 10**(i - 1) for j in range(10) for mid in self.bases[i - 2]]
            # Loop through all the palindrome base of num_dig in length, and
            # identify which ones can produce superpalindrome. Save the eligible
            # ones in the good_bases cache.
            if num_dig not in self.good_bases:
                self.good_bases[num_dig] = []
                for base in self.bases[num_dig]:
                    str_squared = str(base**2)
                    if str_squared != '0' and str_squared == str_squared[::-1]:
                        self.good_bases[num_dig].append(base)
            # Count the number of good bases based on the current number of
            # digits under consideration and the left and right base limit.
            if num_dig == len_l and num_dig == len_r:
                res += (bisect_left(self.good_bases[num_dig], rlim + 1) - bisect_left(self.good_bases[num_dig], llim))
            elif num_dig == len_l:
                res += (len(self.good_bases[num_dig]) - bisect_left(self.good_bases[num_dig], llim))
            elif num_dig == len_r:
                res += bisect_left(self.good_bases[num_dig], rlim + 1)
            else:
                res += len(self.good_bases[num_dig])
        return res


class Solution2:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """This is the official solution, which is dubbed as math solution.
        However, I do not see this as a math solution. It's just a smart method
        to compute palindromes directly (i.e. without the need to save previous
        palindromes)

        The largest base palindrome is sqrt(10^18), whcih has nine
        digits. Thus, the half of the largest base palindrome has five digits
        and is an odd palindrome. Thus we loop through all values up to 10^5
        and check for superpalindromes.

        We can definitely build a cache for this as well, but Let's not do that
        """
        res = 0
        half_lim = 10**5
        lint, rint = int(left), int(right)
        for half in range(1, half_lim):
            # odd palindrome base
            oddp = str(half) + str(half)[-2::-1]
            oddsq = int(oddp)**2
            if oddsq < lint:
                continue
            if oddsq > rint:
                break
            str_oddsq = str(oddsq)
            if str_oddsq == str_oddsq[::-1]:
                res += 1
        for half in range(1, half_lim):
            # even palindrome base
            evenp = str(half) + str(half)[::-1]
            evensq = int(evenp)**2
            if evensq < lint:
                continue
            if evensq > rint:
                break
            str_evensq = str(evensq)
            if str_evensq == str_evensq[::-1]:
                res += 1
        return res


sol = Solution2()
tests = [
    ('4', '1000', 4),
    ('1', '2', 1),
    ('4', '10000', 4),
    ('4', '100000', 9),
    ('4', '1000000000', 20),
]

for i, (left, right, ans) in enumerate(tests):
    res = sol.superpalindromesInRange(left, right)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
