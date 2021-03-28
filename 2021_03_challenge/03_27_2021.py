# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def countSubstrings(self, s: str) -> int:
        """LeetCode 647

        We simply check length of 1 all the way to length of len(s). For each
        length, we traverse the entirty of s, taken substring of the
        corresponding size. Since the size of s is only 1000, this method works.

        O(N^2), 672 ms, 8% ranking.

        Based on the ranking, it seems that there exists a better solution.
        """
        res = len(s)
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                substr = s[i:i + l]
                if substr == substr[::-1]:
                    res += 1
        return res


class Solution2:
    def countSubstrings(self, s: str) -> int:
        """TLE. Apparently, splicing has some internal optimization.
        """
        res = len(s)
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                left, right = i, i + l - 1
                while left < right:
                    if s[left] != s[right]:
                        break
                    left += 1
                    right -= 1
                else:
                    res += 1
        return res


class Solution3:
    def countSubstrings(self, s: str) -> int:
        """This one has much better performance. Although the worst case is
        still O(N^2) when s consists of the same letter, on average it has close
        to O(N) performance because the expansion will not cover the entire
        string.

        The idea is to treat each letter in s or each position between two
        letters as the center of a potential palindrom. Then we expand left and
        right-ward and count how many palindromes can we form for each center.
        To faciltate this operation, we artificially insert a dummy letter to
        unity both odd-number and even-number palindromes.

        O(N^2) worst case, O(N) best case. Average case O(N).
        248 ms, 49% ranking.
        """
        s_ = '#'.join(list(s))
        N, res = len(s_), 0
        for i in range(N):
            left, right = i, i
            while left >= 0 and right < N and s_[left] == s_[right]:
                if s_[left] != '#':
                    res += 1
                left -= 1
                right += 1
        return res


sol = Solution3()
tests = [
    ('abc', 3),
    ('abac', 5),
    ('aaa', 6)
]

for i, (s, ans) in enumerate(tests):
    res = sol.countSubstrings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
