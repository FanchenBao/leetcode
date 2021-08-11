# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def minFlipsMonoIncr(self, s: str) -> int:
        """LeetCode 926

        DP for the rescue as usual. We go from right to left. At any index i,
        if s[i] == '0', we have two choices. Either we keep s[i] as is, then we
        require s[i + 1:] to be monotone increasing. Thus the min flips to make
        s[i] monotone increasing is the same as the min flips to make s[i + 1:]
        monotone increasing. Or we flip s[i] and make it '1'. Then to make
        s[i:] monotone increasing, we need to make s[i + 1:] all '1'. Thus, we
        need to keep track of the number of zeros in s[i + 1:], because that
        determines the number of flips needed to turn s[i + 1:] all '1'.

        Similarly, if s[i] == '1', we can either keep it as '1' and make
        s[i + 1:] all '1', or we flip to '0' and check the min flips that can
        make s[i + 1:] montone increasing.

        Either way, we keep the min flips between the two options. We continue
        this until reaching the start of s.

        O(N) time, O(1) space. 216 ms, 10 % ranking.
        """
        # keep track of the number of zeroes encountered so far
        count_zeroes = min_flips = 0
        for c in s[::-1]:
            if c == '0':
                min_flips = min(min_flips, 1 + count_zeroes)
                count_zeroes += 1
            else:  # s[i] == '1'
                min_flips = min(count_zeroes, 1 + min_flips)
        return min_flips


class Solution2:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Same idea as Solution1, but with refactoring that makes the code
        harder to read. NOT RECOMMENDED!

        Inspired by: https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/1394750/C%2B%2B-Simple-and-Short-O(n)-Solution-With-Explanation
        """
        count_zeroes = min_flips = 0
        for c in s[::-1]:
            if c == '0':
                count_zeroes += 1
            else:
                min_flips += 1
            min_flips = min(min_flips, count_zeroes)
        return min_flips


sol = Solution1()
tests = [
    ('00110', 1),
    ('010110', 2),
    ('00011000', 2),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minFlipsMonoIncr(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
