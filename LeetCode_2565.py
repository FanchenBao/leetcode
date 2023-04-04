# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, deque


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        le_idx = defaultdict(deque)
        for i, le in enumerate(s):
            le_idx[le].append(i)
        lo, hi = 0, len(t) - 1
        pre_left, post_right = -1, len(s)
        lo_stuck = hi_stuck = False
        while lo <= hi and (not lo_stuck or not hi_stuck):
            print(lo, hi, le_idx, pre_left, post_right)
            # left
            while le_idx[t[lo]] and le_idx[t[lo]][0] < pre_left:
                le_idx[t[lo]].popleft()
            if le_idx[t[lo]] and le_idx[t[lo]][0] < post_right:
                pre_left = le_idx[t[lo]].popleft()
                lo += 1
            else:
                lo_stuck = True
            # right
            while le_idx[t[hi]] and le_idx[t[hi]][-1] > post_right:
                le_idx[t[hi]].pop()
            if le_idx[t[hi]] and le_idx[t[hi]][-1] > pre_left:
                post_right = le_idx[t[hi]].pop()
                hi -= 1
            else:
                hi_stuck = True
        return hi - lo + 1


sol = Solution()
tests = [
    # ("abacaba", "bzaa", 1),
    # ("cde", "xyz", 3),
    # ("aabbbaababb", "bbabab", 0),
    # ("aabbbaa", "bbababa", 3),
    # ("aabababbbbababababababa", "bababababaabbabbaababba", 6),
    ("babbababab", "ababababab", 1),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.minimumScore(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
