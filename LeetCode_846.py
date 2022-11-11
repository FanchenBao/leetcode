# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """This is an easy problem, but I wrongly assumed that my initial idea
        was not O(N). But it was. We use a counter, and then brute force it.
        By brute force, I mean we goes through each possible consecutive
        groupSize number of ranges. If any such range lacks a value, we return
        False. If we can go through the entire counter, we return True.

        The key is to realize that as we go through the counter, each occurrence
        of the value is visited only once. This means the time complexity is
        only O(N + MlogM), where N = len(hand) and M is the number of unique
        cards. 213 ms, faster than 92.56%
        """
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        uniqs = sorted(counter)
        for i in range(len(uniqs)):
            while counter[uniqs[i]]:
                for j in range(uniqs[i], uniqs[i] + groupSize):
                    if counter[j]:
                        counter[j] -= 1
                    else:
                        return False
        return True


sol = Solution()
tests = [
    ([1,2,3,6,2,3,4,7,8], 3, True),
    ([1,2,3,4,5], 4, False),
    ([1,2,3,4,2,3,1,2,3], 3, True),
    ([1,2,3,4,2,3,4,2,3], 3, True),
    ([9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11], 10, False),
    ([8,8,9,7,7,7,6,7,10,6], 2, True),
    ([8,10,12], 3, False),
]

for i, (hand, groupSize, ans) in enumerate(tests):
    res = sol.isNStraightHand(hand, groupSize)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
