# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """LeetCode 1029

        I think this is Greedy again. First of all, we choose the smallest
        cost no matter what. After that, we check whether either choice is
        dominant. If both choices have been chosen equal number of times, we
        can return the sum of all the smallest costs directly. Otherwise, we
        need to perform swaps. We start from the min total cost. Then each
        swap needs to be performed on the dominant choices. And the swap must
        happen according to the order of the difference between the two costs.
        Essentially, the difference is the amount of cost that will be added
        to the min cost. Thus, picking a smaller difference means adding less
        to the total cost. Therefore, we sort the cost difference array of the
        dominant choices and add the first K differences to the total, where
        K is the difference between the dominance and equal representation.

        The algorithm of picking the smallest difference for swapping is sound.
        The only part that requires proof is why we only swap on the dominant
        side? Suppose we swap on the non-dominant side (call it A). Then we
        need to swap twice on the dominant side to reach equilibrium (call it
        B and C). In total, there are three swaps A, B, C. It is definitely
        cheaper to not perform A, and only perform the smaller of B and C. In
        this situation, there is only one swap and it costs less. Therefore,
        swapping only the dominant side is proven to be a better choice.

        O(NlogN), 54 ms, 61% ranking.
        """
        choices = [0] * len(costs)
        res = 0
        N = len(costs)
        for i, (c0, c1) in enumerate(costs):
            choices[i] = 0 if c0 <= c1 else 1
            res += min(c0, c1)
        one_choices = sum(choices)
        if one_choices > N // 2:  # too many 1s
            res += sum(sorted([costs[i][0] - costs[i][1] for i, c in enumerate(choices) if c])[:one_choices - N // 2])
        elif one_choices < N // 2:  # too many 0s
            res += sum(sorted([costs[i][1] - costs[i][0] for i, c in enumerate(choices) if not c])[:N // 2 - one_choices])
        return res


class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """A better implementation from:

        https://leetcode.com/problems/two-city-scheduling/discuss/667786/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation

        The idea is similar, but we simply pick choice 0 for everyone. And then
        we decide which n people needs to swap to choice 1. The criteria to
        choose those n people is to find the people with the highest refund
        when swapping to choice 1. More concretely, the n people should be
        chosen by computing the cost difference of cost[1] - cost[0] and find
        the n smallest of them.

        O(NlogN), 52 ms, 65% ranking.
        """
        return sum(c[0] for c in costs) + sum(sorted(c1 - c0 for c0, c1 in costs)[:len(costs) // 2])



sol = Solution2()
tests = [
    ([[10,20],[30,200],[400,50],[30,20]], 110),
    ([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859),
    ([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], 3086),
]

for i, (costs, ans) in enumerate(tests):
    res = sol.twoCitySchedCost(costs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
