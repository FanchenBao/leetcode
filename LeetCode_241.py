# from pudb import set_trace; set_trace()
from typing import List
import operator
from itertools import permutations
import bisect
from functools import lru_cache


class Solution1:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """This is a tough one for me.

        I first parse the expression. Then I locate the indices for each
        operator. After that, I permute the operator indices, and for each
        permutation, I compute the parenthesized expression and result. The
        difficult part is the parenthesization. My method is to keep track of
        the current parenthesization state of the expression str and the
        computed value. In addition, I also use a sentinel value to indicate
        whether a new expression shall come from the original expression or
        the states currently saved in the dict.

        320 ms, 5% ranking.
        """
        exp_parsed, opindices = [], []
        num = 0
        for le in expression:
            if le in '+-*':
                exp_parsed.append(num)
                exp_parsed.append(le)
                opindices.append(len(exp_parsed) - 1)
                num = 0
            else:
                num = 10 * num + int(le)
        exp_parsed.append(num)
        if not opindices:  # edge case where no operators exist in expression
            return exp_parsed
        exp_res = {}
        ops = {'*': operator.mul, '+': operator.add, '-': operator.sub}
        for perm in permutations(opindices):
            exp_copy = exp_parsed[:]
            exp_map = {}
            for opi in perm:
                op = exp_copy[opi]
                if exp_copy[opi - 1] == -1 or exp_copy[opi + 1] == -1:
                    sorted_opi = sorted(exp_map)
                    idx = bisect.bisect_right(sorted_opi, opi)
                    if exp_copy[opi - 1] == -1 and exp_copy[opi + 1] == -1:
                        left_str, left_val = exp_map.pop(sorted_opi[idx - 1])
                        right_str, right_val = exp_map.pop(sorted_opi[idx])
                    elif exp_copy[opi - 1] == -1:
                        left_str, left_val = exp_map.pop(sorted_opi[idx - 1])
                        right_str = right_val = exp_copy[opi + 1]
                    else:
                        left_str = left_val = exp_copy[opi - 1]
                        right_str, right_val = exp_map.pop(sorted_opi[idx])
                    exp_map[opi] = (
                        f'({left_str}{op}{right_str})',
                        ops[op](left_val, right_val),
                    )
                else:
                    exp_map[opi] = (
                        f'({exp_copy[opi - 1]}{op}{exp_copy[opi + 1]})',
                        ops[op](exp_copy[opi - 1], exp_copy[opi + 1]),
                    )
                exp_copy[opi - 1] = exp_copy[opi + 1] = -1
            for exp_str, exp_val in exp_map.values():
                exp_res[exp_str] = exp_val
        return list(exp_res.values())


class Solution2:
    @lru_cache(maxsize=None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """Extremely good recursion.

        Ref: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66328/A-recursive-Java-solution-(284-ms)

        42 ms, 43% ranking
        """
        res = []
        ops = {'*': operator.mul, '+': operator.add, '-': operator.sub}
        for i, e in enumerate(expression):
            if e in '*-+':
                for rl in self.diffWaysToCompute(expression[:i]):
                    for rr in self.diffWaysToCompute(expression[i + 1:]):
                        res.append(ops[e](rl, rr))
        return res if res else [int(expression)]


sol = Solution2()
tests = [
    ("2-1-1", [0, 2]),
    ("2*3-4*5", [-34,-14,-10,-10,10]),
    ('23-45*67', [-2992, -1474]),
    ('0', [0]),
    ("2-1-1-1-1", [2,0,2,2,4,0,2,2,0,0,2,0,0,-2])
]

for i, (expression, ans) in enumerate(tests):
    res = sol.diffWaysToCompute(expression)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {sorted(ans)}, Res: {sorted(res)}')
