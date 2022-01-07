# from pudb import set_trace; set_trace()
from typing import List
from random import randint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        """LeetCode 382

        Reservoir sampling. I think we have to go through the entire linked
        list to produce each random value. It is not correct to stop
        prematurely.

        O(N), 208 ms, 22% ranking.
        """
        res, cnt = 0, 1
        node = self.head
        while node:
            if 1 == randint(1, cnt):
                res = node.val
            cnt += 1
            node = node.next
        return res



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

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
