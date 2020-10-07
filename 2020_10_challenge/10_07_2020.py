# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """92% ranking. No es tan dificil, pero hay alguno edge casos. Por
        ejemplo, cuando no tenemos elemento en la lista, o cuando el
        numero de elemento para mover es lo mismo que el largo de la lista.
        """
        temp = head
        total = 0
        while temp:
            temp = temp.next
            total += 1
        if total <= 1:  # edge case where there is one or empty list
            return head
        to_move = total - k % total
        if to_move == total:  # to move all elements equals not moving anything
            return head
        new_tail = head
        for _ in range(to_move - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        inter = new_head
        while inter.next:
            inter = inter.next
        inter.next = head
        return new_head


class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """Circula la lista.
        """
        if not head:
            return head
        temp = head
        total = 1
        while temp.next:
            temp = temp.next
            total += 1
        temp.next = head  # circula la lista
        new_tail = head
        for _ in range(total - k % total - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

        


# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
