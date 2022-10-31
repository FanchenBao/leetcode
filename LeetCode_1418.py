# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """Very straightforward data wrangling problem.

        The tricky part is everything in orders is string, but we have to sort
        tables using the int version. Also the count in the returned result is
        string.

        O(N), 1137 ms, faster than 37.46%

        UPDATE: saw a clever way that uses the `key` kwarg to sort tables by
        integer. 762 ms, faster than 70.91%
        """
        res_dict = defaultdict(Counter)
        food = set()
        for _, t, f in orders:
            res_dict[t][f] += 1
            food.add(f)
        res = [['Table'] + sorted(food)]
        # very smart move by
        # https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/discuss/586566/Clean-Python-3-hashmap-O(N-%2B-TlogT-%2B-FlogF-%2B-T-*-F)
        for t in sorted(res_dict, key=int):
            res.append([t] + [str(res_dict[t][f]) for f in res[0][1:]])
        return res


sol = Solution()
tests = [
    ([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]], [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]),
    ([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]], [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]),
    ([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]], [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]),
]

for i, (orders, ans) in enumerate(tests):
    res = sol.displayTable(orders)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
