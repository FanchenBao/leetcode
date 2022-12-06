# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 328

        Delete all the even nodes and add them to another list. At the end,
        add this even node list to the end of odd node list.

        O(N), 86 ms, faster than 53.72%
        """
        if not head:
            return head
        dummy = ListNode()
        even_node = dummy
        odd_node = head
        while True:
            temp = odd_node.next
            if temp:
                odd_node.next = odd_node.next.next
                even_node.next = temp
                temp.next = None
                even_node = even_node.next
            if odd_node.next:
                odd_node = odd_node.next
            else:
                break
        odd_node.next = dummy.next
        return head




        

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
