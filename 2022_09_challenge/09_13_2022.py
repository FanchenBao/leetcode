# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """LeetCode 393

        It's not difficult, but two tricky things.

        1. '10xxxxxx' cannot be a leading byte, because for a value of only one
        byte, it has to start with '0'
        2. Each UTF-8 character must not be more than 4 bytes.

        129 ms, faster than 84.80% 
        """
        N = len(data)

        def validate(lo: int, hi: int) -> bool:
            if hi >= N:
                return False
            return all(f'{data[i]:08b}'[:2] == '10' for i in range(lo, hi + 1))

        i = 0
        while i < N:
            b = f'{data[i]:08b}'
            if b[0] == '0':
                i += 1
            else:
                one_count = len(b) - len(b.lstrip('1'))
                if 1 < one_count < 5 and b[one_count] == '0' and validate(i + 1, i + one_count - 1):
                    i += one_count
                else:
                    return False
        return True


sol = Solution()
tests = [
    ([197,130,1], True),
    ([235,140,4], False),
    ([145], False),
    ([250,145,145,145,145], False),
]

for i, (data, ans) in enumerate(tests):
    res = sol.validUtf8(data)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
