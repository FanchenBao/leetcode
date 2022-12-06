# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 876

        Tortoise and hare

        41 ms, faster than 78.28% 
        """
        slow, fast = head, head
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next
        return slow


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
