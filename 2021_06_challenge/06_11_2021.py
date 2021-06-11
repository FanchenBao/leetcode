# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution1:
    def stoneGameVII(self, stones: List[int]) -> int:
        """LeetCode 1690

        It's not simple. But this is still DP. The idea is to find out the
        score difference between Alice and Bob at each possible arrangement of
        stones. That means we start from two stones. What is the score difference
        if Alice goes first, and if Bob goes first. Then we do three stones,
        and so on and so forth, until we get to the entire set of stones.

        At each stone arangement, a player can take the left or right stone.
        After the player makes a move, we already have the score difference of
        the remaining stones if the next player plays optimally. Thus, we can
        compute the two score differences for the current player if s/he chooses
        left or right stone. For Bob, he needs to minimize the score difference,
        so he will choose the min of the two scores. For Alice, she will choose
        the max of the two scores.

        We build up a DP table, with row idx being the length of any stone
        arrangement, and col idx being the left most idx of the current stone
        arrangement. The result is dp[N][0]

        O(N^2), 4420 ms, 69% ranking. Space complexity is O(N^2), which we can
        improve to O(N)
        """
        N = len(stones)
        pre_sum = list(accumulate(stones))
        # row idx is the length, col idx is the left most idx of an array of
        # stones that has length of the col idx
        dp = [[0] * (N - 1) for _ in range(N + 1)]
        bob_turn = N % 2 == 1
        for i in range(2, N + 1):
            for j in range(N - i + 1):
                if i == 2:
                    max_val = max(stones[j], stones[j + i - 1])
                    dp[i][j] = -max_val if bob_turn else max_val
                else:
                    # choose left
                    opt_p1_l = pre_sum[j + i - 1] - pre_sum[j]
                    opt_p2_l = dp[i - 1][j + 1]
                    # choose right
                    opt_p1_r = pre_sum[j + i - 2] - (pre_sum[j - 1] if j > 0 else 0)
                    opt_p2_r = dp[i - 1][j]
                    if bob_turn:
                        dp[i][j] = min(-opt_p1_l + opt_p2_l, -opt_p1_r + opt_p2_r)
                    else:
                        dp[i][j] = max(opt_p1_l + opt_p2_l, opt_p1_r + opt_p2_r)
            bob_turn = not bob_turn
        return dp[N][0]


class Solution2:
    def stoneGameVII(self, stones: List[int]) -> int:
        """Same solution as above but with 1D DP array.

        O(N^2) runtime, O(N) space complexity, 3840 ms, 81% ranking.

        UPDATE: the solution posted here:
        https://leetcode.com/problems/stone-game-vii/discuss/970268/C%2B%2BPython-O(n-*-n)

        clarifies an important point: we do not have to keep track whose turn
        it is. Because at each turn, any player wants to maximize the difference
        between his/her current point and the next round's optimal difference.
        In other words, despite the goal of both players are different, they are
        essentially doing the same thing: to maximize the difference between
        their current point and the optimal difference in the next round.

        Since we do not have to consider turns, the solution can be vastly
        simplified
        """
        N = len(stones)
        pre_sum = list(accumulate(stones))
        # base case with two stones
        dp = [max(stones[j], stones[j + 1]) for j in range(N - 1)]
        for i in range(3, N + 1):
            for j in range(N - i + 1):
                # choose left
                opt_p1_l = pre_sum[j + i - 1] - pre_sum[j]
                opt_p2_l = dp[j + 1]
                # choose right
                opt_p1_r = pre_sum[j + i - 2] - (pre_sum[j - 1] if j > 0 else 0)
                opt_p2_r = dp[j]
                dp[j] = max(opt_p1_l - opt_p2_l, opt_p1_r - opt_p2_r)
        return dp[0]


sol = Solution2()
tests = [
    ([5, 3, 1, 4, 2], 6),
    ([7, 90, 5, 1, 100, 10, 10, 2], 122),
    ([5, 3, 1, 4], 7),
    ([1, 3, 4, 5], 8),
    ([481, 905, 202, 250, 371, 628, 92, 604, 836, 338, 676, 734], 3459),
]

for i, (stones, ans) in enumerate(tests):
    res = sol.stoneGameVII(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
