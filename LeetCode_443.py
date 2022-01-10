# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def compress(self, chars: List[str]) -> int:
        """We use groupby to easily obtain the letter and the number of repeats
        Then we simply turn the number of repeats into string and put each
        digit back into chars.

        The question could've been clearer in what the OJ checks. The OJ does
        not check the returned integer, but using the returned integer to
        check whether appropriate changes have been made to chars.

        O(N), 60 ms, 69% ranking.
        """
        res = 0
        for k, g in groupby(chars):
            l = len(list(g))
            chars[res] = k
            res += 1
            if l > 1:
                for i, dig in enumerate(str(l)):
                    chars[res + i] = dig
                res += len(str(l))
        return res


class Solution2:
    def compress(self, chars: List[str]) -> int:
        """Same idea as Solution1, but without using groupby.

        O(N), 86 ms, 18% ranking.
        """
        lo, hi, i = 0, 1, 0
        chars.append(' ')
        while hi < len(chars):
            if chars[hi] != chars[hi - 1]:
                chars[i] = chars[lo]
                if hi - lo > 1:
                    for dig in str(hi - lo):
                        i += 1
                        chars[i] = dig
                i += 1
                lo = hi
            hi += 1
        return i


sol = Solution2()
tests = [
    (["a","a","b","b","c","c","c"], ["a","2","b","2","c","3"]),
    (['a'], ["a"]),
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","1","2"]),
]

for i, (chars, ans) in enumerate(tests):
    res = sol.compress(chars)
    if chars[:res] == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {chars[:res]}')
