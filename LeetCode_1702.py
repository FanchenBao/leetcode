# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maximumBinaryString(self, binary: str) -> str:
        """Once we find the pattern of '011..10', it can be converted to
        '1011..11'. Then we just need to extend on the right until we find the
        next '0', and the same pattern occurs again.

        Before this pattern shows up, we have to deal with potential leading
        '1's and '0's first.

        O(N), 2184 ms, faster than 16.67%
        """
        arr = list(binary)
        N = len(arr)
        i = 0
        # skip all the leading '1's
        while i < N:
            if arr[i] == '0':
                break
            i += 1
        # handling the situation of consecutive '0's. We can always turn
        # '000..01' into '111..01'
        j = i + 1
        while j < N and arr[j] == '0':
            arr[i] = '1'
            i += 1
            j += 1
        # This is the '0111...10' situation. It can always be converted to
        # '10111...11'. Then we repeat the same situation by moving j forward
        # until the next '0'
        while j < N:
            while j < N and arr[j] == '1':
                j += 1
            if j == N:
                break
            arr[i] = '1'
            arr[i + 1] = '0'
            arr[j] = '1'
            i += 1
            j += 1
        return ''.join(arr)


class Solution2:
    def maximumBinaryString(self, binary: str) -> str:
        """Inspired by lee215 https://leetcode.com/problems/maximum-binary-string-after-change/discuss/987335/JavaC%2B%2BPython-Solution-with-Explanation

        Go from right to left and convert all '10' to '01'. What this does is
        pushing all the '1's to the right and bubbling all the '0' to the left

        For instance, '100010' => '100001' => '010001' => '001001' => '000101'
        => '000011'

        In fact, for any given binary string, we can always perform this
        operation such that '0's are on the left and '1's are on the right.

        Then we turn all the '0's from the left into '111...10' And we are done

        O(N), 188 ms, faster than 67.65%
        """
        c1 = binary.count('1')
        c0 = len(binary) - c1
        if not c0:
            return binary
        i = binary.find('0')  # do not alter the leading '1's
        return binary[:i] + '1' * (c0 - 1) + '0' + '1' * (c1 - i)



sol = Solution2()
tests = [
    ('000110', '111011'),
    ('01', '01'),
]

for i, (binary, ans) in enumerate(tests):
    res = sol.maximumBinaryString(binary)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
