# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def simplifyPath(self, path: str) -> str:
        """We basically extract the actual contents in between all the slashes.
        We first find the first and last letters of the actual content. THen we
        compare the content to special options '.' and '..'. If it's a '.', we
        don't do anything. If it's a '..', we pop the last two elements of the
        stack (the stack is configured that it will always have a slash at its
        top). Of course, this pop will not happen if there is not enough element
        in the stack to be popped.

        O(N), 28 ms, 89% ranking.
        """
        stack = ['/']
        i, size = 0, len(path)
        while i < size:
            while i < size and path[i] == '/':
                i += 1
            start = i
            while i < size and path[i] != '/':
                i += 1
            content = path[start:i]
            if content == '..':
                if len(stack) >= 3:  # otherwise the stack only has one slash
                    stack.pop()
                    stack.pop()
            elif content and content != '.':
                stack += [content, '/']
        # pop the last slash only when the last slash is NOT the only slash
        if len(stack) >= 3:
            stack.pop()
        return ''.join(stack)


class Solution2:
    def simplifyPath(self, path: str) -> str:
        """We can use split to simplify the logic of stepping through all the
        slashes.
        """
        stack = ['/']
        for cnt in path.split('/'):
            if cnt == '..':
                if len(stack) > 1:  # otherwise the stack only has one slash
                    stack.pop()
                    stack.pop()
            elif cnt and cnt != '.':
                stack += [cnt, '/']
        # pop the last slash only when the last slash is NOT the only slash
        if len(stack) > 1:
            stack.pop()
        return ''.join(stack)


sol = Solution2()
tests = [
    ('/home/', '/home'),
    ('/../', '/'),
    ('/home//foo/', '/home/foo'),
    ('/a/./b/../../c/', '/c'),
    ('/..', '/'),
]

for i, (path, ans) in enumerate(tests):
    res = sol.simplifyPath(path)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
