#! /usr/bin/env python3
# from typing import *
"""08/10/2019

Solution1:
DP solution. To process odd-length and even-length text the same, we add a non-
lowercase symbol '.' to the middle of odd-length text.

DP[1, 2, ..., length//2] represents the max decomposition of i letters counting
away from the center. We want to compute DP[length//2].

As i increases, if the next letter on both sides are equal, then DP[i] =
DP[i - 1] + 2. If not, we search from outside in to find the first matching
words on both side, then DP[i] = DP[i - j - 1] + 2, here j is the number of steps
moving towards center. If no two words match in the search, DP[i] = 1.

Complexity O(n^2). This solution clocked in at 372 ms, while the good ones are
at ~30 ms.


Solution2:
Exact same method as solution1, but drastically reduced the number of string
slices. This solution clocked in at 192 ms, 9.37%


Solution3:
This solution eliminated all splicing, but clocked in around 7%, worse than
solution2.


Solution4:
Greedy. Should've realized this from my DP solution, since I stopped the DP
search at the first instance of matching. This should be a signal for greedy.
My greedy clocked in at 40 ms. More detailed explanation is here:
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/350560/JavaC%2B%2BPython-Easy-Greedy-with-Prove

"""


class Solution1:
    def longestDecomposition(self, text: str) -> int:
        length = len(text)
        if length % 2:  # if odd length, make it even
            text = text[: length // 2] + "." + text[length // 2 :]
            length += 1
        # Now all texts have even length
        dp = [0] * (length // 2 + 1)
        for i in range(1, length // 2 + 1):
            if text[length // 2 - i] == text[length // 2 + i - 1]:
                dp[i] = dp[i - 1] + 2
            else:
                for j in range(1, i):
                    if (
                        text[length // 2 - i : length // 2 - i + j + 1]
                        == text[length // 2 + i - 1 - j : length // 2 + i]
                    ):
                        dp[i] = dp[i - j - 1] + 2
                        break
                else:
                    dp[i] = 1
        return dp[length // 2]


class Solution2:
    def longestDecomposition(self, text: str) -> int:
        length = len(text)
        if length % 2:  # if odd length, make it even
            text = text[: length // 2] + "." + text[length // 2 :]
            length += 1
        # Now all texts have even length
        dp = [0] * (length // 2 + 1)
        for i in range(1, length // 2 + 1):
            if text[length // 2 - i] == text[length // 2 + i - 1]:
                dp[i] = dp[i - 1] + 2
            else:
                for j in range(1, i):
                    if (
                        text[length // 2 + i - 1 - j] == text[length // 2 - i]
                        and text[length // 2 - i : length // 2 - i + j + 1]
                        == text[length // 2 + i - 1 - j : length // 2 + i]
                    ):
                        dp[i] = dp[i - j - 1] + 2
                        break
                else:
                    dp[i] = 1
        return dp[length // 2]


class Solution3:
    def longestDecomposition(self, text: str) -> int:
        length = len(text)
        if length % 2:  # if odd length, make it even
            text = text[: length // 2] + "." + text[length // 2 :]
            length += 1
        # Now all texts have even length
        dp = [0] * (length // 2 + 1)
        for i in range(1, length // 2 + 1):
            if text[length // 2 - i] == text[length // 2 + i - 1]:
                dp[i] = dp[i - 1] + 2
            else:
                for j in range(1, i):
                    if text[length // 2 + i - 1 - j] == text[length // 2 - i]:
                        for k in range(1, j + 1):
                            if (
                                text[length // 2 + i - 1 - j + k]
                                != text[length // 2 - i + k]
                            ):
                                break
                        else:
                            dp[i] = dp[i - j - 1] + 2
                            break
                else:
                    dp[i] = 1
        return dp[length // 2]


class Solution4:
    def longestDecomposition(self, text: str) -> int:
        f, b = 0, len(text) - 1
        res = 0
        i = 0  # records how many steps b has taken walking towards center
        while f < b and b >= len(text) // 2:
            # walk b towards center and check whether any match could occur
            # If a match is possible, do it, reset f and b, and continue.
            if (
                text[f] == text[b]
                and text[f : f + i + 1] == text[b : b + i + 1]
            ):
                res += 2
                f += i + 1
                b -= 1
                i = 0
                continue
            i += 1
            b -= 1
        # check for f <= b in case there is a final piece in the center
        return res + 1 if f <= b else res


# sol = Solution()
# text = "elvtoelvto"
# print(sol.longestDecomposition(text))


def test():
    sol = Solution1()
    # Test case 1
    text = "antaprezatepzapreanta"
    if sol.longestDecomposition(text) == 11:
        print("Test case 1: Pass")
    else:
        print(
            f"Test case 1: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 2
    text = "ghiabcdefhelloadamhelloabcdefghi"
    if sol.longestDecomposition(text) == 7:
        print("Test case 2: Pass")
    else:
        print(
            f"Test case 2: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 3
    text = "aba"
    if sol.longestDecomposition(text) == 3:
        print("Test case 3: Pass")
    else:
        print(
            f"Test case 3: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 4
    text = "merchant"
    if sol.longestDecomposition(text) == 1:
        print("Test case 4: Pass")
    else:
        print(
            f"Test case 4: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 5
    text = "aaa"
    if sol.longestDecomposition(text) == 3:
        print("Test case 5: Pass")
    else:
        print(
            f"Test case 5: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 6
    text = "elvtoelvto"
    if sol.longestDecomposition(text) == 2:
        print("Test case 6: Pass")
    else:
        print(
            f"Test case 6: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 7
    text = "rrstkbncgfdvtszniury"
    if sol.longestDecomposition(text) == 1:
        print("Test case 7: Pass")
    else:
        print(
            f"Test case 7: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )

    # Test case 8
    text = "a"
    if sol.longestDecomposition(text) == 1:
        print("Test case 8: Pass")
    else:
        print(
            f"Test case 8: Fail, wrong answer: {sol.longestDecomposition(text)}"
        )


test()
