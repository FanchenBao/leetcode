# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        counter = Counter(prizePositions)
        pos = list(counter.keys())
        if pos[0] + 2 * k + 1 >= pos[-1]:
            return sum(prizePositions)
        
        lst = []
        hi = 0
        for lo, p in enumerate(pos):
            cur = 0 if not lst or lst[-1] - counter[pos[lo - 1]]
            while hi < len(pos) and pos[hi] <= p + k:
                cur += counter[pos[hi]]
                hi += 1
            lst.append(cur)
        print(lst)

        

sol = Solution()
tests = [
    
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
