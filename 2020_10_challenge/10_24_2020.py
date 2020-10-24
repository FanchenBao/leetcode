# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def face_up(self, tokens, left, right, P, score) -> int:
        while left <= right and tokens[left] <= P:
            P -= tokens[left]
            score += 1
            left += 1
        return left, right, P, score

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        """89% ranking. More of a brain teaser than algorithm challenge.
        
        Four key points.
        1. If we cannot play the smallest token face up, the game ends.
        2. We always want to play the smallest token first, because that
        leaves us more token in the tank to attempt a larger one.
        3. We always want to exhaust our power by playing smaller token
        up before resorting to get more tokens. This is because if we
        go for the bigger token first, the end result is the same.
        4. When going for the bigger token, we always go for the max
        available.

        With these four points, the algorithm is not complex. A helper
        function face_up() is provided to exclusively play token face
        up to gain score. We do that first to get the most out of the
        given power.

        Then, we check whether it is necessary to take the
        current max token. The check is to add the max to the current power,
        and compare the sum to the current min. If currnt max + current
        power >= current min, then it is a good decision to take the
        current max, because we have more chance taking playing token face
        up. Otherwise, there is no point going forward. Hence we do the
        loop checking whether there is still point going forward. If there
        is, we continue to play face up as much as we can. Then we check
        whether resorting to the current max is necessary. This repeats
        until we run out of tokens or there is no point going forward.
        """
        tokens.sort()
        left, right, P, score = self.face_up(tokens, 0, len(tokens) - 1, P, 0)
        if not score:  # no move possibnle
            return 0
        while left < right and tokens[right] + P >= tokens[left]:
            left, right, P, score = self.face_up(
                tokens, left, right - 1, P + tokens[right], score - 1,
            )
        return score


sol = Solution()
tests = [
    ([100], 50, 0),
    ([100, 200], 150, 1),
    ([100, 200, 300, 400], 200, 2),
    ([23, 54, 345, 675, 34, 564, 65, 786, 897], 50, 4),
    ([], 10, 0)
]

for i, (tokens, P, ans) in enumerate(tests):
    res = sol.bagOfTokensScore(tokens, P)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
