# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        """LeetCode 76

        The idea is that the answer must start with one of the letters in t.
        Thus, what we can do is to find all the possible substrings in s that
        starts with each letter in t. One of such possible substrings must be
        the answer. We can use sliding window to solve this by using two
        pointers. We move the right pointer when s[l:r + 1] is not a possible
        solution. Once we reach a possible solution, we record it if it is
        shorter than all the previous ones, and then move the left pointer until
        we reach another letter that is in t. Repeat this until we reach the
        end.

        O(M + N), where M is the size of s and N the size of t. Note that when
        we check for whether the current substring is a possible answer, we
        iterate through the counter of t. Since there are only 26 + 26 = 52
        possible keys in the counter, this iteration can be considered an O(1)
        operation.

        596 ms, 7% ranking.
        """
        ct, cs = Counter(t), Counter()
        m, n = len(s), len(t)
        l = 0
        while l < m:  # Find the first letter in s that also exists in t
            if s[l] in ct:
                cs[s[l]] += 1
                break
            l += 1
        r = l
        res = [0, m + n]
        while r < m:  # sliding window
            if all(cs[k] >= v for k, v in ct.items()):
                res = [l, r] if res[1] - res[0] > r - l else res
                # After obtaining one possible answer, we move l until reaching
                # another letter that is in t.
                cs[s[l]] -= 1
                l += 1
                while l <= r:
                    if s[l] in ct:
                        break
                    l += 1
            else:
                # If no match can be found, we expand on r until reaching
                # another letter that is in t
                r += 1
                while r < m:
                    if s[r] in ct:
                        cs[s[r]] += 1
                        break
                    r += 1
        return s[res[0]:res[1] + 1] if res[1] - res[0] < m + n else ''


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        """This is from the official solution:

        https://leetcode.com/problems/minimum-window-substring/solution/

        However, I did have the same idea before, yet I did not follow through
        because Solution1 is easier to code. Anyway, we will first shrink s
        down to a new string that contains only letters found in t. Then we run
        the same algorithm as in Solution1.

        In fact, by shrinking, it's actually easier to code. My original thought
        was wrong. It is easier because we don't have to iterate to find the
        next viable letter during sliding window.
        """
        ct, cs = Counter(t), Counter()
        m, n = len(s), len(t)
        shrink = [(le, i) for i, le in enumerate(s) if le in ct]
        if not shrink:  # don't forget to check edge case!!
            return ''
        l = r = 0
        size = len(shrink)
        res = [0, m + n]
        cs[shrink[0][0]] += 1
        while r < size:  # sliding window
            if all(cs[k] >= v for k, v in ct.items()):
                res = [shrink[l][1], shrink[r][1]] if res[1] - res[0] > shrink[r][1] - shrink[l][1] else res
                cs[shrink[l][0]] -= 1
                l += 1
            else:
                r += 1
                if r < size:
                    cs[shrink[r][0]] += 1
        return s[res[0]:res[1] + 1] if res[1] - res[0] < m + n else ''


class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        """This is a better implementation of Solution2 (note that I did not
        follow the official solution in Solution2).

        This is faster than Solution1 and 2, because we do not have to iterate
        through ct in order to decide whether the current possible solution
        is legitimate.

        180 ms, 25% ranking.
        """
        ct, cs = Counter(t), Counter()
        m, n = len(s), len(t)
        shrink = [(le, i) for i, le in enumerate(s) if le in ct]
        l = r = 0
        size = len(shrink)
        # char_included is whether all the letters in t has been found in
        # current possible solution
        res, char_included = [0, m + n], 0
        while r < size:  # sliding window
            # must check before modifying cs
            if cs[shrink[r][0]] + 1 == ct[shrink[r][0]]:
                char_included += 1
            cs[shrink[r][0]] += 1
            while l <= r and char_included == len(ct):
                res = [shrink[l][1], shrink[r][1]] if res[1] - res[0] > shrink[r][1] - shrink[l][1] else res
                # must modify cs before check
                cs[shrink[l][0]] -= 1
                if cs[shrink[l][0]] < ct[shrink[l][0]]:
                    char_included -= 1
                l += 1
            r += 1
        return s[res[0]:res[1] + 1] if res[1] - res[0] < m + n else ''


sol = Solution3()
tests = [
    ('ADOBECODEBANC', 'ABC', 'BANC'),
    ('a', 'a', 'a'),
    ('a', 'aa', ''),
    ('a', 'b', ''),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.minWindow(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
