# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        """LeetCode 32

        This is not a hard problem if one figures out how the DP works here.
        For each "(", it cannot match anything to the left. For each ")", we
        need to find where its matching "(" is. Let dp[i] be the longest valid
        paren ending at s[i], then the index for a potential match of the
        current ")" must be i - dp[i - 1] - 1. If s[i - 1] == '(', then
        dp[i - 1] = 0, which makes the matching paren for ")" become s[i - 1].
        Otherwise, if s[i - 1] == ')', then i - 1 - dp[i - 1] + 1 is the paren
        that matches s[i - 1], and j = i - 1 - dp[i - 1] + 1 - 1 is the paren in
        front of that matching paren, which is also the paren that we want to
        match s[i]. If this paren is a left, then we have a match for s[i], and
        the longest valid paren is dp[j - 1] + 2 + dp[i - 1]. Otherwise, there
        is no valid paren ending at s[i].

        O(N), 77 ms, faster than 27.14%
        """
        N = len(s)
        if not N:
            return 0
        dp = [0] * N
        for i in range(1, N):
            if s[i] == ')':
                j = i - dp[i - 1] - 1  # index of potential matching left paren
                if j >= 0 and s[j] == '(':
                    dp[i] = 2 + dp[i - 1] + (dp[j - 1] if j - 1 >= 0 else 0)
        return max(dp)


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        """This is the stack solution. We always push "(" onto the stack. Then
        when a ")" shows up and there are "(" in the stack, we always have a
        matching pair. Unmatch happens when the stack is empty but we have a
        ")" at hand. In that case, we simply push that paren into the stack.
        It serves as a sentinel to indicate the next possible mismatch.

        70 ms, faster than 36.57%
        """
        stack, res = [-1], 0  # we must put something in stack initially 
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                # either '(' or ')' gets popped. Doesn't matter. If it's '(',
                # we have a match. If it's ')', stack will become empty, because
                # ')' can only be at the first position
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)  # unmatched ')'
        return res



class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        """This is the O(1) space solution. The intuition is that we go from
        left to right and keep count of the number of '(' and ')'. Whenever the
        count of left paren is smaller than right paren, we have a problem. SO
        we reset the count immediately. Otherwise, whenever the two counts are
        equal, we have found a valid string of paren. We keep track of the 
        largest length. Then we do the same thing going from right to left. The
        only difference now is that we reset the count when the number of right
        is larger than the number of left.

        O(N) time and O(1) space. 80 ms, faster than 23.51% 
        """
        lc = rc = 0
        res = 0
        for p in s:
            if p == '(':
                lc += 1
            else:
                rc += 1
            if lc < rc:
                lc = rc = 0
            elif lc == rc:
                res = max(res, lc + rc)
        lc = rc = 0
        for p in reversed(s):
            if p == '(':
                lc += 1
            else:
                rc += 1
            if lc > rc:
                lc = rc = 0
            elif lc == rc:
                res = max(res, lc + rc)
        return res


sol = Solution3()
tests = [
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("(()())", 6),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestValidParentheses(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
