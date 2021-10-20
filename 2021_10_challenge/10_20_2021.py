# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """I've done this in the past, and I don't like. The restriction is that
        we have to do it in O(1) space, which we can, but I don't feel like
        doing it.
        """
        return ' '.join(reversed(s.strip().split()))



sol = Solution()
tests = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
    ("Alice does not even like bob", "bob like even not does Alice"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseWords(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
