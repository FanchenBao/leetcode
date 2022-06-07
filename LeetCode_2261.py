# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        signposts = [-1] + [i for i, n in enumerate(nums) if n % p == 0] + [len(nums)]
        res_set = set()
        l_edge = defaultdict(lambda: [()])
        r_edge = defaultdict(lambda: [()])
        for i in range(len(signposts) - 1):
            l, r = signposts[i] + 1, signposts[i + 1] - 1
            if l > r:
                continue
            for j in range(l, r + 1):
                for h in range(j, r + 1):
                    tmp = tuple(nums[j:h + 1])
                    if j == l:
                        l_edge[l].append(tmp)
                    if h == r:
                        r_edge[r].append(tmp)
                    res_set.add(tmp)
        for kk in range(1, k + 1):
            for i in range(1, len(signposts) - kk):
                lo, hi = signposts[i], signposts[i + kk - 1]
                # print(kk, lo, hi)
                # print(r_edge[lo - 1])
                # print(l_edge[hi + 1])
                base = tuple(nums[lo:hi + 1])
                for re in r_edge[lo - 1]:  # add right edges
                    for le in l_edge[hi + 1]:  # add left edges
                        res_set.add(re + base + le)
        # print(sorted(res_set))
        return len(res_set)


sol = Solution()
tests = [
    ([2,3,3,2,2], 2, 2, 11),
    ([1,2,3,4], 4, 1, 10),
    ([19,20,3,7,5,7,18], 5, 2, 27),
]

for i, (nums, k, p, ans) in enumerate(tests):
    res = sol.countDistinct(nums, k, p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
