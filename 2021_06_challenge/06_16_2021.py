# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        """LeetCode 22

        Since the largest n is 8, which means the longest parenthesis string
        is 16 element long, we can iterate through all possible parenthesis
        arrangement and check which ones are valid. The max number of check is
        2^16 = 1024 times, which is very reasonable.

        The check is easily done via a stack.

        There is one trick on iterating through all possible parenthesis states.
        Since we designate 0 => ( and 1 => ), then the state cannot start with
        1 and cannot end with 0. Therefore, we only have to iterate 2^(N - 1)
        number of states, and each state must be an odd number. This shrinks our
        search space, and leads to the following runtime.

        O(2^(2N - 2) * N), 44 ms, 25% ranking
        """
        res = []
        for p in range(1, 1 << 2 * n - 1, 2):
            pb = format(p, f'0{2 * n}b')
            if pb.count('0') * 2 == len(pb):
                stack = []
                for e in pb:
                    if e == '0':
                        stack.append(e)
                    elif stack and stack[-1] == '0':
                        stack.pop()
                    else:
                        break
                else:
                    res.append(pb.replace('0', '(').replace('1', ')'))
        return res


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        """I wasn't able to come up with a recursion solution, probably because
        my brain is tired. Anyway, this is the official recursion solution. The
        key observation is that at each step we can add a '(' or  ')'. After
        that, we have the same subproblem which can also be solved by adding
        either a '(' or ')'. However, we can make better decisions as to when
        the '(' or ')' is used. The solution constrants that we can only add a
        '(' when the total number of '(' is ≤ n. And we can only add a ')'
        when the current number of right parenthesis is smaller or equal to the
        left. We cannot have a larger value in right compared to left. With
        these restrictions, the recursion relation is fairly easy to write.

        36 ms.
        """
        res = []

        def helper(pot_lst: List[int], num_right_p: int, num_left_p: int) -> None:
            if len(pot_lst) == 2 * n:
                res.append(''.join(pot_lst))
            else:
                if num_left_p < n:
                    pot_lst.append('(')
                    helper(pot_lst, num_right_p, num_left_p + 1)
                    pot_lst.pop()
                if num_left_p > num_right_p:
                    pot_lst.append(')')
                    helper(pot_lst, num_right_p + 1, num_left_p)
                    pot_lst.pop()


        helper([], 0, 0)
        return res


sol = Solution2()
tests = [
    (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
    (1, ['()']),
]

for i, (n, ans) in enumerate(tests):
    res = sol.generateParenthesis(n)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
