# from pudb import set_trace; set_trace()
from typing import List
import math
import random
from collections import Counter
from itertools import chain


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """LeetCode 912

        Not as easy as I had expected, because of some tricky test cases.
        Quicksort depends on the input array to be as randomly ordered as
        possible. Thus, we need to shuffle it to take advantage of divide and
        conquer.

        On the other hand, we have to also deal with duplicates, in case the
        entire input array consists of the same number. We use a counter, which
        allows us to sort only the unique values.

        Combining these two tricks, we are able to pass the OJ.

        O(NlogN), 1720 ms, faster than 70.50%

        UPDATE: a better way to randomize. We only need to randomize the pivot
        """
        
        def quicksort(lo: int, hi: int, list_nums: List[int]) -> None:
            if lo >= hi:
                return
            pivot = random.randint(lo, hi)
            list_nums[lo], list_nums[pivot] = list_nums[pivot], list_nums[lo]
            st, ed = lo, hi
            while lo < hi:
                if list_nums[lo] <= list_nums[st]:
                    lo += 1
                else:
                    list_nums[lo], list_nums[hi] = list_nums[hi], list_nums[lo]
                    hi -= 1
            if list_nums[lo] > list_nums[st]:
                lo -= 1
            list_nums[st], list_nums[lo] = list_nums[lo], list_nums[st]
            quicksort(st, lo - 1, list_nums)
            quicksort(lo + 1, ed, list_nums)

        counter = Counter(nums)
        keys = list(counter.keys())
        quicksort(0, len(keys) - 1, keys)
        return list(chain(*([k] * counter[k] for k in keys)))
        

sol = Solution()
tests = [
    ([5,2,3,1], [1,2,3,5]),
    ([5,1,1,2,0,0], [0,0,1,1,2,5]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.sortArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
