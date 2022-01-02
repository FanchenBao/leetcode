# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                return False
        return True
        

sol = Solution()
tests = [
    (10, [3,9,19,5,21], True),
    (5, [4,9,23,4], False)
]

for i, (mass, asteroids, ans) in enumerate(tests):
    res = sol.asteroidsDestroyed(mass, asteroids)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
