# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """LeetCode 141

        Very classical and old problem. Two pointers, one slow and one fast.
        If slow catches up to fast, there must be a cycle.

        O(N), 60 ms, 79% ranking.
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True            
        return False


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
