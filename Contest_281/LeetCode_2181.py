# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        cur = head.next
        while cur:
            temp = 0
            while cur.val != 0:
                temp += cur.val
                cur = cur.next
            node.next = ListNode(val=temp)
            node = node.next
            cur = cur.next
        return dummy.next

        


# sol = Solution()
# tests = [
#     ([3,1,3,2,4,3], 3),
#     ([1,2,2,2,2], 2),
#     ([1], 0),
# ]

# for i, (nums, ans) in enumerate(tests):
#     res = sol.minimumOperations(nums)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
