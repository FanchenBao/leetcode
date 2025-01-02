# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Find the max letter in word. Then find the max second letter after the
        first max letter. Keep going until only one substring is left. Along
        the way, we need to keep track of the constraint of the max size allowed
        for a substring.

        O(N^2), 2120 ms, 10.23%
        """
        if numFriends == 1:
            return word
        N = len(word)
        max_len = N - numFriends + 1
        tgts = [[i, i - 1] for i in range(N)]
        while len(tgts) > 1 and tgts[0][1] - tgts[0][0] + 1 <= max_len:
            tmp = []
            max_let = "*"
            for i, j in tgts:
                if j + 1 < N:
                    if word[j + 1] > max_let:
                        max_let = word[j + 1]
                        tmp = [[i, j + 1]]
                    elif word[j + 1] == max_let:
                        tmp.append([i, j + 1])
            tgts = tmp
        return word[tgts[0][0] : tgts[0][0] + max_len]


class Solution2:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        This solution comes from the hint. We know the max length of the
        substring must be N - numFriends + 1. If a max substring can be extended
        to max_len, it definitely should. Thus, we can use sliding window to
        find the max substring with length max_len.

        Then we go through the suffix substrings to see if any of them is even
        larger than the largest substring with max_len.

        O(N(N - K)) where N = len(word), K = numFriends

        19 ms, 39.26%
        """
        if numFriends == 1:
            return word
        N = len(word)
        max_len = N - numFriends + 1
        res = word[:max_len]
        for i in range(max_len, N):
            res = max(res, word[i - max_len + 1 : i + 1])
        for j in range(N - 1, N - max_len, -1):
            res = max(res, word[j:])
        return res


sol = Solution2()
tests = [
    ("gh", 1, "gh"),
]

for i, (word, numFrieds, ans) in enumerate(tests):
    res = sol.answerString(word, numFrieds)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
