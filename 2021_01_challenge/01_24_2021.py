# from pudb import set_trace; set_trace()
from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """Place the head value of each list into a heap. At each round, we pop
        the top of the heap, which is the min of all the lists' head. This min
        is also the min of all the values currently not visited. We place the
        min in the return list, and push the next value of the list where
        the min has come from into the heap. We continue this process,
        guaranteeing that at each step, only the min of all unvisited values
        are pushed into the new list, until our heap is exhausted.

        Note that since we are using index to indicate which list to increment
        after its head is pushed to the heap, there is no need to implement a
        wrapper class.

        O(Nlog(k)), where N is the average length of all the lists and k is the
        number of lists. 108 ms, 62% ranking.
        """
        heap = []
        for i, root in enumerate(lists):
            if root is not None:
                heapq.heappush(heap, (root.val, i))
                lists[i] = lists[i].next
        dummy = ListNode()
        node = dummy
        while heap:
            cur_val, idx = heapq.heappop(heap)  # current min among all lists
            node.next = ListNode(val=cur_val)  # add current mean to the return
            node = node.next  # the return list head move to the next node
            # increment the list where we just pulled a value
            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """Instead of using index, we can put the node directly in the heap.

        Note that we need to implement a wrapper class to define __lt__ to let
        the heapq know how to make comparisons among elements. Note also that
        even if we push a tuple such as (val, node), we still need to implement
        __lt__, because when val is the same, heapq will compare node to
        determine order.
        """
        class WrapperNode:
            def __init__(self, node: ListNode):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        heap = []
        for root in lists:
            if root is not None:
                heapq.heappush(heap, WrapperNode(root))
        dummy = ListNode()
        node = dummy
        while heap:
            cur_wrapper = heapq.heappop(heap)  # current min among all lists
            node.next = ListNode(val=cur_wrapper.node.val)  # add current mean to the return
            node = node.next  # the return list head move to the next node
            # Push the node next to cur_node into the heap and make sure the next node
            # is not None itself. This way, we guarantee that all the nodes in the
            # heap have value.
            if cur_wrapper.node.next is not None:
                heapq.heappush(heap, WrapperNode(cur_wrapper.node.next))
        return dummy.next


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
