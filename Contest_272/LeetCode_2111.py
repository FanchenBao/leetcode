# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def longest_increasing_subseq_len(self, lst: List[int]) -> int:
        last_val = [0]
        lengths = [0]
        for val in lst:
            idx = bisect_right(last_val, val)
            if last_val[idx - 1] == val:
                lengths[idx - 1] += 1
            elif idx == len(last_val):
                last_val.append(val)
                lengths.append(lengths[-1] + 1)
            else:
                last_val[idx] = val
                lengths[idx] = lengths[idx - 1] + 1
        print(last_val, lengths)
        return max(lengths)

    def kIncreasing(self, arr: List[int], k: int) -> int:
        remain, start, res = len(arr), 0, 0
        while remain:
            lst = [arr[i] for i in range(start, len(arr), k)]
            res += len(lst) - self.longest_increasing_subseq_len(lst)
            remain -= len(lst)
            start += 1
        return res


sol = Solution()
tests = [
    # ([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3], 1, 12),
    # ([5,4,3,2,1], 1, 4),
    # ([4,1,5,2,6,2], 2, 0),
    # ([4,1,5,2,6,2], 3, 2),
    ([2,2,2,2,2,1,1,4,4,3,3,3,3,3], 1, 4),
]

for i, (arr, k, ans) in enumerate(tests):
    res = sol.kIncreasing(arr, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
