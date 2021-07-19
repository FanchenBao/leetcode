# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode, tail: ListNode, tail_next: ListNode) -> None:
        pre, cur = tail_next, head
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """LeetCode 25

        This doesn't seem to be too difficult. We basically find the head and
        tail of each k nodes. Perform reverse on it, handle the linkage from the
        previous nodes to the current reversed k nodes, and move on. The edge
        case that caught us was when k == 1. We can of course set k == 1 as a
        special case.

        O(N) time , O(1) space, 48 ms, 79% ranking.
        """
        if k == 1:
            return head
        dummy = ListNode(next=head)
        pre, left, right = dummy, head, head
        while True:
            count = 1
            while right and right.next and count < k:
                right = right.next
                count += 1
            if count == k:
                self.reverse(left, right, right.next)
                pre.next = right
                pre = left
                left = left.next
                right = left
            else:
                break
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
