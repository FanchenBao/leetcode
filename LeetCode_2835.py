# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def break_into_power_of_two(self, val: int) -> List[int]:
        res = []
        cnt = 0
        while val:
            while val & 1 == 0:
                val >>= 1
                cnt += 1
            res.append(1 << cnt)
            val >>= 1
            cnt += 1
        return res

    def minOperations(self, nums: List[int], target: int) -> int:
        """
        This is completely from the hint. I was not able to figure this out.

        Two key leap of logic.

        1. Given a power of 2, let's call it k. And given a list of power of
        2 smaller than k. If the sum of the list is larger than k, then adding
        from the largest value in the list, there will always be a time when
        the sum is equal to k.

        2. To find some values in the list and add them up to be k, it is always
        better to use the largest values first, because this reduces the chance
        of splitting values down the line.

        This implementation leverages two heaps. A min heap and a max heap.
        We start with the min heap to put everything in nums into the heap.
        Then we pop the top that is smaller than the least significant bit of
        target. Each time a value is popped, we add it up and push it to the
        max heap. Once all smaller
        values are popped, we know whether their sum is bigger or smaller than
        the least significant bit.

        If bigger, we use the max heap to pop the largest values that can add
        up to the least significant bit. Then we continue with the next least
        significant bit.

        If smaller, we split the top of the min heap and add the value (if it
        is smaller) to the max heap.

        51 ms, faster than 82.19%
        """
        if sum(nums) < target:
            return -1
        minHeap = nums
        maxHeap: List[int] = []
        heapq.heapify(minHeap)
        res = 0
        cur_sum = 0
        for lsb in self.break_into_power_of_two(target):
            while minHeap and minHeap[0] <= lsb:
                m = heapq.heappop(minHeap)
                cur_sum += m
                heapq.heappush(maxHeap, -m)
            while minHeap and cur_sum < lsb:  # split
                half = heapq.heappop(minHeap) // 2
                res += 1
                if half > lsb:
                    heapq.heappush(minHeap, half)
                    heapq.heappush(minHeap, half)
                else:
                    cur_sum += half * 2
                    heapq.heappush(maxHeap, -half)
                    heapq.heappush(maxHeap, -half)
            add_up = 0
            while maxHeap and add_up < lsb:
                n = -heapq.heappop(maxHeap)
                add_up += n
                cur_sum -= n
        return res


sol = Solution()
tests = [
    # ([1, 32, 1, 2], 12, 2),
    ([1, 1, 1, 1, 128, 1, 64, 8], 7, 1),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.minOperations(nums, target)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
