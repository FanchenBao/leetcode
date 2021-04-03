# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        """LeetCode 32

        I had not expected that LeetCode would throw three hard questions in
        five days. I have done this one before, back in 10/05/2018. But I am
        certain that I have forgotten the solution all together. Fortunately, I
        was able to crack this one. The key is to identify when a valid
        parenthesis string gets interrupted by an unmatched left or right paren.
        We can traverse the string from left to right to identify the unmatched
        right paren. Then we can go right to left to identify the unmatched left
        paren. Once they are identified, we can swap them with a unique flag,
        such as '*'. These flags indicate a breakage of valid paren string.

        Of course, this algorithm can be run in one fewer pass, because if we
        run right to left first, then running left to right is sufficient to
        both identify the flag and the unmatched right paren.

        O(N), 48 ms, 44% ranking.
        """
        lst = list(s)
        stack = []
        for j in range(len(lst) - 1, -1, -1):
            if lst[j] == ')':
                stack.append(lst[j])
            else:
                if stack:
                    stack.pop()
                else:
                    lst[j] = '*'
        stack = []
        res, cur = 0, 0
        for le in lst + ['*']:
            if le == '(':
                stack.append(le)
            else:
                if stack and le == ')':
                    stack.pop()
                    cur += 2
                else:
                    res = max(res, cur)
                    cur = 0
        return res


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        """DP solution from the official solution.

        dp[i] is the longest valid parenthesis ending at s[i]. If s[i] == '(',
        dp[i] = 0, because a valid paren cannot end in '('.

        If s[i] == ')', there are two scenarios. Either we have a '()' or '))'.
        If it's '()', then dp[i] = dp[i - 2] + 2, which means we find the
        longest valid paren right before the '(', and add 2 to it, since we now
        have a new valid paren.

        If it's '))', then we need to find the letter right before the longest
        valid paren of the right paren in front of us. This means we need to
        check s[i - dp[i - 1] - 1]. This paren can either be '(' or ')'. If it
        is a ')', then the current ')' has no match. Else, we have a match, and
        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2, which is to say we find
        the longest paren right before the matching '(', add on top of that the
        longest paren of ')' in front of us, and plus 2.

        The result is the max of dp.
        """
        dp = [0] * (len(s))
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i] == ')' and s[i - 1] == ')':
                idx = i - dp[i - 1] - 1
                if idx >= 0 and s[idx] == '(':
                    dp[i] = dp[i - 1] + dp[idx - 1] + 2
        return max(dp) if dp else 0


class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        """The easiest solution. It uses stack. The key intuition is we need to
        set up deliminator in the stack, which serves as the new starting point
        when an unmatched paren is encountered. Thus, if an unmatched ')' is
        encountered, we push its index in, because it is the deliminator for a
        new start. For '(', we always push its index. So depending on whether it
        is matched, its index is always in the stack.

        Deliminator, that is the key idea here. And that is also why we need to
        start from -1, since it is a deliminator as well.
        """
        stack, res = [-1], 0
        for i, le in enumerate(s):
            if le == '(':
                stack.append(i)
            else:
                # always pop, because either ')' match or it is a new
                # deliminator. We only need to have one deliminator in stack
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


sol = Solution3()
tests = [
    ('', 0),
    ('()', 2),
    ('(())', 4),
    ('(', 0),
    ('(()())', 6),
    ('(()()', 4),
    (')()())', 4),
    ('(()', 2),
    ('()(()', 2),
    ('())()', 2),
    ('))))())()()(()', 4),
    ('(()))())(', 4),
    (')()())', 4),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestValidParentheses(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
