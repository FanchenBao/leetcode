# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def beautifulArray(self, n: int) -> List[int]:
        """LeetCode 932

        There are two hoops to jump. First, we need to figure out a simple
        mechanism to achieve a beautiful array. My method is to group all odd
        numbers on the left side and all even numbers on the right side. This
        way, any interaction between the two sides are guaranteed to satisfy the
        requirement, because even + odd = odd != 2 * some_value.

        Next, we need to figure out how to organize the odd part and even part
        of the array. Suppose the odd part has largest value M. Then we can
        perform (value + 1) // 2 on all the odd numbers. This will turn the odd
        part into an array starting from 1 to (M + 1) // 2. To find a beautiful
        array from 1 to (M + 1) // 2, we actually have solved this problem
        already. Similarly, on the even part, we can perform value // 2 to
        convert into an array starting from 1 to N // 2, where N is the largest
        even number. And this problem has been solved as well.

        Thus, we can use bottom-up DP solution to acquire one beautiful array
        for any given n.

        O(N^2), 305 ms. Very very bad runtime.
        """
        dp = [[], [1], [1, 2], [1, 3, 2]]
        for i in range(4, n + 1):
            ri, le = i // 2, i - i // 2
            dp.append([j * 2 - 1 for j in dp[le]] + [j * 2 for j in dp[ri]])
        return dp[n]


class Solution2:
    def beautifulArray(self, n: int) -> List[int]:
        """O(NlogN), divide and conquer with memoization from lru_cache.

        Same idea as Solution1, but much faster. 41 ms, 27% ranking.

        UPDATE: with memoization, the runtime is O(N). See explanation in
        Solution3
        """

        @lru_cache(maxsize=None)
        def dp(num: int, from_even: bool) -> List[int]:
            if num == 0:
                return []
            if num == 1:
                return [2] if from_even else [1]
            if num == 2:
                return [2, 4] if from_even else [1, 3]
            if num == 3:
                return [2, 6, 4] if from_even else [1, 5, 3]
            le = dp(num - num // 2, False)
            ri = dp(num // 2, True)
            return [v * 2 if from_even else v * 2 - 1 for v in le + ri]

        return dp(n - n // 2, False) + dp(n // 2, True)


class Solution3:
    @lru_cache(maxsize=None)
    def beautifulArray(self, n: int) -> List[int]:
        """Better implementation of divide and conquer.

        32 ms, 92% ranking.

        About the run time. Without memo, the merging cost of each level is O(N).
        But, with memo, only the top level has O(N) cost. The subsequent levels
        has O(N/2), O(N/4), ... because we do not have to compute for each node.
        This means the total complexity is O(N) + O(N/2) + O(N/4) + ... + O(1)
        This will not exceed O(2N). Hence the time complexity is O(N).
        """
        if n == 1:
            return [1]
        le = self.beautifulArray((n + 1) // 2)
        ri = self.beautifulArray(n // 2)
        return [v * 2 - 1 for v in le] + [v * 2 for v in ri]


sol = Solution3()
tests = list(range(1, 100))

# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]
def check_ans(res: List[int]) -> bool:
    for i in range(len(res) - 2):
        for j in range(i + 2, len(res)):
            for k in range(i + 1, j):
                if res[i] + res[j] == res[k] * 2:
                    return False
    return True


for i, n in enumerate(tests):
    res = sol.beautifulArray(n)
    if check_ans(res):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Res: {res}. Test: {n}')
