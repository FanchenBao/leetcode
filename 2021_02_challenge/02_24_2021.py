# from pudb import set_trace; set_trace()
from typing import List, Tuple


class Solution1:
    def scoreOfParentheses(self, S: str) -> int:
        """LeetCode 856

        As usual, parenthesis-related problems can be solved with stack. I
        originally wanted to use some fancy recursion, but I got bogged down in
        some non-trivial index position issues. I backed out of that solution
        and went for the stack. It turns out the stack solution is much much
        better. Both cleaner and faster. The idea is simple. When we see a left
        parenthesis, we alsways push it in the stack. When we see a right
        parenthesis, we pop the stack if there are scores already in it. We pop
        until we encounter the first left parenthesis. Now this is a pair. We
        accumulate the sum of all the scores contained within the pair. If the
        score is zero, which means there is no other parenthesis inside the pair
        we change the top of the stack to 1, which is the score of the current
        pair. Otherwise, we double the score contained within the pair, and also
        change the top of the stack with the score.

        When we finish the whole string, our stack shall contain only scores.
        We return the sum of these scores.

        P(N), 24 ms, 95% ranking.
        """
        stack = []
        for le in S:
            if le == '(':
                stack.append(le)
            else:
                temp = 0
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack[-1] = temp * 2 if temp else 1  # replace '(' with score
        return sum(stack)


class Solution2:
    def scoreOfParentheses(self, S: str) -> int:
        """This is from the official solution.

        Very good solution. The key intuition is that instead of pushing left
        parenthesis, we push 0, which indicates the current score associated
        with the parenthesis pair. Whenever a right parenthesis appears, we pop
        the top of the stack. The value is going to be the score that is
        contained within the current parenthsis pair, except when the score is
        0, which means the current pair does not have any score within it. Then
        we update the current top of the stack, which represents the score of
        the current pair.
        """
        stack = [0]  # this initial zero is important. It is the top level score
        for le in S:
            if le == '(':
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += 2 * score if score else 1
        return stack[-1]


class Solution3:
    def scoreOfParentheses(self, S: str) -> int:
        """This is another one from the official solution. It is called "Count
        Cores". Yet I am going to refer to it as the onion solution.

        For any valid parenthesis string, we can see it as a bunch of onions.
        Each onion might have one or more layers. The intuition is that we can
        always locate the center of all the onions. And once we find the center,
        which is a parenthesis pair without anything else contained within, we
        will know the score of the whole onion as long as we know how many
        layers are outside the core. So the problem becomes to keep counting the
        number of layers until we reach the core. Once the core is reached, the
        total score is incremented by 1 << num_of_layers. Then we move on to the
        next onion.

        Very brilliant solution.
        """
        res, layers = 0, 0
        for i, le in enumerate(S):
            if le == '(':
                layers += 1
            else:
                layers -= 1
                if S[i - 1] == '(':  # we have found the core
                    res += 1 << layers
        return res


sol = Solution3()
tests = [
    ('()', 1),
    ('(())', 2),
    ('()()', 2),
    ('(()(()))', 6),
]

for i, (S, ans) in enumerate(tests):
    res = sol.scoreOfParentheses(S)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
