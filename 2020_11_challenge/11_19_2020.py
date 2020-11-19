# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def decodeString(self, s: str) -> str:
        """33% ranking.

        Pretty standard solution using stack.
        """
        stack = []
        for le in s:
            if le == ']':
                expand = ''
                while stack and stack[-1] != '[':
                    expand = stack.pop() + expand
                stack.pop()  # pop '['
                times = ''
                while stack and '0' <= stack[-1] <= '9':
                    times = stack.pop() + times
                stack += list(expand * int(times))
            else:
                stack.append(le)
        return ''.join(stack)


class Solution2:
    def decodeString(self, s: str) -> str:
        """A seemingly faster solution with only one pass, using stack.

        However it also came out with 34% ranking, which means our old method
        was not significantly slower than this. This is mostly because the test
        case is fairly small (the input string is no longer than 300 chars),
        thus the extra while loop in Solution 1 executes in almost O(1) time.

        Borrowed from:
        https://leetcode.com/explore/featured/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3536/discuss/87662/Python-solution-using-stack
        """
        str_stack = []
        num_stack = []
        cur_str = ''
        cur_num = 0
        for le in s:
            if le == '[':
                str_stack.append(cur_str)
                num_stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif le == ']':
                cur_str = str_stack.pop() + cur_str * num_stack.pop()
            elif '0' <= le <= '9':
                cur_num = cur_num * 10 + int(le)
            else:
                cur_str += le
        return cur_str


sol = Solution2()
tests = [
    ('3[a]2[bc]', 'aaabcbc'),
    ('3[a2[c]]', 'accaccacc'),
    ('2[abc]3[cd]ef', 'abcabccdcdcdef'),
    ('abc3[cd]xyz', 'abccdcdcdxyz'),
    ('a', 'a'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.decodeString(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
