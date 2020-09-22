# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Use Counter results in a one-liner.
        
        Pass OJ with 80% ranking. However, this is NOT linear runtime, nor
        O(1) space.
        """
        return [v for v, c in Counter(nums).most_common() if c > len(nums) // 3]


class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Use Boyer-Moore voting algorithm.

        After a lot of trial and error, I finally ended up with a workable
        solution. It scored 92% ranking. The main trick is ca1 == n and ct1 ==
        0 cannot be combined into one condition.
        """
        res = []
        ca1, ca2, ct1, ct2 = 0, 0, 0, 0
        for n in nums:
            if ca1 == n:
                ct1 += 1
            elif ca2 == n:
                ct2 += 1
            elif ct1 == 0:
                ca1 = n
                ct1 += 1
            elif ct2 == 0:
                ca2 = n
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1
        if nums.count(ca1) > len(nums) // 3:
            res.append(ca1)
        if ca1 != ca2 and nums.count(ca2) > len(nums) // 3:
            res.append(ca2)
        return res


sol = Solution2()
print(sol.majorityElement([1, 2, 2, 3, 2, 1, 1, 3]))
