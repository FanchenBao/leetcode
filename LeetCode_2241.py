# from pudb import set_trace; set_trace()
from typing import List


class ATM:

    def __init__(self):
        """The wording definitely can be better. And it's quite a silly problem
        We simply try the banknotes from the highest denomination to the lowest
        and take as many high nodes as possible until we examine all banknotes.
        If the amount turns to zero, we have succeeded in the withdraw.
        Otherwise, the withdraw shall be rejected.

        936 ms, faster than 5.02%
        """
        self.cash = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, b in enumerate(banknotesCount):
            self.cash[i] += b

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i, b in [(4, 500), (3, 200), (2, 100), (1, 50), (0, 20)]:
            if self.cash[i]:
                q, r = divmod(amount, b)
                if q >= self.cash[i]:
                    res[i] += self.cash[i]
                    amount -= b * self.cash[i]
                    self.cash[i] = 0
                else:
                    res[i] += q
                    amount -= q * b
                    self.cash[i] -= q
        if not amount:
            return res
        for i, r in enumerate(res):
            self.cash[i] += r
        return [-1]


class ATM:

    def __init__(self):
        """Easier implementation from:

        https://leetcode.com/problems/design-an-atm-machine/discuss/1953722/Check-then-withdraw
        """
        self.cash = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, b in enumerate(banknotesCount):
            self.cash[i] += b

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i, b in [(4, 500), (3, 200), (2, 100), (1, 50), (0, 20)]:
            res[i] += min(self.cash[i], amount // b)
            amount -= b * res[i]
            self.cash[i] -= res[i]
        if not amount:
            return res
        for i, r in enumerate(res):
            self.cash[i] += r
        return [-1]


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
