# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """LeetCode 1721

        This is the naive way of handling this. Find the total length, and we
        know where the kth node is from the left and from the right.

        O(N), 1750 ms, 20% ranking.
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        cnt = k - 1
        node1 = head
        while cnt:
            node1 = node1.next
            cnt -= 1
        cnt = length - k
        node2 = head
        while cnt:
            node2 = node2.next
            cnt -= 1
        node1.val, node2.val = node2.val, node1.val
        return head


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """One pass solution

        We first locate the kth node from the left, call it node1. Then we
        start a node2 from the beginning, and a temp node from node1. Have
        the temp node and node2 move in sync until the temp node hits
        the last node. Then node2 will point to the kth node from the right.

        O(N), one pass. 1312 ms, 56% ranking.
        """
        node1 = head
        cnt = k - 1
        while cnt:
            node1 = node1.next
            cnt -= 1
        node2, node = head, node1
        while node.next:
            node = node.next
            node2 = node2.next
        node1.val, node2.val = node2.val, node1.val
        return head



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
