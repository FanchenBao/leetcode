# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """LeetCode 68

        Not really a difficult one, but some analysis is needed to handle tricky
        edge cases.

        The basic idea is to read through all the words until the required
        length, i.e. each word associated with one white space, exceeds maxWidth

        Then we exclude the last word, and justify all the previous words. We
        know the total amount of extra white space needed, so we just need to
        evenly distribute these extra white spaces. We use divmod to find the
        remaining additional white spaces to distribute, we distribute them from
        left to right.

        The two edge cases are 1. the last row, which we shall handle separately
        and 2. a non-last row that contains only one word, which we can also
        handle separately.

        O(N * K), 34 ms, faster than 94.14% 
        """

        def justify(lo: int, hi: int, extra: int) -> str:
            if hi == len(words) - 1:
                # last row, must be left justified
                return ' '.join(words[lo:hi + 1]) + ' ' * extra
            if hi == lo:
                return words[lo] + ' ' * extra
            ave_extra_ws, add_extra_ws = divmod(extra, hi - lo)
            res_arr = []
            for i in range(lo, hi + 1):
                res_arr.append(words[i])
                num_extra_ws = ave_extra_ws + 1
                if add_extra_ws:
                    num_extra_ws += 1
                    add_extra_ws -= 1
                if i < hi:
                    res_arr.append(' ' * num_extra_ws)
            return ''.join(res_arr)

        num_char = lo = 0
        res = []
        for i, w in enumerate(words):
            num_char += len(w)
            if num_char > maxWidth:
                num_char -= len(w) + 1
                res.append(justify(lo, i - 1, maxWidth - num_char))
                num_char = len(w) + 1
                lo = i
            else:
                num_char += 1
        num_char -= 1
        res.append(justify(lo, i, maxWidth - num_char))
        return res


sol = Solution()
tests = [
    (["This", "is", "an", "example", "of", "text", "justification."], 16, ["This    is    an","example  of text","justification.  "]),
    (["What","must","be","acknowledgment","shall","be"], 16, ["What   must   be","acknowledgment  ","shall be        "]),
]

for i, (words, maxWidth, ans) in enumerate(tests):
    res = sol.fullJustify(words, maxWidth)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
