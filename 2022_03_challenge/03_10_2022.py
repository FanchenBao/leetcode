# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 2

        Pure list node operations.

        O(N), 106 ms, 40% ranking.
        """
        dummy = ListNode()
        node = dummy
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry, s = divmod(s, 10)
            node.next = ListNode(val=s)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        while carry and node.next:
            s = node.next.val + carry
            carry, node.next.val = divmod(s, 10)
            node = node.next
        if carry:
            node.next = ListNode(val=carry)
        return dummy.next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Get the number, perform addition, and turn the result into linked
        list.
        """
        num1 = 0
        count = 0
        while l1:
            num1 += l1.val * (10**count)
            l1 = l1.next
        num2 = 0
        count = 0
        while l2:
            num2 += l2.val * (10**count)
            l2 = l2.next
        res = l1 + l2
        dummy = ListNode()
        node = dummy
        while res:
            node.next = ListNode(val=res % 10)
            node = node.next
            res //= 10
        return dummy.next
        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
