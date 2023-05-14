# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        """This one is NOT easy.

        The analysis of the case where giving each child 8 dollars surpass the
        total number of money is quite dense.
        """
        total = children * 8
        if total == money:
            return children
        if total < money:
            return children - 1
        q, r = divmod(total - money, 7)
        res = children - q - int(r != 0)
        # if r == 4, we cannot directly remove from a child, because that child
        # would be left with 4 dollars, which is not allowed. In this case, if
        # we have removed 7 dollars from some previous child, instead of removing
        # 4 dollars, we can remove 5 dollars on the current child and 6 dollars
        # on the previous child. Thus, we won't hurt the remaining 8-dollar
        # children.
        # UNLESS, there are no other child who has 7 dollars removed. In that
        # case, we have to hurt one of the 8-dollar child.
        if r == 4 and q == 0:
            res -= 1
        return res if res >= 0 else -1


sol = Solution()
tests = [
    (20, 3, 1),
    (16, 2, 2),
    (2, 2, 0),
    (1, 2, -1),
    (5, 2, 0),
]

for i, (money, children, ans) in enumerate(tests):
    res = sol.distMoney(money, children)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
