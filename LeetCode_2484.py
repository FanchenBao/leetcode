# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter
import string


class Solution:
    def countPalindromes(self, s: str) -> int:
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
        # palindrome. Find out how many 5-size palindrome can be formed
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
            for k, v in lrsdc.items():
                lrddc[k + s[j - 1]] -= v
            # add dd starting with s[j] to rlddc
            for k, v in rlsdc.items():
                rlddc[s[j] + k] += v
            rlsdc[s[j]] += 1
        return res
        

sol = Solution()
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
