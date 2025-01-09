# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        This is more of a math problem.

        We need to find out how many independent entities a good array has.
        For each index marked by k, it must have the same value as index - 1.
        Thus, we say these two elements form an independent entity. If another
        index marked by k is placed immediately after the previous index, then
        our entity has three elements.

        Now, we can consider any placement of indices. We can see that no
        matter how we move the indices around, the total number of entities
        remain the same, which is n - k. This is because if we move one index
        to another location, its original location does not lose an entity and
        the new location does not gain an entity.

        Sequentially, the first entity has m different choices. The remaining
        entities all have m - 1 choices. Then the k indices can be placed in
        any combination in the n - 1 positions (the index cannot be at position
        zero). With these two pieces of information, we have the solution.
        """
        MOD = 1000000007
        combination = math.comb(n - 1, k) % MOD
        possibilities = m * pow(m - 1, n - k - 1, mod=MOD)
        return possibilities * combination % MOD


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
