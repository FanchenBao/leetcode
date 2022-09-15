# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """LeetCode 2007

        Sort changed. Go from small to large. For each value, if it is not a
        previously doubled value, it must be the original value. We also double
        it and keep track of the doubled value. If it is a doubled value, we
        ignore it and remove its count from the track. At the end, we check
        whether the number of original is equal to half of changed.

        This strategy works because doubling the original always ends up with
        some value not smaller than the original. Thus, if we go through
        changed in ascending order, as long as we ignore the doubled value,
        we will always encounter the original.

        One trick is to use Counter to keep track of the doubled value, because
        using a set does not work with repeated doubled values.

        O(NlogN), 3339 ms, faster than 12.60%
        """
        N = len(changed)
        if N % 2:
            return []
        changed.sort()
        res = []
        doubled = Counter()
        for c in changed:
            # print(c, doubled, res)
            if doubled[c] == 0:
                doubled[2 * c] += 1
                res.append(c)
            else:
                doubled[c] -= 1
        if len(res) == N // 2:
            return res
        return []


class Solution2:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """From lee215:

        https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100

        Similar idea but better implementation. Turn the entire changed into
        a counter. Then go from small to large keys. This way, we speed things
        up by going through only unique keys. For each key, the count of
        2 * key must not be smaller than the count of key. And we also remove
        the count of key from the count of 2 * key whenever a key has been
        visited.

        Special case is for 0, because 2 * 0 == 0

        O(N + KlogK), where K is the size of counter. 2813 ms, faster than 26.65%
        """
        if len(changed) % 2:
            return []
        counter = Counter(changed)
        for c in sorted(counter):
            if counter[c] > counter[2 * c]:
                return []
            # update the count of c doubled, also treat c euql to 0 differently
            counter[2 * c] -= counter[c] if c else counter[c] // 2
        return list(counter.elements())  # notice the use of elements


sol = Solution2()
tests = [
    ([1,3,4,2,6,8], [1,3,4]),
    ([6,3,0,1], []),
    ([1], []),
    ([2,4,8,4,8,16], [2,4,8]),
    ([1,2,1,2,1,2], [1,1,1]),
]

for i, (changed, ans) in enumerate(tests):
    res = sol.findOriginalArray(changed)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
