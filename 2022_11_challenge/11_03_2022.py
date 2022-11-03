# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def longestPalindrome(self, words: List[str]) -> int:
        """LeetCode 2131

        For each word that has the same letter repeated, we can always form
        palindrome if the count is even. We can allow only one odd count, which
        will be placed in the center.

        For each word that does not have any letter repeated, we simply find
        its reverse and take the smaller count between the two.

        O(N), 3512 ms, faster than 27.93%
        """
        counter = Counter(words)
        res = 0
        has_center_occupied = False
        for w, c in counter.items():
            if w[0] == w[1]:
                if c % 2 == 0:
                    res += c * 2
                else:
                    if not has_center_occupied:
                        res += c * 2
                        has_center_occupied = True
                    else:
                        res += (c - 1) * 2
            else:
                res += min(c, counter[w[::-1]]) * 2
        return res


class Solution2:
    def longestPalindrome(self, words: List[str]) -> int:
        """The pair-unpair method from the submission on 01/14/2022
        """
        counter = Counter()
        res = 0
        unpaired_palindrome = 0
        for w in words:
            rev_w = w[::-1]
            if counter[rev_w]:
                res += 4
                counter[rev_w] -= 1
                if w == rev_w and not counter[rev_w]:
                    unpaired_palindrome -= 1
            else:
                counter[w] += 1
                if w == rev_w:
                    unpaired_palindrome += 1
        return res + (2 if unpaired_palindrome > 0 else 0)


sol = Solution2()
tests = [
    (["lc","cl","gg"], 6),
    (["ab","ty","yt","lc","cl","ab"], 8),
    (["cc","ll","xx"], 2),
]

for i, (words, ans) in enumerate(tests):
    res = sol.longestPalindrome(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
