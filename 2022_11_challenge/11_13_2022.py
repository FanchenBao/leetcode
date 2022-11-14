# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def reverseWords(self, s: str) -> str:
        """LeetCode 151

        This is the naive solution, not O(1) extra space

        65 ms, faster than 42.05%
        """
        return ' '.join(w for w in s.split(' ')[::-1] if w)


class Solution2:
    def reverseWords(self, s: str) -> str:
        """Forgot about the trick of doing split with no argument to remove
        all spaces
        """
        return ' '.join(s.split()[::-1])


class Solution3:
    def reverseWords(self, s: str) -> str:
        """in place
        
        Definitely not the easiest to code up.

        O(1) extra space. 68 ms, faster than 35.12%
        """
        lst = list(s)


        def reverse(start: int, end: int) -> None:
            i, j = start, end
            while i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        # remove extra spaces
        i = j = 0
        while True:
            while j < len(lst) and lst[j] == ' ':
                j += 1
            if j == len(lst):
                break
            jj = j
            while j < len(lst) and lst[j] != ' ':
                j += 1
            for d in range(jj, j):
                lst[i] = lst[d]
                i += 1
            if i < len(lst):
                lst[i] = ' '
                i += 1
        i -= 1
        while i >= 0 and lst[i] == ' ':
            i -= 1
        new_len = i + 1  # length of the new string

        # reverse individual word
        i = 0
        for j in range(new_len):
            if lst[j] == ' ':
                reverse(i, j - 1)
                i = j + 1
        reverse(i, new_len - 1)
        # reverse the entire string
        reverse(0, new_len - 1)
        return ''.join(lst[:new_len])


sol = Solution3()
tests = [
    # ("the sky is blue", "blue is sky the"),
    # ("  hello world  ", "world hello"),
    # ("a good   example", "example good a")
    (" asdasd df f", "f df asdasd"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseWords(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
