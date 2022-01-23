# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution1:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """LeetCode 1291

        Find the range for each number of digits, and produce the sequential
        digit number within this range. Then move on to the next number of
        digits. The number production process is carried out via a sliding
        window mechanism.

        28 ms, 84% ranking.
        """
        digits = '123456789'
        num_dig = len(str(low))
        res = []
        il = low
        while True:
            ih = min(high, 10**num_dig - 1)
            lo, hi = 0, num_dig - 1
            while hi < 9:
                cand = int(digits[lo:hi + 1])
                if il <= cand <= ih:
                    res.append(cand)
                elif cand > ih:
                    break
                lo += 1
                hi += 1
            if ih == high:
                break
            num_dig += 1
            il = ih + 1
        return res



class Solution2:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """This is the queue solution, which produces sequential digit number
        in a nicer way.

        Ref: https://leetcode.com/problems/sequential-digits/discuss/853592/Python-Solution-using-queue-explained

        24 ms, 96% ranking.
        """
        queue = deque(range(1, 10))
        res = []
        while queue:
            n = queue.popleft()
            if low <= n <= high:
                res.append(n)
            if n % 10 < 9:
                queue.append(n * 10 + n % 10 + 1)
        return res


sol = Solution2()
tests = [
    (100, 300, [123, 234]),
    (1000, 13000, [1234,2345,3456,4567,5678,6789,12345]),
]

for i, (low, high, ans) in enumerate(tests):
    res = sol.sequentialDigits(low, high)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
