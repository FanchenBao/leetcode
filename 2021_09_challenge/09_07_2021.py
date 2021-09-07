# from pudb import set_trace; set_trace()
from typing import List, Tuple, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 206

        Iterative. O(N), 36 ms, 70% ranking.
        """
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        return pre


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive. O(N), 36 ms.
        """
        if not head:
            return None

        def reverse(head: ListNode) -> Tuple[ListNode, ListNode]:
            if not head.next:
                return head, head
            new_head, tail = reverse(head.next)
            tail.next = head
            head.next = None
            return new_head, head

        return reverse(head)[0]


class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Better recursion
        """
        if not head or not head.next:
            return head
        tail = head.next
        new_head = self.reverseList(head.next)
        tail.next = head
        head.next = None
        return new_head


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
