# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def validUtf8(self, data: List[int]) -> bool:
        """This is not a difficult problem, but it did take me a long time to
        understand how UTF-8 works. The problem description definitely can use
        some improvement.

        The solution is straightforward. We check the input values one by one
        and match it to the four scenarios. If it's the 1-byte scenario, it
        passes automatically. If it's any of the other three scenarios, we
        continue checking the remaining values. At any point a check fails, we
        return False. The check is conducted via bit manipulation.

        O(N), where N = len(data). 100 ms, 95% ranking.
        """
        i, N = 0, len(data)
        masks = [1 << 7, 0, 0, 0, 0]  # masks[0] = '0xxxxxxx'
        masks[1] = masks[0] + (1 << 6)  # '10xxxxxx'
        masks[2] = masks[1] + (1 << 5)  # '110xxxxx'
        masks[3] = masks[2] + (1 << 4)  # '1110xxxx'
        masks[4] = masks[3] + (1 << 3)  # '11110xxx'
        while i < N:
            if data[i] & masks[0]:  # not 1-byte situation
                for j in range(2, 5):
                    if data[i] & masks[j] == int(j * '1' + (8 - j) * '0', 2):
                        for _ in range(j - 1):
                            i += 1
                            if i == N or data[i] & masks[1] != masks[0]:
                                return False
                        break
                else:
                    return False
            i += 1
        return True


class Solution2:
    def validUtf8(self, data: List[int]) -> bool:
        """This is the official solution's bit manipulation.

        96 ms, 98% ranking. It's faster than my bit manipulation.
        """
        m1 = 1 << 7
        m2 = m1 + (1 << 6)
        n_bytes = 0
        for num in data:
            if n_bytes == 0:
                mask = m1
                while num & mask:
                    n_bytes += 1
                    mask = mask >> 1  # this is smart to check the next bit
                if n_bytes == 1 or n_bytes > 4:
                    return False
                elif n_bytes > 0:
                    n_bytes -= 1
            elif num & m2 != m1:
                return False
            else:
                n_bytes -= 1
        return n_bytes == 0


sol = Solution2()
tests = [
    ([197,130,1], True),
    ([235,140,4], False),
    ([237], False),
]

for i, (data, ans) in enumerate(tests):
    res = sol.validUtf8(data)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
