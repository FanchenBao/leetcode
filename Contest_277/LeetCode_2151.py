# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def maximumGood(self, statements: List[List[int]]) -> int:
        """Since only good people's words are trust worthy, we try setting each
        person as good person. From there, we can perform deterministic check
        to see whether all the statements check out. Note that if a person is
        deemed as bad, his statement doesn't matter. This is akin to a DFS
        search, and we return the max good people in each scenario.

        The DFS search can be cached, becasue we use bitmap as representation
        of states. Each state consists of three values: the current ids of the
        good and bad people, and the current person to be grouped into the
        good people. Cache is important to avoid TLE.

        5529 ms, pretty bad run time.
        """
        res = 0
        n = len(statements)
        
        @lru_cache(maxsize=None)
        def check(good: int, bad: int, start: int) -> int:
            good |= (1 << start)
            queue = [start]
            while queue:
                temp = []
                for g in queue:
                    for j in range(n):
                        if statements[g][j] == 1:
                            if bad & (1 << j):
                                return -1
                            elif not good & (1 << j):
                                good |= (1 << j)
                                temp.append(j)
                        elif statements[g][j] == 0:
                            if good & (1 << j):
                                return -1
                            elif not bad & (1 << j):
                                bad |= (1 << j)
                queue = temp
            cur_state = good | bad
            res = 0
            for i in range(n):
                if not cur_state & (1 << i):
                    res = max(res, check(good, bad, i))
            return max(res, bin(good).count('1'))

        for i in range(n):
            res = max(res, check(0, 0, i))
        return res


class Solution2:
    def maximumGood(self, statements: List[List[int]]) -> int:
        """This solution is so good.

        Ref: https://leetcode.com/problems/maximum-good-people-based-on-statements/discuss/1711218/C++Python-Simple-Solution-w-Explanation-or-DFS+Backtracking-and-Bitmasking/1231857

        The idea is to go through all possible combinations of good and bad
        people using bitmap. For each bitmap, we need to validate against each
        statement. If any of the statement does not check out with the bitmap,
        that means the bitmap is impossible.

        The check for each statement can be done by first converting the
        statements into two arrays of bitmaps, one representing all the cases
        of good people claimed by each person, and the other the bad people.
        Then to see whether a person's statement checks out, we first XOR the
        current state with the person's claims of good people. If the person's
        claim is correct, then the only ones left after XOR should be the good
        people that the person has not declared. Then we and this new state
        with the person's claim of bad people. If this result is not zero, that
        means some good people are claimed as bad people by the current person.
        This means the statements do not checkout.

        O(N * 2^N), 604 ms.

        NOTE: in this version, when validate, we also include another check,
        that is the current person's claim for good people does match the good
        people in the current state. This is slightly different from the refed
        solution.
        """
        N = len(statements)
        good_claims = [0] * N
        bad_claims = [0] * N
        # Build good and bad claims based on statements
        for i in range(N):
            for j in range(N):
                if statements[i][j] == 1:
                    good_claims[i] |= 1 << j
                elif statements[i][j] == 0:
                    bad_claims[i] |= 1 << j
        
        # Validate statement
        def validate(cur_state: int) -> bool:
            for i in range(N):
                if cur_state & 1 << i:  # ith person is a good person
                    if (cur_state | good_claims[i] | 1 << i) != cur_state or (cur_state ^ good_claims[i]) & bad_claims[i]:
                        return False
            return True

        res = 0
        for cur_state in range(1 << N):
            cnt = bin(cur_state).count('1')
            if cnt > res and validate(cur_state):
                res = cnt
        return res



sol = Solution2()
tests = [
    ([[2,1,2],[1,2,2],[2,0,2]], 2),
    ([[2,0],[0,2]], 1),
    ([[2,2,2,2],[1,2,1,0],[0,2,2,2],[0,0,0,2]], 1),
]

for i, (statements, ans) in enumerate(tests):
    res = sol.maximumGood(statements)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
