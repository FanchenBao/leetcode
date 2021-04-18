# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """We create a gap of n steps between a left pointer and right pointer.
        When the right pointer reaches the end, the left pointer will point at
        the node right before the target deletion. Then we can easily remove the
        target. Use a dummy node at the very beginning to simplify syntax.

        O(N), 36 ms, 43% ranking.
        """
        dummy = ListNode(next=head)
        left, right = dummy, dummy
        for _ in range(n):
            right = right.next
        while right.next:  # find the node before the one to be removed
            left, right = left.next, right.next
        left.next = left.next.next  # remove the target node
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
