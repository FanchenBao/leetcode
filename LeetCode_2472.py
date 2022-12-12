# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def maxPalindromes(self, s: str, k: int) -> int:
        """It works! I am surprised and happy.

        The DP idea is specified in the definition of DP below. At each s[i],
        we need to find all possible palindromes ending at s[i]. Each such
        palindrome represents a partition. Then we just need to find the max
        number of palindrome substrings that corresponds to each partition.

        The edge cases are when k = 1, where a single letter can be a legit
        palindrome. And when k <= 2, where a substring like "aa" can be a legit
        palindrome. For all the other cases, we need to check all the palindrome
        scenarios of s[i - 1], because the only way to form a new palindrome
        ending at s[i] is to have the letter right before the paldinrome ending
        at s[i - 1] equal to s[i].

        For each palindrome ending at s[i], we need to check the max number of
        substrings right before the current palindrome ending at s[i]. Here is
        a very important trick. If at s[i] we have the number of substrings
        smaller than at s[i - 1], we keep the larger in the DP. This is
        important and can be illustrated as such.

        Say at s[i - 1], it can form a palindrome with s[j]. So now we need to
        compare s[j - 1] and s[i]. If they are the same, then we have a new
        palindrome from s[j - 1] to s[i]. Then we need to know the max number of
        legit substrings from s[0] to s[j - 2]. It is likely that the max is
        reached somewhere between s[0] and s[j - 2]. If we only keep in the DP
        the exact number of legit substrings at each letter, we will have to
        run another loop searching from j - 2 to 0 to find the max. However, we
        can also keep track the max at each letter. Then, we only need to check
        dp[j - 2] to find the max substring from s[0] to s[j - 2].

        O(N^2), 3481 ms, faster than 28.94%
        """
        # Definition of dp[i] = (
        #   all previous indices such that s[dp[i][0]:i + 1] is a palindrome,
        #   max substrings that satisfy the requirement ending in s[i]
        # )
        dp = [[[0], int(k == 1)]]
        for i in range(1, len(s)):
            dp.append([[i], 0])
            if k == 1:
                dp[-1][1] = max(dp[-1][1], 1 + dp[i - 1][1])
            if s[i] == s[i - 1]:
                dp[-1][0].append(i - 1)
                if k <= 2:
                    dp[-1][1] = max(dp[-1][1], 1 + (dp[i - 2][1] if i - 2 >= 0 else 0))
            for j in dp[i - 1][0]:
                if j - 1 >= 0 and s[j - 1] == s[i]:
                    dp[-1][0].append(j - 1)
                    if i - j + 2 >= k:
                        dp[-1][1] = max(dp[-1][1], 1 + (dp[j - 2][1] if j - 2 >= 0 else 0))
            dp[-1][1] = max(dp[-1][1], dp[-2][1])
        return dp[-1][1]


class Solution2:
    def maxPalindromes(self, s: str, k: int) -> int:
        """This is the solution from
        https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/discuss/2809293/C%2B%2B-Both-DP-%2B-Greedy-Solution-Explained-Clean-Code\

        Man, this solution has deconstructed the problem so much that it makes
        it look almost too easy.

        Two steps. First, we create a DP table where dp[i][j] records whether
        s[i:j + 1] is a palindrome.

        Then we run a top down DP to find the max substring from s[i] to the
        end. At each step, we either not take s[i], or take s[i]. When we take
        s[i], we need to find all the palindromes starting from s[i] with length
        larger or equal to k, and find all of their count of substring.

        This might not be fast, but it is really simple.

        O(N^2), 8559 ms, faster than 5.02%
        """
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1):
            for i in range(N):
                j = i + l - 1
                if j < N:
                    if i == j:
                        dp[i][j] = True
                    elif i + 1 == j:
                        dp[i][j] = s[i] == s[j]
                    else:
                        dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])


        @lru_cache(maxsize=None)
        def solve(idx: int) -> int:
            if idx >= N:
                return 0
            res = solve(idx + 1)  # not take s[idx]
            for j in range(idx + k - 1, N):
                if dp[idx][j]:
                    res = max(res, 1 + solve(j + 1))
            return res

        return solve(0)


class Solution3:
    def maxPalindromes(self, s: str, k: int) -> int:
        """This is the greedy version
        https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/discuss/2809337/PythonC%2B%2B-recursive-and-iterative-DP-solutions-(explained)

        Same set up as Solution2, but we don't have to go through each index
        in the solve function. We only need to check the smallest possible
        palindrome. Because if we have a palindrome longer than k, it is always
        better to just consider the smaller palindrome of length k (consider
        palindromes of longer lengths does not increase the chance of finding
        new palindromes). This is the greedy part.

        O(N^2), and TLE!!
        """
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1):
            for i in range(N):
                j = i + l - 1
                if j < N:
                    if i == j:
                        dp[i][j] = True
                    elif i + 1 == j:
                        dp[i][j] = s[i] == s[j]
                    else:
                        dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])


        @lru_cache(maxsize=None)
        def solve(idx: int) -> int:
            if idx + k - 1 >= N:
                return 0
            res = solve(idx + 1)  # not take s[idx]
            if dp[idx][idx + k - 1]:
                # length k
                res = max(res, 1 + solve(idx + k))
            if idx + k < N and dp[idx][idx + k]:
                # length k + 1, we need both to handle even and odd palindrome
                res = max(res, 1 + solve(idx + k + 1))
            return res

        return solve(0)


class Solution4:
    def maxPalindromes(self, s: str, k: int) -> int:
        """We shall not use a DP table to store the palindrome info. We can just
        compute it on demand.

        O(NK), 111 ms, faster than 61.13%
        """
        N = len(s)

        def is_pal(i: int, j: int) -> bool:
            if j < N and s[i:j + 1] == s[i:j + 1][::-1]:
                return True
            return False

        @lru_cache(maxsize=None)
        def solve(idx: int) -> int:
            if idx + k - 1 >= N:
                return 0
            res = solve(idx + 1)  # not take s[idx]
            if is_pal(idx, idx + k - 1):
                # length k
                res = max(res, 1 + solve(idx + k))
            if is_pal(idx, idx + k):
                # length k + 1, we need both to handle even and odd palindrome
                res = max(res, 1 + solve(idx + k + 1))
            return res

        return solve(0)


sol = Solution4()
tests = [
    ("abaccdbbd", 3, 2),
    ("adbcda", 2, 0),
    ("a", 1, 1),
    ("aaaaaaa", 1, 7),
    ("aaaaaaa", 2, 3),
    ("aaaaaaa", 3, 2),
    ("aaaaaaa", 4, 1),
    ("aaaaaaa", 5, 1),
    ("aaaaaaa", 6, 1),
    ("aaaaaaa", 7, 1),
    ("aabaaaa", 2, 3),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.maxPalindromes(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
