# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """LeetCode 1721

        Two sets of edge cases. First, when swap_l and swap_r are adjacent, we
        must swap them directly without resorting to another node in between.

        Second, when k is big and swap_l ends up to the right of swap_r, and if
        they are adjacent, the swap is the opposite compared to when swap_l is
        to the left of swap_r.

        O(N), 959 ms, faster than 87.97%
        """
        dummy = ListNode(next=head)
        swap_r_pre = hi = dummy
        for _ in range(k):
            hi = hi.next
        while hi.next:
            hi = hi.next
            swap_r_pre = swap_r_pre.next
        swap_l_pre = dummy
        for _ in range(k - 1):
            swap_l_pre = swap_l_pre.next
        swap_l, swap_l_next = swap_l_pre.next, swap_l_pre.next.next
        swap_r, swap_r_next = swap_r_pre.next, swap_r_pre.next.next
        if swap_l.next == swap_r:  # if the swaps are adjacent
            swap_l_pre.next = swap_r
            swap_r.next = swap_l
            swap_l.next = swap_r_next
        elif swap_r.next == swap_l:  # if swap_l is on the right to swap_r
            swap_r_pre.next = swap_l
            swap_l.next = swap_r
            swap_r.next = swap_l_next
        else:
            swap_l_pre.next = swap_r
            swap_r.next = swap_l_next
            swap_r_pre.next = swap_l
            swap_l.next = swap_r_next
        return dummy.next

        

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
