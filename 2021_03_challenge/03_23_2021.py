# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """LeetCode 923

        First of all, we need to realize that the requirement on indices i, j
        and k is just a distraction. We don't have to worry about that at all.
        Then the problem becomes how many ways there are to pick three numbers
        from arr that sum up to target. Our solution is to fix the first and
        second values, and examine whether a third value can be found in arr.
        To make this process systemic, we convert the arr into a counter. Thus
        we have knowledge of the number of repeats each value has. Then, when
        we fix the first and second values, we make sure that it is done in a
        non-descending order. This is to avoid double counting. When we obtain
        the third value. Since we are always iterating in a non-descending
        order, if the third value does not follow the order, we know that the
        current iteration is over. This allows us early stop. Similarly, we can
        do early stop with the first value as well. If the first value is larger
        than half of the target, it is guaranteed that with our scheme, no
        solution will be found.

        O(N^2), 72 ms, 92% ranking.
        """
        counter = Counter(arr)
        vals = sorted(counter.keys())
        res = 0
        for i, a in enumerate(vals):
            if a > target // 2:
                break
            for j in range(i, len(vals)):
                b, c = vals[j], target - a - vals[j]
                if c < b:
                    break
                if c in counter:
                    if a == b and b != c:
                        res += math.comb(counter[a], 2) * counter[c]
                    elif a != b and b == c:
                        res += math.comb(counter[b], 2) * counter[a]
                    elif a == c:
                        res += math.comb(counter[a], 3)
                    else:
                        res += counter[a] * counter[b] * counter[c]
        return res % 1000000007


sol = Solution()
tests = [
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20),
    ([1, 1, 2, 2, 2, 2], 5, 12),
    ([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5], 0, 1),
]

for i, (arr, target, ans) in enumerate(tests):
    res = sol.threeSumMulti(arr, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
