# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """LeetCode 387

        139 ms, faster than 70.76%
        """
        counter = Counter(s)
        for i, le in enumerate(s):
            if counter[le] == 1:
                return i
        return -1


sol = Solution()
tests = [
    ('leetcode', 0),
    ('loveleetcode', 2),
    ('aabb', -1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.firstUniqChar(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
