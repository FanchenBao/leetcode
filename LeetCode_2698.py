# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import accumulate
from bisect import bisect_right


class Solution1:
    def __init__(self) -> None:
        self.viables = self._pre_compute()
        self.psum = list(accumulate(v * v for v in self.viables))

    def _pre_compute(self) -> List[int]:

        @lru_cache(maxsize=None)
        def dp(num_str: str, tgt: int) -> bool:
            if tgt == 0 and not num_str:
                return True
            for i in range(len(num_str)):
                left = int(num_str[:i + 1])
                if left > tgt:
                    break
                if dp(num_str[i + 1:], tgt - left):
                    return True
            return False

        return [i for i in range(1, 1001) if dp(str(i * i), i)]

    def punishmentNumber(self, n: int) -> int:
        """Pre-compute all the viable values for computing the punishement
        number. The viable values can be calculated via DP.

        2408 ms, faster than 17.77%
        """
        idx = bisect_right(self.viables, n)
        return self.psum[idx - 1]


class Solution2:
    def _get_vialbles(self, n: int) -> List[int]:

        @lru_cache(maxsize=None)
        def dp(num_str: str, tgt: int) -> bool:
            if tgt == 0 and not num_str:
                return True
            for i in range(len(num_str)):
                left = int(num_str[:i + 1])
                if left > tgt:
                    break
                if dp(num_str[i + 1:], tgt - left):
                    return True
            return False

        return [i for i in range(1, n + 1) if dp(str(i * i), i)]

    def punishmentNumber(self, n: int) -> int:
        """Pre-compute all the viable values for computing the punishement
        number. The viable values can be calculated via DP.

        1015 ms, faster than 85.52%
        """
        viables = self._get_vialbles(n)
        idx = bisect_right(viables, n)
        return sum(viables[i]**2 for i in range(idx))
        

sol = Solution2()
tests = [
    (10, 182),
    (37, 1478),
]

for i, (n, ans) in enumerate(tests):
    res = sol.punishmentNumber(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
