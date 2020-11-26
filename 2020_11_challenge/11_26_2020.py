# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import re


class Solution1:
    def longestSubstring(self, s: str, k: int) -> int:
        """38% ranking. Surprisingly this solution passed. But the run time is
        quite ugly.

        The idea is to find the letters that do not repeat k times over the
        entire string. These letters cannot be included in the find result. So
        we replace them with an empty space, and then split the original string
        into multiple smaller potentials. Then we run the same algo on each
        smaller potential until we get the result.

        According to the official solution, this method is divide and conquer.
        """
        ineligibles = [le for le, count in Counter(s).items() if count < k]
        if not ineligibles:
            return len(s)
        if len(ineligibles) == len(set(s)):
            return 0
        return max(self.longestSubstring(subs, k) for subs in re.sub('|'.join(ineligibles), ' ', s).split(' '))


class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        """The sliding window solution described in the official soltuion.

        We first count the number of unique letters in s. We know that the final
        answer must contain either 1, 2, 3, ..., max unique letters. So we try
        to check the substring with 1, 2, 3, ..., max unique letters number of
        unique letters.

        We use a sliding window strategy to do the check by having two indices:
        left and right. If the number of unique letters in s[left:right] equals
        our current target number, we count each letter's frequency and
        determine whether the current substring satisfies the requirement. If
        it does, we update the max substring length. If not, we leave it be.

        If the number of unique letters in s[left:right] is smaller than the
        current target number, we leave left as is and expand on right. If, on
        the other hand, the number of unique letters in s[left:right] is larger
        than the current target number, we shrink left by one and then progress
        right by one.

        Each run of a unique letter takes O(N), and there are at most 26 such
        runs. Thus the run time is O(26 * N) = O(N).

        UPDATE: the sliding window solution takes much longer than recursion. I
        got 200 ms (15% ranking), and I have to manually manage count_map and
        cur_uni. I might have gotten it wrong.
        """
        uniques = set(s)
        max_len = 0
        for num_uni in range(1, len(uniques) + 1):
            left, right = 0, num_uni
            count_map = [0] * 26
            cur_uni = len(set(s[left:right]))
            for i in range(left, right):
                count_map[ord(s[i]) - 97] += 1
            while True:
                if cur_uni == num_uni:
                    if all(c >= k for c in count_map if c > 0):
                        max_len = max(max_len, right - left)
                elif cur_uni > num_uni:
                    left += 1
                    count_map[ord(s[left - 1]) - 97] -= 1
                    if count_map[ord(s[left - 1]) - 97] == 0:
                        cur_uni -= 1
                    continue
                right += 1
                if right > len(s):
                    break
                count_map[ord(s[right - 1]) - 97] += 1
                if count_map[ord(s[right - 1]) - 97] == 1:
                    cur_uni += 1
        return max_len


sol = Solution2()
tests = [
    ('aaabb', 3, 3),
    ('ababbc', 2, 5),
    ('cababb', 2, 5),
    ('cababbc', 2, 7),
    ('cababb', 3, 0),
    ('', 1, 0),
    ('aaaaabaaa', 3, 5),
    ('aaaaabaaa', 4, 5),
    ('abcaabbdaaabbbe', 2, 6),
    ('abcaabbdaaabbbe', 3, 6),
    ('abcaabbdaaabbbe', 1, 15),
    ("aaaaaaaaabbbcccccddddd", 5, 10),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.longestSubstring(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
