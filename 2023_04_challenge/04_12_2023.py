# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def simplifyPath(self, path: str) -> str:
        """LeetCode 71

        Still stack today.

        O(N), 34 ms, faster than 66.29%
        """
        stack = []
        for ele in path.split('/'):
            if ele == '..':
                if stack:
                    stack.pop()
            elif ele != '.' and ele:
                stack.append(ele)
        return '/' + '/'.join(stack)


sol = Solution()
tests = [
    ("/home/", '/home'),
    ('/../', '/'),
    ('/home//foo/', '/home/foo'),
    ("/a/../../b/../c//.//", '/c'),
]

for i, (path, ans) in enumerate(tests):
    res = sol.simplifyPath(path)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
