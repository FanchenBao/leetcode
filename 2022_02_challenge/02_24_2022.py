# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 148

        Merge sort.

        O(NlogN) time, O(1) space if not counting recursion.

        410 ms, 73% ranking
        """
        if not head or not head.next:
            return head
        dummy = ListNode(next=head)
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sorted_right = self.sortList(slow.next)
        slow.next = None
        sorted_left = self.sortList(head)
        # merge
        node = dummy
        while sorted_left and sorted_right:
            if sorted_left.val <= sorted_right.val:
                node.next = sorted_left
                sorted_left = sorted_left.next
            else:
                node.next = sorted_right
                sorted_right = sorted_right.next
            node = node.next
        node.next = sorted_left if sorted_left else sorted_right
        return dummy.next
        

sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
