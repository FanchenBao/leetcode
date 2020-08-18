# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    # def process(self, d1, val_per_pos):



    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = []
        all_pos = [[set() for _ in range(N - 1)] for _ in range(10)]
        for i in range(1, 10):
            pre_set = {i}
            for cur_set in all_pos[i]:
                for val in pre_set:
                    if 0 <= val + K <= 9:
                        cur_set.add(val + K)
                    if 0 <= val - K <= 9:
                        cur_set.add(val - K)
                if cur_set:
                    pre_set = cur_set
                else:
                    break
            # if all_pos[i][0]:
            #     res += self.process(i, all_pos[i])
        return res


sol = Solution()

sol.numsSameConsecDiff(9, 1)
