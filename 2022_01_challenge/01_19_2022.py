# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 142

        This is a classic problem, and I have encountered it or similar ones
        multiple times. The solution is to use two pointers, one goes twice
        as fast as the other. Thus, if a cycle exists, the two will meet again.
        Then, we place one pointer back at the beginning and the other pointer
        at where they have met. Then move them both one step at a time. The
        next time they meet each other, the node is the start of the cycle.

        Proof:

        Let's say the linked list starts from A, and the loop starts at B, and
        the first time the slow and fast pointers meet at C. And the loop
        length is L, where L = BC + CB

        When fast and slow meet at C, say the slow moves k steps. We have
            
            AB + BC = k

        Fast moves 2k steps. We have

            AB + n * L + BC = 2k

        Thus k = n * L
        Then we need to prove that AB = CB + m * L, where m is some integer

        n * L = AB + BC => BC + CB + (n - 1) * L = AB + BC
        => AB = CB + (n - 1) * L This is exactly what we want to prove.

        Thus, we can say that the point where the slow and fast ponters meet
        for the second time is the start of the loop.

        O(N) time and O(1) space, 67 ms, 35% ranking.
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow


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
