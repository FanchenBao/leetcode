# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def hammingWeight(self, n: int) -> int:
        """More or less a cheating method, because I used Python's built-in
        function to convert input into binary and then literally count the
        number of 1s.

        52 ms, 5% ranking.
        """
        return format(n, '032b').count('1')


class Solution2:
    def hammingWeight(self, n: int) -> int:
        """This seems to be the common method. We simply right shift the given
        number, and each time we check whether the shifted-off value is a one.
        If it is, we increment a counter.

        32 ms, 63% ranking.
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


class Solution3:
    def hammingWeight(self, n: int) -> int:
        """Solution1 was dumb! There is no need to fill the entire 32 bits. We
        can just use bin() and it will work.

        36 ms, 26% ranking.
        """
        return bin(n).count('1')


class Solution4:
    def hammingWeight(self, n: int) -> int:
        """This is one of the official solutions. Its genious lies in the bit
        manipulation where the right most '1' digit gets flipped to '0' by a
        simple operation: n & (n - 1).
        """
        counter = 0
        while n:
            counter += 1
            n = n & (n - 1)
        return counter


class Solution5:
    def hammingWeight(self, n):
        """This is just genious. Let me use an example to explain.

        Given n = 198 = '11000110', and consider only the least significant 8
        bits.

        n & 0x55555555 = 1100 0110 & 0101 0101 = 0100 0100 This means we have
        one 1 in the left most 2 bits, and another one 1 in the mid left most
        2 bits.

        (n >> 1) & 0x55555555 = 0110 0011 & 0101 0101 = 0100 0001 This means we
        have another one 1 in the left most 2 bits, and one 1 in the right most
        2 bits.

        Combine the two results 0100 0100 + 0100 0001 = 10 00 01 01 This means
        we have two 1s in the left most 2 bits, one 1 in the middle 2 bits, and
        another one 1 in the right most 2 bits.

        We proceed to use mask 0x33333333, which aggregates the number of 1s in
        the first four bits and last four bits. Similarly, we use 0x0f0f0f0f
        mask for aggregating the first eight bits, 0x00ff00ff for the first 16
        bits, and 0x0000ffff for the first 32 bits.

        This operation runs in five steps for all 32 bit numbers. Genious!
        """
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555))
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n


sol = Solution5()
tests = [
    # (11, 3),
    # (128, 1),
    (198, 4)
]

for i, (n, ans) in enumerate(tests):
    res = sol.hammingWeight(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
