# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """I feel like this is a cheat. We are using additional memory for this
        and it reaches 16% ranking.
        """
        l1_str = l2_str = ''
        l1_node = l1
        l2_node = l2
        while l1_node:
            l1_str = str(l1_node.val) + l1_str
            l1_node = l1_node.next
        while l2_node:
            l2_str = str(l2_node.val) + l2_str
            l2_node = l2_node.next
        sum_str = ''
        carry = 0
        n1, n2 = len(l1_str), len(l2_str)
        for i in range(max(n1, n2)):
            d1 = int(l1_str[i]) if i < n1 else 0
            d2 = int(l2_str[i]) if i < n2 else 0
            s = d1 + d2 + carry
            sum_str += str(s % 10)
            carry = s // 10
        if carry:
            sum_str += str(carry)
        dummy = ListNode()
        cur = dummy
        for d in sum_str[::-1]:
            cur.next = ListNode(val=int(d))
            cur = cur.next
        return dummy.next


class Solution2:
    def count(self, head: ListNode) -> int:
        node = head
        c = 0
        while node:
            c += 1
            node = node.next
        return c

    def reverse(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        left, right = dummy, head
        while right:
            temp = right
            right = right.next
            temp.next = left
            left = temp
        head.next = None
        return left

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """This one is less cheating. Got 27% ranking.

        It also does not reverse l1 and l2. It first align the two linked list
        relative to their ends. Then perform addition for each location without
        the regard for carrying. After the first round of addition, the
        resulting linked list is traversed from right to left, and any carries
        are added here. Finally we reverse the resulting linked list and that
        is our answer.
        """
        n1, n2 = self.count(l1), self.count(l2)
        l1_node, l2_node = l1, l2
        dummy = ListNode()
        # leave an additional pos for possible carry ahead of the first digit
        tail = ListNode(val=0, next=dummy)
        left = tail
        for _ in range(abs(n1 - n2)):  # align
            if n1 > n2:
                temp = ListNode(val=l1_node.val, next=left)
                l1_node = l1_node.next
            else:
                temp = ListNode(val=l2_node.val, next=left)
                l2_node = l2_node.next
            left = temp
        while l1_node and l2_node:
            temp = ListNode(val=l1_node.val + l2_node.val, next=left)
            left = temp
            l1_node = l1_node.next
            l2_node = l2_node.next
        tail.next = None
        cur, carry = left, 0
        while cur:
            cur.val += carry
            carry = cur.val // 10
            cur.val %= 10
            cur = cur.next
        res_head = self.reverse(left)
        if res_head.val == 0:
            res_head = res_head.next
        return res_head


# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
