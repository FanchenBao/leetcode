# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution:
    def add(self, num1_lst: List[int], num2_lst: List[int]) -> List[int]:
        res = []
        i, j = len(num1_lst) - 1, len(num2_lst) - 1
        c = 0
        while i >= 0 and j >= 0:
            res.append(0)
            s = num1_lst[i] + num2_lst[j] + c
            c, res[-1] = divmod(s, 10)
            i -= 1
            j -= 1
        if i < 0:
            while j >= 0:
                res.append(0)
                s = num2_lst[j] + c
                c, res[-1] = divmod(s, 10)
                j -= 1
        else:
            while i >= 0:
                res.append(0)
                s = num1_lst[i] + c
                c, res[-1] = divmod(s, 10)
                i -= 1
        if c:
            res.append(c)
        return res[::-1]

    def mult_one_digit(self, num_lst: List[int], one_digit: int) -> List[int]:
        res = []
        c = 0
        for i in range(len(num_lst) - 1, -1, -1):
            res.append(0)
            p = num_lst[i] * one_digit + c
            c, res[-1] = divmod(p, 10)
        if c:
            res.append(c)
        return res[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        """LeetCode 43

        Use two helper functions to handle simple operations: add two numbers
        represented by list of integers, multiple one list of integers with a
        one-digit number. Combining these two helper functions, we can find
        the product of num1 and num2 easily.

        However, compared to Solution2, this one feels a bit too cumbersome.
        That said, I think this solution is more intuitive and easier to debug.

        O(MN), 276 ms, 10% ranking.
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1_lst = [int(n) for n in num1]
        num2_lst = [int(n) for n in num2]
        N2 = len(num2_lst)
        res = [0]
        for i, n in enumerate(num2_lst):
            res = self.add(
                res,
                self.mult_one_digit(num1_lst, n) + [0] * (N2 - i - 1),
            )
        return ''.join(str(n) for n in res)


class Solution2:
    def multiply(self, num1, num2):
        """This is the more succinct solution that performs multiplication
        directly. It is from the official solution.

        The key is the insight that the temp result from multiplying ith digit
        from num1 and jth digit from num2 is located at the same position as
        multiplying jth digit from num1 and ith digit from num2. This allows us
        to save the temp result in the same array as the final result.

        O(MN), 108ms, 52% ranking.
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1_lst = [int(n) for n in num1]
        num2_lst = [int(n) for n in num2]
        res = [0] * (len(num1_lst) + len(num2_lst))  # max length of answer
        for i in range(len(num1_lst) - 1, -1, -1):
            c = 0
            for j in range(len(num2_lst) - 1, -1, -1):
                c, res[i + j + 1] = divmod(num1_lst[i] * num2_lst[j] + res[i + j + 1] + c, 10)
            res[i] += c  # extra carry after the current round of mult
        return ''.join(str(n) for n in res).lstrip('0')


sol = Solution2()
num_test = 100
num1_digit = 100
num2_digit = 100
tests = [(randint(10**(num1_digit - 1), 10**(num1_digit)), randint(10**(num2_digit - 1) - 1, 10**(num2_digit))) for _ in range(num_test)]

for i, (num1, num2) in enumerate(tests):
    res = sol.multiply(str(num1), str(num2))
    ans = str(num1 * num2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {(num1, num2)}')
