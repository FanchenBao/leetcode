# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """Since the size of price, special, and needs are all quite small. It
        is possible to brute force this problem, i.e. iterate all possible
        solutions and pick the one with the lowest price.

        The way I iterate through everything is that for each special, I use it
        0, 1, 2, ... times until any of the needs is exceeded. For each
        repetition of special usage, I have to options going forward: either
        not use any other specials and compute the price of buying the items
        directly. Or continue to use other specials.
        
        I cannot figure out the time complexity.
        """
        self.res = math.inf
        N = len(special)

        def helper(idx: int, cur_needs: List[int], cost: int) -> None:
            if idx == N:
                return
            t = 0
            while True:
                next_needs = []
                for i in range(len(cur_needs)):
                    if cur_needs[i] >= special[idx][i] * t:
                        next_needs.append(cur_needs[i] - special[idx][i] * t)
                    else:
                        return
                # cost of not using any more specials
                c = sum(price[i] * cur for i, cur in enumerate(next_needs))
                self.res = min(self.res, cost + t * special[idx][-1] + c)
                # Use other specials
                helper(idx + 1, next_needs, cost + t * special[idx][-1])
                t += 1

        helper(0, needs, 0)
        return self.res


sol = Solution()
tests = [
    ([2,5], [[3,0,5],[1,2,10]], [3,2], 14),
    ([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1], 11),
]

for i, (price, special, needs, ans) in enumerate(tests):
    res = sol.shoppingOffers(price, special, needs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
