# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """From the question, we can have two basic findings. First,
        each number can at least create one tree, which a tree of only the root.
        Second, since all the numbers are integers, the root must be bigger than
        its children. Therefore, we can sort the orginal arr, and traverse from
        left to right. For each number, we can examine the values smaller than
        itself, and see if there are any number that is divisible and the
        quotient is also in the arr. And since we are traversing from small to
        big numbers, each time a new number is examined, all of the numbers
        smaller than it must have been examined already. This is a perfect
        situation for DP. Now the trick is only when we find a valid pair for
        a root number, how many trees in total can we create for this specific
        root. Say we use dp to record the number of trees each root value can
        create. Then for a root value x = y * z, the number of trees that can
        be created based on x is 2 * dp[y] * dp[z] if y != z, or d[y] * dp[y] if
        y == z. And that's it. We go through the entire arr (sorted of course),
        populate the DP dictionary (cannot use array because the values can be
        way too big), and eventually return the sum of all number of trees for
        each number.

        O(N^2), 160 ms, 93% ranking.
        """
        dp = defaultdict(int)
        arr_set = set(arr)
        arr.sort()
        for i in range(len(arr)):
            dp[arr[i]] += 1
            thresh = int(math.sqrt(arr[i]))
            for j in range(i):
                if arr[j] > thresh:
                    break
                q, r = divmod(arr[i], arr[j])
                if r == 0 and q in arr_set:
                    dp[arr[i]] += dp[arr[j]] * dp[q] * (1 << (q != arr[j]))
        return sum(dp.values()) % (10**9 + 7)


class Solution2:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """The short version of this problem, insquired by Mr. Pochmann. The run
        time is not very good (1068 ms), but it is an interesting solution.

        The official solution also worth a check, but I am not going to repeat
        it here, as the basic idea is the same. The official solution simply
        relies on index as the key for dp, instead of the actual numbers as in
        Solution1.
        """
        dp = {}
        for a in sorted(arr):
            dp[a] = 1 + sum(dp[b] * dp.get(a / b, 0)for b in arr if b < a)
        return sum(dp.values()) % (10**9 + 7)


sol = Solution2()
tests = [
    ([2, 4], 3),
    ([2, 4, 5, 10], 7),
    ([2, 4, 5, 16, 20, 40, 80], 78),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.numFactoredBinaryTrees(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
