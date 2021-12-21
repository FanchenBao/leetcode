# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        """LeetCode 231

        Turn n into a binary value and XOR with its mask. The mask is a power of
        2 determined by the number of bits in n.

        I didn't consider negative values, but just out of pure luck, bin() of
        a negative values would yield a wrong number of binary digits for this
        solution. Thus, by mistake, we have solved the negative case as well.
        The correct way is to first check whether n is positive or negative, and
        then use the binary check.

        O(1), 28 ms, 88% ranking.
        """
        return n ^ (1 << (len(bin(n)) - 3)) == 0


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        """This is the actual trick.

        Ref: https://leetcode.com/problems/power-of-two/discuss/63974/Using-nand(n-1)-trick
        """
        return n > 0 and (not n & (n - 1))


sol = Solution2()
tests = [
    (1, True),
    (2, True),
    (3, False),
    (2**31 - 1, False),
    (2**17, True),
    (-2, False),
]

for i, (n, ans) in enumerate(tests):
    res = sol.isPowerOfTwo(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
