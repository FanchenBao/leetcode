# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """96% ranking. Use stack."""
        right, left = [], []
        for i, ast in enumerate(asteroids):
            if ast > 0:
                right.append(ast)
            else:
                while right:
                    top = right.pop()
                    if top > -ast:
                        right.append(top)
                        break
                    elif top == -ast:
                        ast = 0
                        break
                    # if top < -ast, keep popping right
                if not right and ast:
                    left.append(ast)
        return left + right


class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Better stack"""
        res = []
        for ast in asteroids:
            while res and ast < 0 < res[-1]:
                if res[-1] < -ast:
                    res.pop()
                elif res[-1] == -ast:
                    res.pop()
                    break
                else:  # res[-1] > -ast
                    break
            else:
                res.append(ast)
        return res


sol = Solution2()
tests = [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),
]

for i, (asteroids, ans) in enumerate(tests):
    res = sol.asteroidCollision(asteroids)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
