# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre

    def pairSum(self, head: Optional[ListNode]) -> int:
        """LeetCode 2130

        We reverse the second half of the linked list. Find the max twin sum.
        And finally reverse the second half back.

        O(N), 969 ms, faster than 32.79%
        """
        slow, fast = head, head
        while fast:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        tail = self.reverse(mid)
        res = 0
        front, back = head, tail
        while back:
            res = max(res, front.val + back.val)
            front = front.next
            back = back.next
        # clean up
        self.reverse(tail)
        return res
        

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
