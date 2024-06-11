# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        """
        Sort the frequencies of all the letters in s. If there are no more than
        k unique letters, we cannot form any K-subsequence.

        Otherwise, we will have to use the first k letters with the highest
        frequencies.

        However, there is a complication when the kth, k + 1th, ... letters
        also have the same freq as the k - 1th letter.

        In this case, we need to include them as well when computing the total
        number of K-subsequences.

        72 ms, faster than 88.55%
        """
        sorted_cnts = sorted(Counter(s).items(), key=lambda tup: tup[1], reverse=True)
        if k > len(sorted_cnts):
            return 0
        i, j = k - 2, k
        while i >= 0 and sorted_cnts[i][1] == sorted_cnts[k - 1][1]:
            i -= 1
        i += 1
        while j < len(sorted_cnts) and sorted_cnts[j][1] == sorted_cnts[k - 1][1]:
            j += 1
        j -= 1
        MOD = 10**9 + 7
        res = 1
        for ii in range(i):
            res = (res * sorted_cnts[ii][1]) % MOD
        # the number of letters to choose from that has the same freq as the kth letter
        p = j - i + 1
        # the number of letters allowed to be in the K-subsequence that has the same freq as the keth letter
        q = k - i
        return (res * math.comb(p, q) * pow(sorted_cnts[k - 1][1], q, MOD)) % MOD


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
