# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def kadane_ish(self, arr: List[int]) -> int:
        # Kadane aux to find the max and min sum of subarray
        # However, it is not the vanilla Kadane, because we require that
        # the subarray to contain at least one 1 and one -1. Thus, an
        # example of [1, 1, -1, -1] shall return 1, instead of 2. To
        # solve this, we need to know which subarray produces the max or
        # min sum. If the subarray length is the same as the max or min
        # sum, that means we have not included any of the opposite value.
        # Thus, the real value has to be that max or min reducing one.
        kmax, kmin = -math.inf, math.inf
        kmax_idx = kmin_idx = 0
        cmax, cmin = 0, 0
        max_start, min_start = [], []
        for i, a in enumerate(arr):
            # find max
            if cmax + a >= a:
                cmax = cmax + a
                if max_start:
                    max_start.append(max_start[-1])
                else:
                    max_start.append(i)
            else:
                cmax = a
                max_start.append(i)
            if cmax > kmax or (cmax == kmax and i - max_start[i] + 1 > cmax):
                kmax = cmax
                kmax_idx = i
            # find min
            if cmin + a <= a:
                cmin = cmin + a
                if min_start:
                    min_start.append(min_start[-1])
                else:
                    min_start.append(i)
            else:
                cmin = a
                min_start.append(i)
            if cmin < kmin or (cmin == kmin and i - min_start[i] + 1 > -cmin):
                kmin = cmin
                kmin_idx = i
        # kmax and kmin need to be adjusted if there is no opposite
        # value in the max or min subarray sum
        if kmax_idx - max_start[kmax_idx] + 1 == kmax:
            kmax -= 1
        if kmin_idx - min_start[kmin_idx] + 1 == -kmin:
            kmin += 1
        return max(kmax, -kmin)

    def largestVariance(self, s: str) -> int:
        """LeetCode 2272 (Hint)

        Very very tough. I tried DP, but didn't work. Checked the hint, realized
        that it can be solved using Kadane, but not exactly Kadane. After we
        swap all the pairs into 1 and -1, Kadane can tell us the max or min
        subarray sum. However, we need to include at least one value of the
        opposite side. Thus, if the Kadane max or min only contains one value,
        it is invalid. To detect that, I have to record the starting position
        of each max or min subarray sum. And if the length of the subarray is
        equal to max or min, that means we do not include any opposite value.
        And the Kadane max or min must deduct one before being considered for
        the final answer.

        O(26 * 26 * N), 2923 ms, faster than 88.03%
        """
        uniqs = list(set(s))
        res = 0
        for i in range(len(uniqs)):
            for j in range(i + 1, len(uniqs)):
                aux = []
                for k in range(len(s)):
                    if s[k] == uniqs[i]:
                        aux.append(1)
                    elif s[k] == uniqs[j]:
                        aux.append(-1)
                res = max(res, self.kadane_ish(aux))
        return res


class Solution2:
    def kadane_ish(self, s: List[str], major: str, minor: str) -> int:
        # Kadane aux to find the max sum of subarray
        # However, it is not the vanilla Kadane, because we require that
        # the subarray to contain at least one 1 and one -1. Thus, an
        # example of [1, 1, -1, -1] shall return 1, instead of 2. To
        # solve this, we need to know which subarray produces the max
        # sum. If the subarray length is the same as the max
        # sum, that means we have not included any of the opposite value.
        # Thus, the real value has to be that max or min reducing one.
        kmax = -math.inf
        kmax_idx = 0
        cmax = 0
        max_start = []
        aux = []
        for i, le in enumerate(s):
            if le == major:
                aux.append(1)
            elif le == minor:
                aux.append(-1)
        for i, v in enumerate(aux):
            # find max
            if cmax + v >= v:
                cmax = cmax + v
                if max_start:
                    max_start.append(max_start[-1])
                else:
                    max_start.append(i)
            else:
                cmax = v
                max_start.append(i)
            if cmax > kmax or (cmax == kmax and i - max_start[i] + 1 > cmax):
                kmax = cmax
                kmax_idx = i
        # kmax need to be adjusted if there is no opposite
        # value in the max or min subarray sum
        if kmax_idx - max_start[kmax_idx] + 1 == kmax:
            kmax -= 1
        return kmax

    def largestVariance(self, s: str) -> int:
        """Same as solution1, but only do max subarray sum. For each pair of
        letters, we swap the order of major and minor
        """
        uniqs = list(set(s))
        res = 0
        for i in range(len(uniqs)):
            for j in range(i + 1, len(uniqs)):
                res = max(
                    res,
                    self.kadane_ish(s, uniqs[i], uniqs[j]),
                    self.kadane_ish(s, uniqs[j], uniqs[i]),
                )
        return res


class Solution3:
    def kadane_ish(self, s: List[str], major: str, minor: str) -> int:
        # This one uses Kadane as well, but only update kmax when the current
        # subarray contains at least one minor. Thus, we need a flag to keep
        # track of whether a minor has been incorporated in the subarray.
        # We reset the flag when the subarray gets reset.
        kmax = -math.inf
        cmax = 0
        has_minor = False
        for i, le in enumerate(s):
            if le != major and le != minor:
                continue
            v = 1 if le == major else -1
            # find max
            if cmax + v >= v:
                if v < 0:
                    has_minor = True
                cmax = cmax + v
            else:
                cmax = v
                has_minor = False
            # notice that kmax is updated differently if there has not been a
            # minor in the subarray
            kmax = max(kmax, cmax if has_minor else cmax - 1)
        return kmax

    def largestVariance(self, s: str) -> int:
        """Same as solution1, but only do max subarray sum. For each pair of
        letters, we swap the order of major and minor

        3760 ms, faster than 60.68% 
        """
        uniqs = list(set(s))
        res = 0
        for i in range(len(uniqs)):
            for j in range(i + 1, len(uniqs)):
                res = max(
                    res,
                    self.kadane_ish(s, uniqs[i], uniqs[j]),
                    self.kadane_ish(s, uniqs[j], uniqs[i]),
                )
        return res


sol = Solution3()
tests = [
    ('aababbb', 3),
    ('abcde', 0),
    ("aaaaa", 0),
    ("abbbcacbcdce", 3),
    ("lripaa", 1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.largestVariance(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
