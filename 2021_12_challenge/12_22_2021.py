# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre, cur = head, head.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        head.next = None
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """LeetCode 143

        Split the given linked list into two halves. Subject the second half
        to a reverse operation. Then the problem becomes merging two linked list
        in zigzao pattern.

        92 ms, 71% ranking.

        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head_rev = self.reverse(slow.next)
        slow.next = None
        n1, n2 = head, head_rev
        while n1 and n2:
            temp = n1.next
            n1.next = n2
            n1 = temp
            n1, n2 = n2, n1
        return head


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
