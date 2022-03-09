# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 82

        One pass solution. Very straightforward.

        O(N), 73 ms, 23% ranking.
        """
        dummy = ListNode(next=head)
        anchor, cur = dummy, head
        is_consec = False
        while cur:
            if cur.next and cur.next.val == cur.val:
                is_consec = True
            elif is_consec:
                anchor.next = cur.next
                is_consec = False
            else:
                anchor = anchor.next
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
