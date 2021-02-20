# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        """LeetCode 1249

        We run the generic stack operation to check the validity of all the
        parentheses in the string. We do not have to push any letter into the
        stack, nor the actual parenthesis. We only need to push the index of
        the left parenthesis into the stack. Whenever a rigth parenthesis
        appears, we check whether the stack is empty. If it is not, then by the
        rule of the operation, we can be sure that the top of the stack must be
        a left parenthesis. We have a valid match, and we can pop the top of the
        stack. If the stack is empty, that means the right parenthesis is
        invalid and we need to note down its index. At the end, any left
        parenthesis left in the stack are also invalid. We pool together all the
        invalid indices, and based on that we can produce a valid string.

        It is also worth noting that since the parenthesis validation procedure
        naturally assumes maximum number of valid parentheses, any invalid
        parenthesis it finds are the minimum number of parentheses to remove.

        O(N), 116 ms, 71% ranking.
        """
        stack, removed = [], set()
        for i, le in enumerate(s):
            if le == '(':
                stack.append(i)
            elif le == ')':
                if stack:
                    stack.pop()
                else:
                    removed.add(i)
        res = ''
        removed |= set(stack)
        for i, le in enumerate(s):
            if i not in removed:
                res += le
        return res


class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        """The same main concept, but less memory use, because we do not need to
        create new sets to hold the invalid indices. Instead, we simply reset
        invalid parenthesis to an empty string, and use join() to recreate the
        valid string. Good solution.

        Reference: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100

        O(N), 68 ms, 99% ranking.

        I am initially shocked by the performance. But come to think of it, it
        is understandable, because this solution has no extra operations with
        a set. Every time we add something to a set, although it is O(1), the
        system still has to manage a hashmap. And that takes time. This solution
        completely avoids it, hence it is super duper fast. Plus it saves on
        memory as well.
        """
        s_lst, stack = list(s), []
        for i, le in enumerate(s):
            if le == '(':
                stack.append(i)
            elif le == ')':
                if stack:
                    stack.pop()
                else:
                    s_lst[i] = ''
        for i in stack:
            s_lst[i] = ''
        return ''.join(s_lst)


sol = Solution2()
tests = [
    ('lee(t(c)o)de)', 'lee(t(c)o)de'),
    ('a)b(c)d', 'ab(c)d'),
    ('))((', ''),
    ('(a(b(c)d)', 'a(b(c)d)'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minRemoveToMakeValid(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
