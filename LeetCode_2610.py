# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """Just pick all the unqiue values from nums to fill the first row. Then
        the remaining uniques for the second row, so on and so forth.

        O(N), 77 ms, faster than 9.54%
        """
        counter = Counter(nums)
        res = []
        while counter:
            res.append([])
            for k in list(counter.keys()):
                res[-1].append(k)
                counter[k] -= 1
                if not counter[k]:
                    del counter[k]
        return res
        

class Solution2:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """From lee215: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/discuss/3368523/JavaC%2B%2BPython-Maximum-Frequence

        Very smart way of using Counter. We can find the max frequency in
        counter, which represents the total number of rows in the result.

        Then we use this nifty method called elements(), which outputs
        "an iterator over elements repeating each as many times as its count."

        Then we just need to pick every k values, where k is the max frequency,
        and it is guaranteed that all the values picked are unique. Here, he
        uses a smart slicing notation of list.

        O(N), 60 ms, faster than 58.48%
        """
        counter = Counter(nums)
        max_freq = max(counter.values())
        repeats = list(counter.elements())
        return [repeats[i::max_freq] for i in range(max_freq)]

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
