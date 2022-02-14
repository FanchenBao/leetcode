# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, deque
import heapq



class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """TLE
        """
        num_counter = Counter(nums)
        slot_state = Counter()
        self.res = 0
        for _ in range(2):
            for i in range(1, numSlots + 1):
                if i in num_counter:
                    self.res += i
                    num_counter[i] -= 1
                    slot_state[i] += 1
                    if num_counter[i] == 0:
                        del num_counter[i]
        choices = []
        for n, cnt in num_counter.items():
            for _ in range(cnt):
                choices.append([])
                for i in range(1, numSlots + 1):
                    if slot_state[i] < 2:
                        choices[-1].append((n & i, i))
        N = len(choices)

        def backtrack(idx: int, cur_sum: int) -> None:
            if idx == N:
                self.res = max(self.res, cur_sum)
            else:
                for val, slot in choices[idx]:
                    if slot_state[slot] < 2:
                        slot_state[slot] += 1
                        backtrack(idx + 1, cur_sum + val)
                        slot_state[slot] -= 1

        backtrack(0, self.res)
        return self.res


sol = Solution()
tests = [
    ([1, 2, 3, 4, 5, 6], 3, 9),
    ([1, 3, 10, 4, 7, 1], 9, 24),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3],9,90),
    ([1], 2, 1),
    ([15,13,4,4,11,6,6,12,15,7,3,12,13,7],8,70),
]

for i, (nums, numSlots, ans) in enumerate(tests):
    res = sol.maximumANDSum(nums, numSlots)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
