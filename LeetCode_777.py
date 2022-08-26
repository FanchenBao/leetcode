# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def canTransform(self, start: str, end: str) -> bool:
        """A few things to note.

        1. R can only move right until there is no more X on the right.
        2. L can only move left until there is no more X on the left.
        3. Movement of R and L is independent.
        4. If we move the right-most R first, each R only takes one action to
            reach the end position. 
        5. If we move the left-most L first, each L only takes one action to
            reach the end position.

        Based on these observations, we record the indices of R and L on start
        and end. Then we simulate the movement. For R, we move the right-most
        first. For L, we move the left-most first.

        O(N), 1516 ms, faster than 5.03% 
        """
        if len(start) != len(end):
            return False
        r_start, r_end, l_start, l_end = [], [], [], []
        for i, (le_start, le_end) in enumerate(zip(start, end)):
            if le_start == 'R':
                r_start.append(i)
            if le_start == 'L':
                l_start.append(i)
            if le_end == 'R':
                r_end.append(i)
            if le_end == 'L':
                l_end.append(i)
        # print(r_start, r_end, l_start, l_end)
        if len(r_start) != len(r_end) or len(l_start) != len(l_end):
            return False
        list_start = list(start)
        for i, j in zip(r_start[::-1], r_end[::-1]):
            if i > j:
                return False
            for k in range(i + 1, j + 1):
                if list_start[k] != 'X':
                    return False
            list_start[i], list_start[j] = list_start[j], list_start[i]
        for i, j in zip(l_start, l_end):
            if i < j:
                return False
            for k in range(i - 1, j - 1, -1):
                if list_start[k] != 'X':
                    return False
            list_start[i], list_start[j] = list_start[j], list_start[i]
        return True


class Solution2:
    def canTransform(self, start: str, end: str) -> bool:
        """This is inspired by:
        https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/113789/Simple-Java-one-pass-O(n)-solution-with-explaination/114804

        We know that R must go right and L must go left, and R will be blocked
        by another R or L, and the same goes for L as well. This means, if we
        scan from left to right and ignore Xs, the first R/L in start must
        match the first R/L in end, and the index in end must be larger
        than the index in start for R, or smaller for L.

        This way, we can run the check in one pass.

        O(N), 72 ms, faster than 60.75%
        """
        N, M = len(start), len(end)
        if M != N:
            return False
        i = j = 0
        while True:
            while i < M and start[i] == 'X':
                i += 1  # skip all Xs, find the next R/L
            while j < N and end[j] == 'X':
                j += 1  # skip all Xs, find the next R/L
            if (i == M) ^ (j == N):  # the count of R/L does not match
                return False
            if i == M and j == N:
                break
            if start[i] != end[j]:
                return False
            if start[i] == 'R' and i > j:  # R must move right
                return False
            if start[i] == 'L' and i < j:  # L must move left
                return False
            i += 1
            j += 1
        return True


sol = Solution2()
tests = [
    ("RXXLRXRXL", "XRLXXRRLX", True),
    ("X", "L", False),
    ("RXXLRXRXL", "XXRLXXRRL", True),
]

for i, (start, end, ans) in enumerate(tests):
    res = sol.canTransform(start, end)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
