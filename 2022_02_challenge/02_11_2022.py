# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """LeetCode 567

        Sliding window with counter. I have seen similar method used in other
        problems before. And the use of array as counter is easier to operate
        compared to using Counter, because of the ease in equality comparison.

        O(N), where N = len(s2), 106 ms, 59% ranking.
        """
        if len(s1) > len(s2):
            return False
        s1cnt, windowcnt = [0] * 26, [0] * 26
        M = len(s1)
        for le in s1:
            s1cnt[ord(le) - 97] += 1
        for i, le in enumerate(s2):
            windowcnt[ord(le) - 97] += 1
            if i >= M:
                windowcnt[ord(s2[i - M]) - 97] -= 1
            if windowcnt == s1cnt:
                return True
        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """This is from the official solution. Same sliding window with counter,
        but the comparison between windowcnt and s1cnt can be shorted to O(1)
        instead of O(26)

        91 ms, 68% ranking.
        """
        if len(s1) > len(s2):
            return False
        s1cnt, windowcnt = [0] * 26, [0] * 26
        M = len(s1)
        for i in range(M):
            s1cnt[ord(s1[i]) - 97] += 1
            windowcnt[ord(s2[i]) - 97] += 1
        count = 0
        for i in range(26):
            count += s1cnt[i] == windowcnt[i]
        for i in range(M, len(s2)):
            if count == 26:  # all letter frequencies match
                return True
            rmidx = ord(s2[i - M]) - 97
            if windowcnt[rmidx] == s1cnt[rmidx]:
                count -= 1
            elif windowcnt[rmidx] == s1cnt[rmidx] + 1:
                count += 1
            windowcnt[rmidx] -= 1
            adidx = ord(s2[i]) - 97
            if windowcnt[adidx] == s1cnt[adidx]:
                count -= 1
            elif windowcnt[adidx] == s1cnt[adidx] - 1:
                count += 1  
            windowcnt[adidx] += 1
        return count == 26


sol = Solution2()
tests = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ('a', 'a', True),
    ('aa', 'baab', True),
    ("hello", "ooolleoooleh", False),
]

for i, (s1, s2, ans) in enumerate(tests):
    res = sol.checkInclusion(s1, s2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
