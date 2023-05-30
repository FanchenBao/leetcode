# from pudb import set_trace; set_trace()
from typing import List
import math


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lot = [0, big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        """LeetCode 1603

        140 ms, faster than 44.63%
        """
        if self.lot[carType]:
            self.lot[carType] -= 1
            return True
        return False


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
