# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce
from operators import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """LeetCode 260

        I wasn't able to solve this within the constraint. I check the
        solution here:

        https://leetcode.com/problems/single-number-iii/discuss/1561785/Java-Simple-Bit-Manipulation-using-XOR-or-Two-Pass-or-Beats-100-0ms-or-TC%3AO(N)-SC%3AO(1)

        It was brilliant. Still, we use XOR. But since the result of XOR all
        numbers in nums is a XOR b, we cannot determine a and b. But we can
        determine the right most bit that is different between a and b. That
        bit would be the right most set bit in a XOR b. Knowing that the kth bit
        is the right most bit that is different between a and b, and suppose
        a has kth bit set whereas b has kth bit unset, we can XOR nums again but
        picking only the values whose kth bit is set. Their XOR result will give
        us a. And we can obtain b by a XOR b XOR a.

        The trick is to identify the difference between a and b, and such diff
        allows us to XOR nums without including b. The ones that are included
        must be either dups or a by itself.
        
        O(N), 60 ms, 77% ranking.
        """
        axorb = reduce(xor, nums)
        mask = axorb & (-axorb)  # finding the right most set bit
        a = reduce(xor, [n for n in nums if n & mask])
        return [a, axorb ^ a]
        
        

# sol = Solution3()
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

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
