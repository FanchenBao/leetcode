# from pudb import set_trace; set_trace()
from typing import List
import math
import re


class Solution:
    def maskPII(self, s: str) -> str:
        """40 ms, faster than 75.18% 
        """
        if '@' in s:
            # email
            name, domain = s.lower().split('@')
            return name[0] + '*' * 5 + name[-1] + '@' + domain
        else:
            # phone
            num_str = re.sub('[\(\)\-\+\s]', '', s)
            local = num_str[-10:]
            country = num_str[:-10]
            return ('+' + '*' * len(country) + '-' if country else '') + '*' * 3 + '-' + '*' * 3 + '-' + local[-4:]



sol = Solution()
tests = [
    ("LeetCode@LeetCode.com", "l*****e@leetcode.com"),
    ("AB@qq.com", "a*****b@qq.com"),
    ("1(234)567-890", "***-***-7890"),
    ("+123(234)567(890)", "+**-***-***-7890"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.maskPII(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
