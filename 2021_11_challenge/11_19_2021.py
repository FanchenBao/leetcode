# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        """LeetCode 461

        Use binary string
        """
        return bin(x ^ y).count('1')


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        """Right shift to count 1 bit"""
        temp, res = x ^ y, 0
        while temp:
            res += (temp & 1)
            temp >>= 1
        return res


class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        """Brian Kernighan approach. So good!
    
        Ref: https://leetcode.com/problems/hamming-distance/discuss/1585474/C%2B%2BPython-4-Simple-Solutions-w-Explanations-or-XOR-and-Brian-Kernighan-method
        """
        temp, res = x ^ y, 0
        while temp:
            res += 1
            temp &= (temp - 1)  # unset the right most bit
        return res

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
