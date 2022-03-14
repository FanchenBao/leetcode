# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        """LeetCode 71

        Split by '/' and ignore empty string allows us to get rid of multiple
        slashes. Also this creates a list of tokens.

        If the token is '.', we can ignore it because nothing happens. If the
        token is '..', we need to ignore the previous folder. This can be done
        in a stack, where the encounter of '..' leads to the pop of the stack,
        if there is something to pop. Otherwise, all tokens are pushed to the
        stack.

        O(N), 36 ms, 82% ranking.
        """
        tokens = path.split('/')
        stack = []
        for tok in tokens:
            if tok and tok != '.':
                if tok != '..':
                    stack.append(tok)
                elif stack:
                    stack.pop()
        return '/' + '/'.join(stack)


sol = Solution()
tests = [
    ("/home/", '/home'),
    ("/../", '/'),
    ("/home//foo/", '/home/foo'),
    ("/./home/../foo", '/foo'),
    ("/./home/../...//../.../..../foo", "/.../..../foo"),
    ('/', '/'),
    ('///', '/'),
]

for i, (path, ans) in enumerate(tests):
    res = sol.simplifyPath(path)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
