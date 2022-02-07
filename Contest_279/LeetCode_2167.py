# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def minimumTime(self, s: str) -> int:
        """My idea is very close to the hint, but I did use the hint to
        massively simplify the computation and correct one misconception. The
        misconception is that we must remove the flanking 1s by popping them
        one by one. This turns out incorrect. In other words, the flanking 1s
        should not be treated separately.

        The key observation is as such: if from left to right or right to left
        we have executed a remove anywhere operation, then it is always worse
        if we remove the rest using a pop operation. This is because the remove
        anywhere operation costs 2, which is one more than the pop operation.
        The implication of this is that once we perform a remove anywhere, we
        might as well perform remove anywhere for the remaining 1s (because if
        we want to pop after remove anywhere, it will always be worse than not
        doing the remove anywhere and focus just on popping). Thus, the final
        solution shall resemble something like this:

        pop, pop, pop, remove anywhere, remove anywhere, pop, pop, pop

        So the task becomes finding the min cost of a combination of pop and
        remove anywhere going from left to right. And find the cost of popping,
        which is trivial, going from right to left. Combining these two, we
        will find the min cost of handling the entire array.

        I use heap to find the min cost from left to right with consideration
        of pop and remove anywhere. I first compute the base cost, which is to
        use remove anywhere for all 1s. Then I go from left to right, one by
        one forcing each ` to pop and record the total cost. Then I go from right
        to left, finding the min cost ending at each position.

        O(NlogN), 5913 ms, 10% ranking.
        """
        N = len(s)
        one_indices = []
        for k in range(N):
            if s[k] == '1':
                one_indices.append(k)
        if not one_indices:  # edge case where there is no 1s
            return 0
        M = len(one_indices)
        base = 2 * M
        temp = [(base, -1)]
        for i in range(M):
            heapq.heappush(temp, (base - 2 * (i + 1) + one_indices[i] + 1, i))
        ltor = [0] * M
        for k in range(M - 1, -1, -1):
            while temp and temp[0][1] > k:
                heapq.heappop(temp)
            ltor[k] = temp[0][0] - 2 * (M - k - 1)
        res = min(ltor[-1], N - one_indices[0])
        for j in range(M - 1):
            res = min(res, ltor[j] + N - one_indices[j + 1])
        return res


class Solution2:
    def minimumTime(self, s: str) -> int:
        """Both Lee215 and DBabichev solutions are brilliant. But they are not
        beyond my reach. I was very very close to realizing this structure for
        the final solution

        pop, pop, pop, remove anywhere, remove anywhere, pop, pop, pop

        I just lacked the brilliance to reach this epiphony and carry on to
        get to the final solution.

        DBabichev turns the problem to finding max subarray sum. Lee215, whose
        method I will use here, directly computes the min cost of the left in
        a one pass solution.

        It's a DP problem to find the min cost of the left. If I already have
        the min cost upto i - 1, for the ith value, either I remove anywhere on
        it and add it to the min cost of i - 1, or I have to pop everything
        until i. Take the smaller of the two, then we have the min cost upto
        i. So brilliant

        Ref: https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/discuss/1748704/JavaC%2B%2BPython-Short-One-Pass-O(1)-Space

        O(N), 2878 ms
        """
        left_min = 0
        res = N = len(s)
        for i, dig in enumerate(s):
            left_min = min(left_min + (2 if dig == '1' else 0), i + 1)
            res = min(res, left_min + N - i - 1)
        return res


sol = Solution2()
tests = [
    ('1100101', 5),
    ('0010', 2),
    ('010001000', 4),
    ('011100001000000', 6),
    ("01011010", 7),
    ("01010101011011001001010101011010101010101010101101010010101", 56),
    ("0", 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minimumTime(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
