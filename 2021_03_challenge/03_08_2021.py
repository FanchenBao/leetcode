# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """LeetCode 1332

        This is a quite a meaningless problem. Since what we remove is a
        subsequence, which means we can choose exactly which letters to combine
        and then remove, we might as well remove all the 'a' and then all the
        'b', because all 'a' forms a palindrome, and so does all 'b'. So the
        problem becomes checking whether the given s is a palindrome itself. If
        it is, we return 1, else we always return 2. And one more edge case is
        empty string, where we return 0.

        O(N), 28 ms, 80% ranking.
        """
        return 0 if not s else 1 if s == s[::-1] else 2


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
