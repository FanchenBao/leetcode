# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        """First things first, we can do q1 ^ q2 to find the value to search in
        s. We turn the value into its binary string, so the problem is converted
        to finding the index of the first occurring substring in s.

        The naive solution is to use s.index(bin_str). It might be fast if the
        bin_str can be found. But if it cannot, python throws an exception. We
        have one test case where all the queries will throw exceptions. Since
        python's exception handling is very slow, we TLE.

        The next attempt is to cache all the values we have encountered during
        matching. This is basically an avoidance of going through KMP. For each
        target bin_str, we sliding window s to find all available substring of
        the same length. We compute their decimal values and check if the
        current window range has the smallest start. We save the smallest start
        in a dict, with the key being the value.

        This way, for a bin_str in the future whose value we have searched
        before, we can simply obtain it from the cache.

        The tricky part is with zero. Because when we encounter zero during
        sliding window, it might be multiple consecutive zeroes. This we have to
        handle differently.

        Since the max value in queries is 10^9, which is 2^30, at most we run
        the sliding window 30 times.

        O(M + 30N), where M = len(queries), N = len(s)
        1603 ms, faster than 57.94%
        """
        res = []
        val_occ_map = {}  # key is some val, value is the range of its first occurrence in s
        checked = set()  # the checked length should not be checked again
        for q1, q2 in queries:
            val = q1 ^ q2
            bin_val = f'{val:b}'
            if len(bin_val) not in checked:
                win = ''
                for i in range(len(s)):  # sliding window
                    win += s[i]
                    if len(win) == len(bin_val):
                        n = int(win, 2)
                        if n == 0:  # zero must be handled differently
                            st = ed = i - len(win) + 1
                        else:
                            st, ed = i - len(win.lstrip('0')) + 1, i
                        if val_occ_map.get(n, [math.inf, math.inf])[0] > st:
                            val_occ_map[n] = [st, ed]
                        win = win[1:]
                checked.add(len(bin_val))
            res.append(val_occ_map.get(val, [-1, -1]))
        return res


sol = Solution()
tests = [
    ("101101", [[0,5],[1,2]], [[0,2],[2,3]]),
    ("0101", [[12,8]], [[-1,-1]]),
    ("1", [[4,5]], [[0,0]]),
    ("111010110", [[4,2],[3,3],[6,4],[9,9],[10,28],[0,470],[5,83],[10,28],[8,15],[6,464],[0,3],[5,8],[7,7],[8,8],[6,208],[9,15],[2,2],[9,95]], [[1,3],[3,3],[2,3],[3,3],[4,8],[0,8],[2,8],[4,8],[0,2],[0,8],[0,1],[1,4],[3,3],[3,3],[1,8],[1,3],[3,3],[2,8]]),
    ("0000001111101001010", [[0,3914],[2,4],[2,2],[3,8009],[4,3918],[7,26]], [[7,18],[9,11],[0,0],[6,18],[7,18],[8,12]]),
]

for i, (s, queries, ans) in enumerate(tests):
    res = sol.substringXorQueries(s, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
