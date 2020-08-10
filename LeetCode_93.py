#! /usr/bin/env python3
"""07/20/2019

Solution1 is naive recursion, using DFS method. The intuition is that for each
number position, we can have one, two, or three digits. Once we pick one, we
keep searching until the search fails or succeeds. If it succeeds, we record
the outcome. Then we backtrack to check on the next option. A sanity check to
see whether the remaining length of s exceeds the maximum possible for IP
address greatly reduces computation time (it actually saved this algorithm from
being timed out to clocking at 36 ms and 90%).

Solution2 is iterative. I saw a post in the discussion mention this method and
coded it myself. It divides s into four parts and uses three loops to check
whether each part can be fit with one, two, or three-digit IP address number.
The backtrack mentality is still in use in this method.
"""
from typing import List


class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res: List[List[str]] = []
        self.helper(s, 4, res, [])
        return [".".join(r) for r in res]

    def helper(
        self, s: str, remain: int, res: List[List[str]], temp: List[str]
    ) -> None:
        if remain == 0 and len(s) == 0:
            res.append(temp[:])
        else:
            if (
                len(s) <= 3 * remain
            ):  # sanity check, important to reduce runtime
                if len(s) >= 1:
                    temp.append(s[:1])
                    self.helper(s[1:], remain - 1, res, temp)
                    temp.pop()
                if len(s) >= 2 and "10" <= s[:2] <= "99":
                    temp.append(s[:2])
                    self.helper(s[2:], remain - 1, res, temp)
                    temp.pop()
                if len(s) >= 3 and "100" <= s[:3] <= "255":
                    temp.append(s[:3])
                    self.helper(s[3:], remain - 1, res, temp)
                    temp.pop()


class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res: List[List[str]] = []
        temp = []
        length = len(s)
        for i in range(1, 4):
            if self.isValid(s[:i], i) and length - i <= 9:
                temp.append(s[:i])
                for j in range(i + 1, i + 4):
                    if self.isValid(s[i:j], j - i) and length - j <= 6:
                        temp.append(s[i:j])
                        for k in range(j + 1, j + 4):
                            if self.isValid(s[j:k], k - j) and length - k <= 3:
                                temp.append(s[j:k])
                                if self.isValid(s[k:], length - k):
                                    res.append(temp + [s[k:]])
                                temp.pop()
                        temp.pop()
                temp.pop()
        return [".".join(r) for r in res]

    def isValid(self, s: str, length: int) -> bool:
        return (
            (length == 1)
            or (length == 2 and "10" <= s <= "99")
            or (length == 3 and "100" <= s <= "255")
        )


sol = Solution2()
print(sol.restoreIpAddresses("25525511135"))
