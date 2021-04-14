# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """LeetCode 86

        Straightforward solution. We look for the first node whose value is
        >= x. That node determines where future smaller nodes will be
        inserted. Then we keep moving forward and cut the node that is smaller
        than x and insert it right before the first node that is >= x. Keep
        doing this until we hit the end.

        O(N), 36 ms, 54% ranking.
        """
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        while cur:
            if cur.val >= x:
                break
            cur = cur.next
            pre = pre.next
        while cur and cur.next:
            if cur.next.val >= x:
                cur = cur.next
            else:
                # cut
                temp = cur.next
                cur.next = temp.next
                # paste
                temp.next = pre.next
                pre.next = temp
                pre = pre.next
        return dummy.next


class Solution2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """This is the official solution. It is not any better than Solution1,
        but it does require less mental effort.
        """
        left, right = ListNode(), ListNode()
        node, nl, nr = head, left, right
        while node:
            if node.val < x:
                nl.next = node
                nl = nl.next
            else:
                nr.next = node
                nr = nr.next
            temp = node
            node = node.next
            temp.next = None  # cut the link when a node goes to left or right
        nl.next = right.next
        return left.next


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
