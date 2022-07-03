# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter
import heapq
from itertools import groupby, zip_longest
import math


class Solution1:
    def largestVariance(self, s: str) -> int:
        """This is one of the most difficult I've done.

        The first layer is to realize that we can break down the problem to
        considering only pairs of letters.

        The second layer is that once we have only two letters in a string, we
        can use Kadane to find the max diff in frequency of the two letters
        among all possible substrings. This Kadane is tricky, because we need
        to first dictate that the second letter must have higher frequency than
        the first, otherwise the max frequency value is zero.

        Then, the only time we can update the max frequency is when the current
        frequency is bigger and there is at least one occurrence of the first
        letter.

        Finally, the most tricky layer is that once the current frequency drops
        below zero, there is no point keep counting and we should restart. But
        we can only restart if there is at least one more first letter
        remaining. Otherwise, if there is no longer first letter, there is no
        point resetting.

        I cannot do this. This is the ceiling of my current capacity.

        O(26 * 26 * N), 5940 ms, faster than 23.36% 
        """
        counter = Counter(s)
        uniqs = list(counter.keys())
        res = 0
        for i in range(len(uniqs)):
            for j in range(len(uniqs)):
                if i == j:
                    continue
                max_freq = pre_freq = freq_i = 0
                remain_i = counter[uniqs[i]]
                # we want to find the max diff in frequency between i and j
                # and we dictate that freq_j >= freq_i; otherwise, we restart
                # this is Kadane
                for le in s:
                    if le != uniqs[i] and le != uniqs[j]:
                        continue
                    elif le == uniqs[i]:
                        freq_i += 1
                        pre_freq -= 1
                        remain_i -= 1
                    else:
                        pre_freq += 1
                    if pre_freq > max_freq and freq_i > 0:
                        max_freq = pre_freq
                    elif pre_freq < 0 and remain_i > 0:
                        # because when i is encountered again, start over.
                        # however, if there is no more i left, we do not start
                        # over, because starting over is meaningless in this
                        # sense.
                        freq_i = 0
                        pre_freq = 0
                res = max(res, max_freq)
        return res


class Solution2:
    def largestVariance(self, s: str) -> int:
        """This solution is adapted from
        https://leetcode.com/problems/substring-with-largest-variance/discuss/2038556/Python3-or-Simple-or-Kadanes-algo-or-Faster-than-100

        It is more comprehensible to me.

        3739 ms, faster than 52.63%
        """
        uniqs = list(set(s))
        res = 0
        for i in range(len(uniqs)):
            for j in range(len(uniqs)):
                if i == j:
                    continue
                has_a = False
                a, b = uniqs[i], uniqs[j]
                max_freq = cur_freq = 0
                for le in s:
                    if le != a and le != b:
                        continue
                    if le == a:
                        cur_freq -= 1
                        has_a = True
                    elif le == b:
                        cur_freq += 1
                    if cur_freq > max_freq:
                        max_freq = cur_freq if has_a else cur_freq - 1
                    elif cur_freq < 0:
                        cur_freq = 0
                        has_a = False
                res = max(res, max_freq)
        return res



sol = Solution2()
tests = [
    ('aaaa', 0),
    ('aaaabb', 3),
    ("aababbb", 3),
    ("abcde", 0),
    ("icexiahccknibwuwgi", 3),
    ("dsyemilsuwhciclqwprizywgkwkbgcqhtcwfvlw", 5),
    ("lripaa", 1),
    ("fjpualxkrxjkxrymbzkwrgwqiwhcxxdvllixwagwwyrabakxdmarqgkeuiyctbcpgtisvifcnocynteherojfcxtdwutcavzjdfgteethcrerjmxavzuhoewbhnaflrxmitkvnpxsjhkutrsrdzbvsxyjeumndyczvarejbgggktbhsgecoefvfxxfvyffbdnltdacfimqvezvwyidlrhbkrawarwzfxqznlzyggsnofpodjfyofzqlucquyigggkogf", 13),
    ("bbaabbaabbaabb", 2),
]

for i, (s, ans) in enumerate(tests):
    res = sol.largestVariance(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
