# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter
import string


class Solution1:
    def countPalindromes(self, s: str) -> int:
        """The two hints are very important.

        The second hint points out that we should consider each middle digit
        when constructing the lenght-five palindrome. Once the middle digit is
        set, we need two on the left and two on the right.

        The first hint points out that the two digit pattern on the left has no
        more than 100 possibilities. This means in the worst case we can iterate
        trough all the patterns, find its count on the left, and find its
        reverse's count on the right. Then we just need to multiply the two
        counts, and we have the total number of length-five palindrome at the
        current middle digit.

        The problem now has converted to how to compute the counts of all double
        digit pattern on the left and on the right. We can use DP to solve this.
        
        On the left side, each time a new digit is encountered, all the digits
        that have been encountered before can pair with the new digit to form
        additional double digit patterns. The total number of such additional
        double digit patterns is equal to the count of the previous digit.
        Thus, if we keep track of the count of single digit, we can easily
        compute the counts of all possible double digit pattern up till the
        newly encountered digit.

        We can do the same on the right by going from right to left. The only
        difference is that the additional double digit patterns are formed with
        the newly encountered digit at the beginning.

        We can precompute the left and right single and double digit conuter.
        And then as the middle digit move, we modify the counters as we go.

        O(100N), 1405 ms, faster than 85.02%
        """
        N = len(s)
        if N < 5:
            return 0
        lrsdc, lrddc = Counter(), Counter()
        for i in range(N - 3):
            for k, v in lrsdc.items():
                lrddc[k + s[i]] += v
            lrsdc[s[i]] += 1
        rlsdc, rlddc = Counter(s[-2:]), Counter([s[-2:]])
        # go from right to left, consider each digit as the center of the
        # palindrome. Find out how many length-five palindrome can be formed
        res = 0
        for j in range(N - 3, 1, -1):
            if len(rlddc) < len(lrddc):
                for dd, v in rlddc.items():
                    res += lrddc[dd[::-1]] * v
            else:
                for dd, v in lrddc.items():
                    res += rlddc[dd[::-1]] * v
            # remove dd ending in s[j - 1] from lrddc
            lrsdc[s[j - 1]] -= 1
            if lrsdc[s[j - 1]] == 0:
                del lrsdc[s[j - 1]]
            for k, v in lrsdc.items():
                lrddc[k + s[j - 1]] -= v
                if lrddc[k + s[j - 1]] == 0:
                    del lrddc[k + s[j - 1]]
            # add dd starting with s[j] to rlddc
            for k, v in rlsdc.items():
                rlddc[s[j] + k] += v
            rlsdc[s[j]] += 1
        return res % (10**9 + 7)


class Solution2:
    def countPalindromes(self, s: str) -> int:
        """The two hints are very important.

        The second hint points out that we should consider each middle digit
        when constructing the lenght-five palindrome. Once the middle digit is
        set, we need two on the left and two on the right.

        The first hint points out that the two digit pattern on the left has no
        more than 100 possibilities. This means in the worst case we can iterate
        trough all the patterns, find its count on the left, and find its
        reverse's count on the right. Then we just need to multiply the two
        counts, and we have the total number of length-five palindrome at the
        current middle digit.

        The problem now has converted to how to compute the counts of all double
        digit pattern on the left and on the right. We can use DP to solve this.
        
        On the left side, each time a new digit is encountered, all the digits
        that have been encountered before can pair with the new digit to form
        additional double digit patterns. The total number of such additional
        double digit patterns is equal to the count of the previous digit.
        Thus, if we keep track of the count of single digit, we can easily
        compute the counts of all possible double digit pattern up till the
        newly encountered digit.

        We can do the same on the right by going from right to left. The only
        difference is that the additional double digit patterns are formed with
        the newly encountered digit at the beginning.

        We can precompute the left and right single and double digit conuter.
        And then as the middle digit move, we modify the counters as we go.

        O(100N), 1354 ms, faster than 85.53%
        """
        N = len(s)
        if N < 5:
            return 0
        lrsdc, lrddc = Counter(), Counter()
        for i in range(N - 3):
            for k, v in lrsdc.items():
                lrddc[k + s[i]] += v
            lrsdc[s[i]] += 1
        rlsdc, rlddc = Counter(s[-2:]), Counter([s[-2:]])
        # go from right to left, consider each digit as the center of the
        # palindrome. Find out how many length-five palindrome can be formed
        res = 0
        for j in range(N - 3, 1, -1):
            for dd, v in rlddc.items():
                res += lrddc[dd[::-1]] * v
            # remove dd ending in s[j - 1] from lrddc
            lrsdc[s[j - 1]] -= 1
            for k, v in lrsdc.items():
                lrddc[k + s[j - 1]] -= v
            # add dd starting with s[j] to rlddc
            for k, v in rlsdc.items():
                rlddc[s[j] + k] += v
            rlsdc[s[j]] += 1
        return res % (10**9 + 7)
        

sol = Solution2()
tests = [
    ("103301", 2),
    ("0000000", 21),
    ("9999900000", 2),
]

for i, (s, ans) in enumerate(tests):
    res = sol.countPalindromes(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
