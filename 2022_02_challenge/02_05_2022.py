# from pudb import set_trace; set_trace()
from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """LeetCode 23

        I have done this problem many times so the solution is well known to me
        but I still had more hiccups than I'd like. For the one part, I didn't
        realize that I couldn't put a tuple of (val, ListNode) into heapq,
        because heapq first compares the val, and if the vals are the same, it
        will try to compare the second element, which is ListNode. The ListNode
        prepared by the problem cannot be compared. Thus, we have to use index
        to indicate which linked list the current node belongs to. Furthermore,
        I had to use an extra array to store the current node for each linked
        list.

        The overall logic is not difficult, just keep adding and popping the
        priority queue. Yet the implementation proves to be tricky still.

        O(NlogK), where N is the length of linked list and K is the number
        of linked lists. 205 ms, 24% ranking
        """
        pq = [(head.val, i) for i, head in enumerate(lists)]
        cur_nodes = [head for head in lists]
        heapq.heapify(pq)
        dummy = ListNode()
        node = dummy
        while pq:
            v, idx = heapq.heappop(pq)
            node.next = ListNode(val=cur_nodes[idx].val)
            node = node.next
            if cur_nodes[idx].next:
                heapq.heappush(pq, (cur_nodes[idx].next.val, idx))
                cur_nodes[idx] = cur_nodes[idx].next
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
