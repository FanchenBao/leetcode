# from pudb import set_trace; set_trace()
from typing import List, Tuple
from functools import lru_cache


class Solution1:
    def addOperators(self, num: str, target: int) -> List[str]:
        """LeetCode 282

        Top down DP solution. We consider at each index of num, we can either
        take the current digit by itself, or we can take 2, 3, 4, ..., all the
        rest of the digits as a whole. Once the current number is determined by
        including however many digits we want, we can add a plus, minus, or
        multiply symbol afterwards. If it is a plus sign, we can recurse on the
        remaining num, and whatever value the remaining computes, we will add
        the current number to it as the overall value. If it is a minus sign,
        we do the same procedure as the plus sign, except that we have to
        reverse the plus and minus sign from the expression of the remaining.
        If it is a multiply sign, we will pass a factor to the next round. This
        factor includes the current value as a multiplier for the next round.
        Whatever value returned from the next round will have already considered
        the current number, thus we do not have to do any more computation for
        the current number.

        There is one trick with '0'. It can only be considered as a single digit

        O((N-1)C0 * 3^0 + (N-1)C1 * 3^1 + (N-1)C2 * 3^2 + ... + (N-1)C(N-1) * 3^N)
        time complexity

        However, the official solution says the time complexity is O(4^N). I
        believe in that than my time complexity.

        But space complexity is pretty bad, because we evaluate after all the
        recursion is done, which means all expressions must be kept in memory.
        The official solution evaluates at the end of a DFS and backtracks, thus
        it does not have to keep all expressions in memory.

        1094 ms, 28% ranking.
        """
        N = len(num)

        @lru_cache(maxsize=None)
        def help(factor: int, idx) -> List[Tuple[int, str]]:
            res = []
            for i in range(idx, idx + 1 if num[idx] == '0' else N):
                n = int(num[idx:i + 1])
                if i == N - 1:
                    res.append((factor * n, str(n)))
                else:
                    for val, exp in help(1, i + 1):  # +
                        res.append((factor * n + val, f'{n}+{exp}'))
                    for val, exp in help(1, i + 1):  # -
                        rev_exp = exp.replace('+', '#').replace('-', '+').replace('#', '-')
                        res.append((factor * n - val, f'{n}-{rev_exp}'))
                    for val, exp in help(factor * n, i + 1):  # *
                       res.append((val, f'{n}*{exp}'))
            return res

        return [exp for val, exp in help(1, 0) if val == target]


class Solution2:
    def addOperators(self, num: str, target: int) -> List[str]:
        """This is according to the official solution, but based on DBabichev

        https://leetcode.com/problems/expression-add-operators/discuss/1470156/Python-dfs-with-stack-of-monomials-explained

        The order of recursion is different. It considers what has happened
        before, and then what will happen when the current number is included.
        Solution 1 is given the current number, recurse to find what the rest
        is going to generate. Two different ways of handling recursion, but this
        solution, which is DFS, has a space advantage, because it does not have
        to store all intermediate values in memory.

        One important trick is handling multiplication. Note that we do

        `val - last + last * n`

        which means we remove the effect of last in the previous evaluation, and
        add the new effect which is last * n.

        616 ms
        """
        res = []
        N = len(num)

        def dfs(idx: int, val: int, last: int, exp: str) -> None:
            if idx == N:
                if val == target:
                    res.append(exp)
            else:
                for i in range(idx, idx + 1 if num[idx] == '0' else N):
                    n = int(num[idx:i + 1])
                    if idx == 0:
                        dfs(i + 1, n, n, str(n))
                    else:
                        dfs(i + 1, val + n, n, exp + f'+{n}')
                        dfs(i + 1, val - n, -n, exp + f'-{n}')
                        dfs(i + 1, val - last + last * n, last * n, exp + f'*{n}')

        dfs(0, 0, 0, '')
        return res


sol = Solution2()
tests = [
    ('123', 6, ['1*2*3', '1+2+3']),
    ('232', 8, ['2*3+2', '2+3*2']),
    ('105', 5, ['1*0+5', '10-5']),
    ('00', 0, ['0*0', '0+0', '0-0']),
    ('3456237490', 9191, []),
    ('1', 6, []),
    ('6', 6, ['6']),
    ('105', 6, ['1+0+5', '1-0+5']),
]

for i, (num, target, ans) in enumerate(tests):
    res = sol.addOperators(num, target)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
