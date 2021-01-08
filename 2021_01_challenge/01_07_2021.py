# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """DP solution. The observation is that we keep track of two things. One
        is the left bound index of the max non-repeating substring ending with
        the previous letter. We call it `pre_left_bound`. Using `pre_left_bound`
        and the current letter's index, we can compute the max length of the
        non-repeating substring ending with the current letter.

        Two is a dict recording the index the last time a letter shows up. We
        use this dict to compute one of the potential left bounds of the
        substring ending with the current letter: this string cannot go beyond
        the last time the current letter shows up. This potential left bound is
        compared to the `pre_left_bound`, and the larger of the two is the
        `cur_left_bound`. We repeat this process until the end and updating
        `pre_left_bound` and dict along the way.

        O(N), 68 ms, 52% ranking.

        Note, this is the same as the official solution, though the official
        solution calls it sliding window, which from its perspective does make
        sense.
        """
        pos = {}
        pre_left_bound = res = 0
        for i, le in enumerate(s):
            cur_left_bound = max(pos.get(le, -1) + 1, pre_left_bound)
            res = max(res, i - cur_left_bound + 1)
            pre_left_bound = cur_left_bound
            pos[le] = i
        return res


sol = Solution()
tests = [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.lengthOfLongestSubstring(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
