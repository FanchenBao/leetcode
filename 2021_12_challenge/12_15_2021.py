# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 147

        Insertion sort that cuts each node from the original list and insert
        into the new list.

        O(N^2), 1652 ms, 52% ranking.
        """
        dummy = ListNode()
        while head:
            sn = dummy
            while sn.next:
                if sn.next.val >= head.val:
                    break
                sn = sn.next
            # cut the node from original list to new list
            head, temp = head.next, head
            sn.next, temp.next = temp, sn.next
        return dummy.next


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
