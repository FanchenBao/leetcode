# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """LeetCode 929

        Very straightforward method. We first obtain local and domain names
        by splitting on '@'. Domain name remains as is, but local name needs to
        be parsed by first splitting on '+' to obtain the real part of the local
        name. Then within the real part, we swap the '.' with empty string.

        O(N), N is the total number of letters in emails.
        44 ms, 95% ranking.
        """
        ads = defaultdict(set)
        for em in emails:
            local, domain = em.split('@')
            ads[domain].add(local.split('+')[0].replace('.', ''))
        return sum(len(val) for val in ads.values())


sol = Solution()
tests = [
    (['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com'], 2),
    (['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com'], 3),
]

for i, (emails, ans) in enumerate(tests):
    res = sol.numUniqueEmails(emails)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
