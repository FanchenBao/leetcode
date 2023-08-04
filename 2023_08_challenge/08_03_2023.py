# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """LeetCode 17

        41 ms, faster than 81.43%
        """
        if not digits:
            return []
        digit_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        self.res = []

        def helper(idx: int, letters: str) -> None:
            if idx == len(digits):
                self.res.append(letters)
            else:
                for le in digit_letter_map[digits[idx]]:
                    helper(idx + 1, letters + le)

        helper(0, '')
        return self.res


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
