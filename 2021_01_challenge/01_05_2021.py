# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Use three pointers: ln, mn, and rn, one pass. mn and rn are used to
        determine duplicates. They keep moving forwards and are always adjacent.
        ln lags behind. Once duplicates are found, mn and rn keep walking
        forward until all the duplicates are exhausted. Then ln links to rn to
        delete all the duplicates in between. The tricky part is when the loop
        exists, we have to check for dup one more time because the list can
        consiste of all duplicates.

        O(N), 40 ms, 71% ranking.
        """
        dummy1 = ListNode(val=-101, next=head)
        dummy0 = ListNode(next=dummy1)
        ln, mn, rn = dummy0, dummy1, head
        dup = False
        while rn:
            if mn.val == rn.val:
                dup = True
                mn = mn.next
            elif dup:
                ln.next = rn
                mn = rn
                dup = False
            else:
                ln = ln.next
                mn = mn.next
                dup = False
            rn = rn.next
        if dup:
            ln.next = rn
        return dummy1.next


class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Use two points instead of three

        O(N), 32 ms, 97% ranking
        """
        dummy = ListNode(val=-101, next=head)
        ln, rn = dummy, head
        dup = False
        while rn.next:
            if rn.val == rn.next.val:
                dup = True
            elif dup:
                ln.next = rn.next
                dup = False
            else:
                ln = ln.next
            rn = rn.next
        if dup:
            ln.next = rn.next
        return dummy.next


class Solution3:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Recursion

        O(N), 40 ms, 71% ranking
        """
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            while head and head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)


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
