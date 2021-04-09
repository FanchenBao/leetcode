# from pudb import set_trace; set_trace()
from typing import List


class Solution1:

    digit_letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """LeetCode 17.

        Easy problem. Create a mapping from each digit to the letters it
        represents. Iterate through each digit in digits, and incrementally add
        the new letter to each of the result from the previous round.

        O(N^3), 28 ms, 81% ranking
        """
        if not digits:
            return []
        res = ['']
        for d in digits:
            res = [r + le for r in res for le in self.digit_letter[d]]
        return res


class Solution2:

    digit_letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """Backtracking solution.
        """
        res = []
        N = len(digits)

        def helper(idx: int, temp: List[int]):
            if idx == N:
                if temp:
                    res.append(''.join(temp))
                return
            for le in self.digit_letter[digits[idx]]:
                temp.append(le)
                helper(idx + 1, temp)
                temp.pop()  # backtracking

        helper(0, [])
        return res


sol = Solution2()
tests = [
    ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
    ('', []),
    ('2', ['a', 'b', 'c'])
]

for i, (digits, ans) in enumerate(tests):
    res = sol.letterCombinations(digits)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
