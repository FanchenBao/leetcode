# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        LeetCode 1207

        Use counter to find the frequencies of each value and check whether
        these frequencies themselves are unique.
        
        O(N), 39 ms, faster than 82.48% 

        Args:
            arr: 

        Returns:
            
        """
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter)



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
