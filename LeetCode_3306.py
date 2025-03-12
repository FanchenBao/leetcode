# from pudb import set_trace; set_trace()
from typing import List
import math
import collections


class Solution:
    def atleast_k(self, word: str, k: int) -> int:
        N = len(word)
        vowels = {"a", "e", "i", "o", "u"}
        res = 0
        counter = collections.Counter()
        i = cc = 0
        for j in range(N):
            if word[j] in vowels:
                counter[word[j]] += 1
            else:
                cc += 1
            while len(counter) == 5 and cc >= k:
                res += N - j
                if word[i] in vowels:
                    counter[word[i]] -= 1
                    if not counter[word[i]]:
                        del counter[word[i]]
                else:
                    cc -= 1
                i += 1
        return res

    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        This is from the editorial which uses the relaxed constraint method.

        Instead of finding the substring exactly k consonants, we find the
        number of substrings that contains at least k consonants, call it
        atleast_k.

        Then we find the number of substrings that contains at least k + 1
        consonants, call it atleast_k_plus_1.

        Then the answer is atleast_k_plus_1 - atlast_k.

        O(N) 1913 ms, 60.70%
        """
        return self.atleast_k(word, k) - self.atleast_k(word, k + 1)


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
