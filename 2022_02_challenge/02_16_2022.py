# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 24

        Straightforward swapping. Pay attention to the scenario where the size
        of the linked list is odd.
        
        O(N), 52 ms, 28% ranking.
        """
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        while cur and cur.next:
            temp = cur.next
            pre.next = temp
            cur.next = temp.next
            temp.next = cur
            pre = cur
            cur = cur.next
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
