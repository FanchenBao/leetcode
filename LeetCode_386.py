# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def lexicalOrder(self, n: int) -> List[int]:
        """We know 1 must be at the beginning. Then for each subsequent value,
        we check what should be the next value to append to the res. To do that
        we obtain the last value in res. The first check should be res[-1] * 10
        If this is possible, we append it and loop again. If it is not possible,
        then the next value could be res[-1] + 1. Then we check the valididty
        of res[-1] + 1. There are two scenarios that will make res[-1] + 1 
        invalid. One, res[-1] + 1 is too big; and two res[-1] + 1 is divisible
        by 10. Either these two scenarios are encountered, we need to remove
        the last digit of res[-1] and try again. The reason for the first
        scenario is quite straightforward. The reason for the second scenario is
        that we are incrementing the digit to the left. We don't want to do this
        because we might miss other values in between. We continue chopping off
        the last digit, until a value becomes valid.

        O(n), 128 ms, 48% ranking.
        """
        res = [1]
        while len(res) < n:
            if res[-1] * 10 <= n:
                res.append(res[-1] * 10)
            else:
                temp = res[-1]
                while temp + 1 > n or (temp + 1) % 10 == 0:
                    temp //= 10
                res.append(temp + 1)
        return res


class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        """This is a good solution, treating the problem as a tree. For each
        value, it has potentially 10 children. We DFS each tree and add the
        children from small to big.

        Ref: https://leetcode.com/problems/lexicographical-numbers/discuss/86231/Simple-Java-DFS-Solution

        O(N), 196 ms.
        """
        res = []

        def dfs(cur: int) -> None:
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                if cur * 10 + i > n:
                    return
                dfs(cur * 10 + i)

        for i in range(1, 10):
            dfs(i)
        return res


sol = Solution2()
tests = list(range(1, 1000))
# tests = [10]

for i, n in enumerate(tests):
    res = sol.lexicalOrder(n)
    ans = [int(s) for s in sorted(str(i) for i in range(1, n + 1))]
    if res != ans:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
