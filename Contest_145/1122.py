from typing import List, Dict
from collections import defaultdict

"""
07/13/2019

This is the ONLY problem I solved for this week's contest. Very disappointing
to be honest.

Solution2 was the one I saw on discussion, utilizing python's sort function
to do custom sort.

Another solution, which I am not going to write down here, is to count the
number of occurrences of each element in arr1. Then loop through each element
in arr2 and add to the answer the corresponding count of that element recorded
from occurrences in arr1. Once this is done. We add the remaining counts from
the occurrences in arr1 that are not present in arr2, and we are done.
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        assem: Dict[int, List[int]] = defaultdict(list)
        remain: List[int] = []
        for ele in arr1:
            if ele in assem:
                assem[ele].append(ele)
            else:
                remain.append(ele)
        remain.sort()
        res: List[int] = []
        for v in assem.values():
            res += v
        return res + remain

    def solution2(self, arr1, arr2):
        # record the order of element in arr2 as key to sort arr1
        pos = {v: i for i, v in enumerate(arr2)}
        # notice that we use the get() method for the pos dictionary
        # because for elements not in arr2, they need to be placed at
        # the end of arr1, which is to say the position returned must
        # be very large.
        return sorted(arr1, key=lambda x: pos.get(x, 1000 + x))
