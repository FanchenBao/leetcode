# from pudb import set_trace; set_trace()
from typing import List
import math
import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution1:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        """LeetCode 382

        This is reservoir sampling and it uses O(1) space. But it can be very
        very slow, if the linked list is long.

        O(N) runtime. 366 ms, faster than 5.02%
        """
        node = self.head.next
        val = self.head.val
        i = 1
        while node:
            if random.randint(0, i) == 0:
                val = node.val
            i += 1
            node = node.next
        return val


class Solution2:
    def __init__(self, head: Optional[ListNode]):
        self.lst = []
        while head:
            self.lst.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """Use O(N) space to make the call O(1) in time

        163 ms, faster than 19.15%
        """
        return random.choice(self.lst)


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
