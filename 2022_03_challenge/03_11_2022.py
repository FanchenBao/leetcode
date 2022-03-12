# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """LeetCode 61

        Count the total number of nodes, find k % count. This tells us how many
        nodes counting from the tail need to be moved to the front. Note that
        if the remainder is 0, we can directly return the original list.
        Otherwise, we walk a prehead node all the way to the node immediately
        prior to the new head, and make the cut-and-paste.

        O(N), 42 ms, 75% ranking.
        """
        if not head:  # another edge case
            return head
        count = 1
        tail = head
        while tail.next:
            count += 1
            tail = tail.next
        r = k % count
        if r == 0:  # handle edge case
            return head
        prehead = head
        for _ in range(count - r - 1):
            prehead = prehead.next
        newhead = prehead.next
        prehead.next = None
        tail.next = head
        return newhead

        

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
