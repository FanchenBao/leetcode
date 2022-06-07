# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """LeetCode 160

        O(M + N) time and space. 187 ms, faster than 62.32%
        """
        addrs = set()
        node = headA
        while node:
            addrs.add(id(node))
            node = node.next
        node = headB
        while node:
            if id(node) in addrs:
                return node
            node = node.next
        return None


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """O(1) extra space.

        The idea is to run both linked lists to the end. If one of them exits
        first, we creae a new head for the other one and keep running until the
        other linked list exhausts. By doing this, we are able to make sure
        the two linked lists start at the same position. Then we traverse them
        again and once the two linked lists have the same node, that is the one
        to return.

        O(M + N) time and O(1) space. 170 ms, faster than 80.06%
        """
        na, nb = headA, headB
        while na and nb:
            na = na.next
            nb = nb.next
        if na:
            nl = headA
            while na:
                na = na.next
                nl = nl.next
            ns = headB
        elif nb:
            nl = headB
            while nb:
                nb = nb.next
                nl = nl.next
            ns = headA
        else:
            nl, ns = headA, headB
        while nl and ns:
            if nl is ns:
                return nl
            nl = nl.next
            ns = ns.next
        return None


class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """This is the same idea as solution2, but gawdy this one is good. Two
        tricks are here. First, we use `na = na.next` if na else headA to perform
        the wrap around. Second, we use `while na is not nb` to make sure the
        only condition where the loop exits is when either na and nb points to
        the same node or they are both None. Brilliant.

        IMPORTANT: don't forget to swap headA and headB within the loop!!
        """
        na, nb = headA, headB
        while na is not nb:
            na = na.next if na else headB
            nb = nb.next if nb else headA
        return na



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
