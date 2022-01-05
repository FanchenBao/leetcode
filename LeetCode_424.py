# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        """TLE
        """
        alphabet = set(s)
        dp = [[0] * 26 for _ in range(len(s) + 1)]
        for j in range(1, len(s) + 1):
            dp[j][ord(s[j - 1]) - 65] += 1 + dp[j - 1][ord(s[j - 1]) - 65]
        for _ in range(k):
            temp = [[0] * 26 for _ in range(len(s) + 1)]
            for j in range(1, len(s) + 1):
                for le in alphabet:
                    idx = ord(le) - 65
                    if le == s[j - 1]:
                        temp[j][idx] += 1 + temp[j - 1][idx]
                    else:
                        temp[j][idx] += 1 + dp[j - 1][idx]
            dp = temp
        return max(max(cnt) for cnt in dp[1:])


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        """I read the hint from the discussion and came up with this sliding
        window solution.

        The idea is that given a substring s[lo:hi + 1], the best strategy is
        always to find the letter with the most repeats, and change the rest
        to that letter. Thus, we can use a counter to obtain the number of
        changes needed for each range in O(26) time. We keep increasing hi if
        the number of changes is within limit. Otherwise, we increase lo to
        reduce the range.

        O(26N), 472 ms, 6% ranking.
        """
        cnt = Counter(s[0])
        lo, hi = 0, 1
        res = 0
        while hi < len(s):
            cnt[s[hi]] += 1
            mc, c = cnt.most_common(1)[0]
            while hi - lo + 1 - c > k:
                cnt[s[lo]] -= 1
                lo += 1
                mc, c = cnt.most_common(1)[0]
            res = max(res, hi - lo + 1)
            hi += 1
        return res


class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        """Better implementation of solution2, where the max_cnt of the
        letter in the range is obtained in O(1) instead of O(26)

        However, it is crucial to note that max_cnt does NOT always points to
        the max repeats of a letter in the window. We can only be sure that it
        does point to the max repeats whenever it is updated. In other words,
        when it is updated, we obtain the correct res.

        When hi - lo + 1 - max_cnt > k, we increment lo. This will change the
        max repeats in the window, but this change does not affect the next
        iteration, because in the next iteration, as long as max_cnt does not
        increase, we will hit hi - lo + 1 - max_cnt > k regardless. To put it
        in another way, as long as max_cnt does not increase, once we hit
        hi - lo + 1 - max_cnt > k, we will always hit it and always perform
        hi + 1 and lo - 1. This is fine because the max range does not change
        when this happens. It remains the same as the last time it is valid.

        O(N), 236 ms, 18% ranking.
        """
        cnt = Counter(s[0])
        res, max_cnt, lo = 0, 1, 0
        for hi in range(1, len(s)):
            cnt[s[hi]] += 1
            max_cnt = max(max_cnt, cnt[s[hi]])
            if hi - lo + 1 - max_cnt > k:
                cnt[s[lo]] -= 1
                lo += 1
            res = max(res, hi - lo + 1)
        return res
            

sol = Solution3()
tests = [
    ('ABAB', 2, 4),
    ('AABABBA', 1, 4),
    ("ZUOYSIMYEOJCWK", 10, 12),
    ('ABBB', 2, 4),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.characterReplacement(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
