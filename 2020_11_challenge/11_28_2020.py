# from pudb import set_trace; set_trace()
from typing import List
import heapq
import collections


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """TLE. I thought the question is a softball, but I got a TLE in return.
        Very fitting.
        """
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """TLE. Failed on a special case where nums is reversely sorted.
        I kinda wished this case wouldn't happen, but who am I kidding.
        """
        res = [max(nums[:k])]
        cur_max = res[0]
        for i in range(k, len(nums)):
            if nums[i - k] != cur_max:
                cur_max = max(cur_max, nums[i])
            else:
                cur_max = max(nums[i - k + 1:i + 1])
            res.append(cur_max)
        return res


class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Passed OJ with 7% ranking. O(nlog(n))

        Used a combination of heapq and Counter. heapq to quickly return the
        current max. Counter to keep track of the state of current window. We
        use counter to determine whether the max on heapq actually exists in the
        current window.
        """
        hq = [-n for n in nums[:k]]
        heapq.heapify(hq)
        counter = collections.Counter(hq)
        res = [-hq[0]]
        for i in range(k, len(nums)):
            counter[-nums[i - k]] -= 1  # lost a number
            while hq and counter[hq[0]] <= 0:  # remove all the max that is not in the window
                heapq.heappop(hq)
            counter[-nums[i]] += 1  # gained a number
            heapq.heappush(hq, -nums[i])  # add the gained number to the heap
            res.append(-hq[0])
        return res


class Solution4:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Standard solution from the discussion using deque
        68% ranking, O(n)
        """
        # indices stores the indices of the number in nums in sorted decreasing
        # order within each window.
        indices = collections.deque()
        res = []
        for i in range(len(nums)):
            while indices and indices[0] < i - k + 1:  # indices[0] not in window
                indices.popleft()
            while indices and nums[indices[-1]] < nums[i]:  # new value bigger than tails
                indices.pop()
            indices.append(i)
            if i >= k - 1:
                res.append(nums[indices[0]])
        return res


sol = Solution4()
tests = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1]),
    ([1, -1], 1, [1, -1]),
    ([9, 11], 2, [11]),
    ([4, -2], 2, [4]),
]

for i, (num, k, ans) in enumerate(tests):
    res = sol.maxSlidingWindow(num, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
