# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution1:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """LeetCode 970

        Very naive approach. Simply set a current x and increment y to see
        whether the sum is smaller or equal to bound. If it is, we add that to
        the result, else we break. The tricky part is the edge case when x or y
        is 1. I have been bitten by many edge cases.

        O(logN * logN), 32 ms, 69% ranking.
        """
        if x == 1 and y == 1:
            return [2] if x + y <= bound else []
        elif x == 1 or y == 1:
            cur = 1
            res = []
            while cur + 1 <= bound:
                res.append(cur + 1)
                cur *= max(x, y)
            return res

        res = set()
        curx = 1
        while curx <= bound:
            cury = 1
            while cury <= bound:
                if curx + cury <= bound:
                    res.add(curx + cury)
                else:
                    break
                cury *= y
            curx *= x

        return list(res)


class Solution2:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """Much better implementation, inspired by the official solution.
        20 ms, 100% ranking !!
        """
        res = set()
        curx = 1
        while curx <= bound:
            cury = 1
            while cury <= bound:
                if curx + cury <= bound:
                    res.add(curx + cury)
                else:
                    break
                cury *= y
                if y == 1:
                    break
            curx *= x
            if x == 1:
                break
        return list(res) 


sol = Solution2()
tests = [
    (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
    (3, 5, 15, [2, 4, 6, 8, 10, 14]),
    (1, 1, 100, [2]),
]

for i, (x, y, bound, ans) in enumerate(tests):
    res = sol.powerfulIntegers(x, y, bound)
    if sorted(res) == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
