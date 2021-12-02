# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 328

        This is not hard in terms of algo, but the logic does require some
        attention. The idea is to keep a pointer right before the first even
        node, and keep another pointer right before the next odd node. Then we
        simply insert the next odd node before the first even node.

        O(N) time, O(1) space, 44 ms, 68% ranking.
        """
        if not head or not head.next:
            return head
        pre_fe = head
        pre_cur = head.next
        while pre_cur and pre_cur.next:
            fe = pre_fe.next
            ne = pre_cur.next.next
            pre_fe.next = pre_cur.next
            pre_cur.next.next = fe
            pre_cur.next = ne
            pre_fe = pre_fe.next
            pre_cur = pre_cur.next
        return head


class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """This is from the official solution.
        
        It has simpler logic than Solution1. We extrac all even nodes into a
        separate linked list, and link the odd nodes to the even nodes at the
        end.

        40 ms, 86% ranking.
        """
        if not head or not head.next:
            return head
        even_head = ListNode()
        odd = head
        even_tail = even_head
        while odd.next:
            even_tail.next = odd.next
            odd.next = odd.next.next
            even_tail = even_tail.next
            if odd.next:
                odd = odd.next
        even_tail.next = None
        odd.next = even_head.next
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
