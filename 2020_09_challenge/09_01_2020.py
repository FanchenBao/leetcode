# from pudb import set_trace; set_trace()
from typing import List
from itertools import permutations
from time import strftime, strptime


class Solution1:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        """Built-in permutation and time module"""
        valid_times = []
        for h1, h2, m1, m2 in permutations(A, len(A)):
            try:
                valid_times.append(strptime(f'{h1}{h2}:{m1}{m2}', '%H:%M'))
            except Exception:
                pass
        try:
            return strftime('%H:%M', max(valid_times))
        except ValueError:
            return ''


class Solution2:
    def full_permute(
        self,
        lst: List[int],
        idx: int,
        permutes: List[List[int]],
    ) -> None:
        """Using the swap method to pin the value that does not change, and permute the rest"""
        if idx == len(lst) - 1:
            permutes.append(lst[:])
            return
        for i in range(idx, len(lst)):
            lst[idx], lst[i] = lst[i], lst[idx]  # swap to pin the ith value
            self.full_permute(lst, idx + 1, permutes)
            lst[i], lst[idx] = lst[idx], lst[i]  # backtrack
        return

    def largestTimeFromDigits(self, A: List[int]) -> str:
        """Hand-craft permutation and time string parser"""
        max_time = ''
        permutes = []
        self.full_permute(A, 0, permutes)
        print(permutes)
        for h1, h2, m1, m2 in permutes:
            hour = h1 * 10 + h2
            minutes = m1 * 10 + m2
            if hour < 24 and minutes < 60:
                max_time = max(max_time, f'{h1}{h2}:{m1}{m2}')
        return max_time



sol = Solution2()
print(sol.largestTimeFromDigits([1, 2, 3, 4]))

        