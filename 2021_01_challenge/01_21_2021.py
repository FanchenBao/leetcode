# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_left
import heapq


class Solution1:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """A very convoluted solution, leveraging a heap and two dicts.

        We use the heap to keep track of the current min value. We use one
        dict to record each value's indices, such that when a min value is
        pulled out, we can identify whether it is a suitable fit given the
        current index on nums (i_nums). If the current min value's right most
        index is smaller than i_nums, this min value is no longer useful. We
        discard it. If it's left most index that is larger than i_nums is too
        small to house the remaining numbers required by k, we put the value
        in a temp list and search for the next min value. Once a min value's
        left most index that is larger than i_nums is good enough, we take it
        and put it in res. Finally, we put back all the min values from temp
        to the heap. If a min value has been exhausted, we do not put it back
        in the heap.

        A final trick of speeding up: if the remaining available numbers
        happens to fit the requirement of k, we put them in res immediately.

        O(Nlog(N)K), 1740 ms, 13% ranking.
        """
        pos = defaultdict(list)
        counter = defaultdict(int)
        for i, n in enumerate(nums):
            pos[n].append(i)
            counter[n] += 1
        heap = list(pos.keys())
        heapq.heapify(heap)
        res = []
        i_nums, size = 0, len(nums)
        temp = []
        while len(res) < k:
            while True:
                pot_min = heapq.heappop(heap)  # potential min
                pi = bisect_left(pos[pot_min], i_nums)  # index in pos[pot_min]
                if pi == len(pos[pot_min]):  # pot_min is no longer useful
                    continue
                lmp = pos[pot_min][pi]  # left most pos larger than i_nums
                if size - lmp < k - len(res):  # lmp too big, save for later
                    temp.append(pot_min)
                else:
                    break
            if size - lmp == k - len(res):  # we are done here
                res += nums[lmp:]
                break
            res.append(pot_min)
            counter[pot_min] -= 1
            if counter[pot_min]:
                heapq.heappush(heap, pot_min)
            while temp:  # return the min values back to heap
                heapq.heappush(heap, temp.pop())
            i_nums = lmp + 1
        return res


class Solution2:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """The official stack method. Thanks to lee215. I should've thought
        of it myself, because this is not any different from the rain water
        collection problem: we are finding an increasing stack of numbers in
        a given list.

        O(N), 1312 ms, 55% ranking.
        """
        stack = []
        size = len(nums)
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(stack) + size - i > k:
                stack.pop()
            stack.append(n)
        return stack[:k]


sol = Solution2()
tests = [
    ([3, 5, 2, 6], 2, [2, 6]),
    ([2, 4, 3, 3, 5, 4, 9, 6], 4, [2, 3, 3, 4]),
    ([3, 5, 2, 6, 4, 3, 2, 1, 2, 3], 4, [2, 1, 2, 3]),
    ([1], 1, [1]),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.mostCompetitive(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
