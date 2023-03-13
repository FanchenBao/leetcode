# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """LeetCode 23

        This is a classic problem. This is the fourth time I have solved it, but
        it has better performance than the second and the third time. The main
        reason, I think, is that I have an early stop on the while loop. Instead
        of exhausting everything in heap, I exist the loop when the size of
        heap becomes one. This means all the other linked lists have been
        exhausted, and thus the remaining values must all come from the linked
        list in the heap and its original order. So we can save the trouble of
        traversing a linked list that we will add to the final result in the
        same order anyway.

        The reason I thought about it this time is that I was peeling off each
        element of the linked list during the while loop, instead of creating
        new ones. Basically, no new node is created (except from the dummy) in
        this solution.

        O(MlogN), where N = len(lists) and M is the length of the second longest
        linked list inside lists.

        93 ms, faster than 93.56%
        """
        heap = [(head.val, i) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)
        dummy = ListNode()
        node = dummy
        while len(heap) > 1:
            _, idx = heapq.heappop(heap)
            # take the head of lists[idx] out
            tmp_node = lists[idx]
            lists[idx] = tmp_node.next
            tmp_node.next = None
            # extend the result linked list
            node.next = tmp_node
            node = node.next
            # add new val to heap
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        if heap:
            node.next = lists[heap[0][1]]
        return dummy.next

        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
