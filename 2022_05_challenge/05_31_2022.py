# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """LeetCode 1461

        Sliding window to compute each binary code value of length k.

        O(N), 1198 ms
        """
        if len(s) < k:
            return False
        p = 2**(k - 1)
        num = int(s[:k], 2)
        num_set = set([num])
        for i in range(k, len(s)):
            num = ((num - int(s[i - k]) * p) << 1) + int(s[i])
            num_set.add(num)
        return len(num_set) == p * 2


class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """Directly use set on substring

        944 ms, faster than 12.83%
        """
        str_set = set()
        for i in range(k - 1, len(s)):
            str_set.add(s[i - k + 1:i + 1])
        return len(str_set) == 2**k


class Solution3:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """This is the same idea as Solution1, but using bit manipulation to
        compute each new value of k-length binary code faster.

         946 ms, faster than 12.83% 
        """
        if len(s) < k:
            return False
        all_ones = (1 << k) - 1
        num = int(s[:k], 2)
        num_set = set([num])
        for i in range(k, len(s)):
            num = (num << 1) & all_ones | int(s[i])
            num_set.add(num)
        return len(num_set) == all_ones + 1



sol = Solution3()
tests = [
    ("00110110", 2, True),
    ('0110', 1, True),
    ('0110', 2, False),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.hasAllCodes(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
