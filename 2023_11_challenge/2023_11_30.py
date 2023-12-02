# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        LeetCode 1611

        Given a binary number of length 2 + k + p

        10...01x...x
         k 0s  p xs

        with k 0s between the first and second bits and p remaining digits.

        The optimal way to reduce the binary number to 0 is to convert it into

        110.......0

        because this is the only way to remove the first bit. Once the first bit
        is removed, which takes 1 step, we only need to convert the remaining
        10...0 to 0, which through trial and error shows that it takes
        2**(2 + k + p - 1) - 1 steps. Put it together, to turn

        110......0

        to 0, takes 2**(2 + k + p - 1) steps.

        Now the question is how to turn

        0...01x...x

        into

        10.......0

        We first need to turn x...x into 0...0, which can be solved via recursion.

        Then we need to turn

        0...010...0 into 10.....0

        This can be achieved via

        0...010...0 => 0...0110...0  (takes 1 step)
        k 0s  p 0s     k-1 0s p 0s

        0...0110...0 => 0...010...0 (takes 2**(p + 1) - 1 steps)
        k-1 0s  p 0s    k-1 0s p+1 0s

        Similarly we can turn

        0...010...0 => 0...010...0 (takes 1 + 2**(p + 2) - 1 steps)
        k-1 0s p+1 0s  k-2 0s p+2 0s

        and so on

        Thus to turn 0...010...0 into 10.....0 takes
                     k 0s  p 0s      0 0s  p+k 0s

        2**(p + 1) + 2**(p + 2) + ... + 2**(p + k) steps
        This can be rewritten as 2**p(2**(k + 1) - 2)

        Thus the recursion relation has been established.

        36 ms, faster than 83.77%
        """

        def helper(strn: str) -> int:
            i = 0
            # find the first '1'
            while i < len(strn) and strn[i] == '0':
                i += 1
            if i == len(strn):  # no bit is '1'
                return 0
            first_bit_idx = i
            k = 0
            i += 1
            # find the number of '0' between the first and second '1', and save
            # it in k
            while i < len(strn) and strn[i] == '0':
                k += 1
                i += 1
            if i < len(strn):  # a second '1' is found
                p = len(strn) - i - 1
                tmp1 = 2**p * (2**(k + 1) - 2)
                tmp2 = 1 + 2**(len(strn) - first_bit_idx - 1) - 1
                return helper(strn[i + 1:]) + tmp1 + tmp2
            return 2**(len(strn) - first_bit_idx) - 1  # no second '1'

        return helper(bin(n)[2:])


class Solution2:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        This follows the official solution, where it is shown with proof that
        a value 2**k would take 2**(k + 1) - 1 steps to reduce to zero.

        But a more important conclusion is the proof that the optimal operations
        to turn x -> y is the same as y -> x.

        Thus, given any value n, we can break it into two parts. The 2**k part
        which contains the left most bit, and the remaining part. The remaining
        part is n XOR 2**k

        Let's call A(n) as the function that finds the minimum operations, then
        A(n) = 2**(k + 1) - 1 - A(n XOR 2**k)

        Here is the last important part where we identify that A(n) is the
        difference, not the sum of the two operations.
        
        This is because the steps to go from 0 to n is the same as n to 0, both
        are 2**(k + 1) - 1.

        To go from 2**k to n XOR 2**k takes A(n XOR 2**k) (because this is the same as
        going from n XOR 2**k to 2**k).

        Thus we have 2**(k + 1) - 1 = A(n XOR 2**k) + A(n)
        """
        if n == 0:
            return 0

        k = len(bin(n)) - 2
        return (1 << k) - 1 - self.minimumOneBitOperations(n ^ (1 << (k - 1)))
        



sol = Solution()
tests = [
    (0, 0),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
