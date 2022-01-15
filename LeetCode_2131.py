# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def longestPalindrome(self, words: List[str]) -> int:
        """The idea is that for each word that is not palindrome itself, it can
        only be used when its reverse version is also in words. If a word is
        palindrome, then if there are even count of the word, it is the same
        situation as non-palindrome word with its reverse pair. However, if
        there are odd count of a palindrome word, then one of the word must
        serve as the middle part of the resulting palindrome.

        This question restricts each word to length 2. But this is not
        necessary, and the following solution does not care about this restric-
        tion.

        O(N), 1692 ms, 61% ranking.
        """
        counter = Counter(words)
        res = 0
        max_seed = 0
        for w in counter:
            rev_w = w[::-1]
            if w != rev_w:  # w is not palindrome
                res += min(counter[w], counter[rev_w]) * 2 * len(w)
            elif counter[w] % 2 == 0:  # w is palindrome and has even count
                res += counter[w] * len(w)
            else:  # w is palindrome and has odd count
                res += (counter[w] - 1) * len(w)
                max_seed = max(max_seed, len(w))
            counter[w] = 0  # avoid double counting
            if rev_w in counter:
                counter[rev_w] = 0
        return res + max_seed


class Solution2:
    def longestPalindrome(self, words: List[str]) -> int:
        """I really like this pair-unpair solution from:

        https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/discuss/1675343/Python3-Java-C%2B%2B-Counting-Mirror-Words-O(n)

        O(N), 1758 ms
        """
        counter = Counter()  # record how many times each word is NOT paired
        res = unpaired_palindrome = 0
        for w in words:
            rev_w = w[::-1]
            if counter[rev_w] > 0:
                res += 4
                counter[rev_w] -= 1
                if w == rev_w:
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
    (["bb","bb"], 4),
]

for i, (words, ans) in enumerate(tests):
    res = sol.longestPalindrome(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
