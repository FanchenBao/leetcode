# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        """LeetCode 17

        Recursion is sufficient.

        45 ms, faster than 42.53%
        """
        h = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def helper(idx: int) -> List[str]:
            if idx == len(digits) - 1:
                return list(h[digits[idx]])
            return [le + r for le in h[digits[idx]] for r in helper(idx + 1)]

        return helper(0) if digits else []


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        """Backtracking

        45 ms, faster than 42.53%
        """
        h = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def helper(idx: int, cur: List[str]) -> None:
            if idx == len(digits):
                res.append(''.join(cur))
            else:
                for le in h[digits[idx]]:
                    cur.append(le)
                    helper(idx + 1, cur)
                    cur.pop()  # backtracking
        if digits:
            helper(0, [])
        return res


class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        """Rolling combination

        42 ms, faster than 51.23% 
        """
        if not digits:
            return []
        h = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = list(h[digits[0]])
        for d in digits[1:]:
            temp = []
            for r in res:
                for le in h[d]:
                    temp.append(r + le)
            res = temp
        return res


sol = Solution3()
tests = [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("", []),
    ("2", ["a","b","c"]),
]

for i, (digits, ans) in enumerate(tests):
    res = sol.letterCombinations(digits)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
