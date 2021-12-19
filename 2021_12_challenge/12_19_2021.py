# from pudb import set_trace; set_trace()
from typing import List, Tuple


class Solution1:
    def decodeString(self, s: str) -> str:
        """LeetCode 394

        An old question, and an easy medium. I did this more than a year ago
        quite smoothly. This time around, it took me a bit longer than I had
        expected. But the basic concept is recursion. We recurse everytime a
        left bracket is encountered. Of course, before recursion, we shall have
        already obtained the number of repeats. Inside the recursion, we will
        produce a string contained within the brackets. The condition for
        jumping out of the recursion is either s is exhausted or the first right
        bracket is encountered.

        O(N), 28 ms, 83 % ranking.
        """

        def helper(idx: int) -> Tuple[str, int]:
            res = ''
            k, i = idx, idx
            while i < len(s) and s[i] != ']':
                if '0' <= s[i] <= '9':
                    res += s[k:i]
                    count = 0
                    while '0' <= s[i] <= '9':
                        count = count * 10 + int(s[i])
                        i += 1
                    rep, new_idx = helper(i + 1)
                    res += count * rep
                    i = new_idx
                    k = i + 1
                i += 1
            return res + s[k:i], i

        return helper(0)[0]


class Solution2:
    def decodeString(self, s: str) -> str:
        """This is the method I used last year.

        I made small changes, and it runs at 20 ms, 99% ranking.
        """
        stack = []
        for le in s:
            if le == ']':
                rep = ''
                while stack and stack[-1] != '[':
                    rep = stack.pop() + rep
                stack.pop()  # pop '['
                count = ''
                while stack and '1' <= stack[-1] <= '9':
                    count = stack.pop() + count
                stack.append(int(count) * rep)
            else:
                stack.append(le)
        return ''.join(stack)


class Solution3:
    def decodeString(self, s: str) -> str:
        """This must be from the discussion with two stacks
        """
        cur_str, cur_num, str_st, num_st = '', 0, [], []
        for le in s:
            if '0' <= le <= '9':
                cur_num += cur_num * 10 + int(le)
            elif le == '[':
                str_st.append(cur_str)
                num_st.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif le == ']':
                cur_str = str_st.pop() + num_st.pop() * cur_str
            else:
                cur_str += le
        return cur_str


sol = Solution3()
tests = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("abc3[cd]xyz", "abccdcdcdxyz"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.decodeString(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
