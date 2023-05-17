# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 24

        48 ms, faster than 16.98%
        """
        dummy = ListNode(next=head)
        n1, n2 = dummy, head
        while n2 and n2.next:
            t = n2.next
            n2.next = t.next
            n1.next = t
            t.next = n2
            n2 = n2.next
            n1 = n1.next.next
        return dummy.next



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
