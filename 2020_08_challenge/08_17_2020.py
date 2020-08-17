# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """Pure math"""
        n = num_people
        x = int(math.sqrt(2 * candies + 1 / 4) - 1 / 2)
        q, r = divmod(x, n)
        res = [(i + 1) * q + n * q * (q - 1) // 2 for i in range(n)]
        for j in range(r):
            res[j] += j + 1 + n * q
        res[r] += candies - x * (x + 1) // 2
        return res


class Solution2:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """Brute force. Not any slower than pure math"""
        res = [0] * num_people
        i = 0
        while candies > 0:
            res[i % num_people] += min(i + 1, candies)
            candies -= i + 1
            i += 1
        return res


sol = Solution2()
print(sol.distributeCandies(10, 3))