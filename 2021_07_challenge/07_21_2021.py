# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def pushDominoes(self, dominoes: str) -> str:
        """LeetCode 838

        This problem reminds us of matching parenthesis. We use a stack to
        keep track whether there is an unmatched R. If the current domino is L,
        there are two scenarios in the stack: stack has an R or stack is empty.
        If stack has an R, then we know from the R in the stack to L, we can
        form an enclosed pair, and the states of all dominoes within this
        enclosure can be easily computed. If the stack is empty, that means
        everything from the current end of res towards the current L must all be
        L.

        If the current domino is R, there are the same two scenarios. If the
        stack has an R in it, then everything from that R towards the current R
        must all be R. If the stack is empty, then everything from the end of
        res towards the current R must all be '.'.

        If the current domino is '.', we skip.

        O(N), 184 ms, 60% ranking.
        """
        stack = []
        res = ''
        for i, d in enumerate(dominoes):
            if d == 'L':
                if not stack:
                    res += 'L' * (i - len(res) + 1)
                else:  # stack has R in it
                    quo, rem = divmod(i - stack.pop() + 1, 2)
                    res += 'R' * quo + '.' * rem + 'L' * quo
            elif d == 'R':
                if not stack:
                    res += '.' * (i - len(res))
                else:  # stack has R in it
                    res += 'R' * (i - stack.pop())
                stack.append(i)
        remains = len(dominoes) - len(res)
        return res + ('R' * remains if stack else '.' * remains)


class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        """This is the same concept as the first solution in the official
        solution, but we will do it in the way of DBabichev:

        https://leetcode.com/problems/push-dominoes/discuss/1352252/Python-simulate-process-explained

        The basic idea is to find L-R pairs. It can either be LL, LR, RL, or RR.
        For each pair, we can easily compute the state of the dominoes in
        between. We ignore all the '.' dominoes at the beginning. Also, we need
        to add dummy dominoes L and R to the left and right side, respectively.
        """
        dominoes = 'L' + dominoes + 'R'
        res, j = '', 0
        for i in range(1, len(dominoes)):
            if dominoes[i] == '.':
                continue
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * (i - j)
            elif dominoes[i] < dominoes[j]:  # RL
                quo, rem = divmod(i - j + 1, 2)
                res += 'R' * (quo - 1) + '.' * rem + 'L' * quo
            else:  # LR
                res += '.' * (i - j - 1) + 'R'
            j = i
        # we always include the right side of the L-R pair, so res is one bigger
        # than it is supposed to be
        return res[:-1]


class Solution3:
    def pushDominoes(self, dominoes: str) -> str:
        """The force solution from the official solution.

        https://leetcode.com/problems/push-dominoes/solution/

        Interesting solution, but kinda slow. 400 ms.
        """
        N = len(dominoes)
        force = [0] * N
        # force of R, go from left to right
        f = 0
        for i, d in enumerate(dominoes):
            if d == 'R':
                f = N
            elif d == '.':
                f = max(f - 1, 0)
            else:
                f = 0
            force[i] = f
        # force of L, go from right to left
        f = 0
        for i in range(N - 1, -1, -1):
            if dominoes[i] == 'L':
                f = -N
            elif dominoes[i] == '.':
                f = min(f + 1, 0)
            else:
                f = 0
            force[i] += f
        return ''.join('R' if f > 0 else 'L' if f < 0 else '.' for f in force)


sol = Solution3()
tests = [
    ('RR.L', 'RR.L'),
    ('.L.R...LR..L..', 'LL.RR.LLRRLL..'),
    ('RRRRRRL...', 'RRRRRRL...'),
]

for i, (dominoes, ans) in enumerate(tests):
    res = sol.pushDominoes(dominoes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
