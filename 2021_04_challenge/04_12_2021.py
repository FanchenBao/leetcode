# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """LeetCode 667

        The intuition is that we can always create k unique diffs in the
        first k + 1 numbers. We construct the first k + 1 numbers like this:

        1, k + 1, 2, k, 3, k - 1, 4, k - 2, 5, ...

        Basically, we go 1, 2, 3, ... on all the even indices until index k.
        We go k + 1, k, k - 1, k - 2, ... on all the odd indices until index k.

        O(K), 44 ms, 86% ranking.
        """
        res = list(range(1, n + 1))
        p = 0
        for i in range(0, k + 1, 2):
            res[i] = p + 1
            if i + 1 <= k:
                res[i + 1] = k - p + 1
            p += 1
        return res


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
