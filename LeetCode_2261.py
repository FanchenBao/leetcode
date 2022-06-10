# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """1. Find all the sign posts. A sign post is an index pointing to an
        element divisible by p.

        2. Iterate through all the islands in between the sign posts. Each
        island contains only elements NOT divisible by p. Thus, all combinations
        of subarray there can be included.

        3. We build up a library of all the subarrays ending on the right
        boundary of  each island, and all the subarrays starting on the left
        boundary. We will use this library to build other subarrays.

        4. We go from kk = 1, 2, 3, ..., k. For each kk value, we iterate
        through all subarrays of sign points of size kk. And then we create a
        full combination of subarrays on the right edge and left edge that just
        surrounds the current subarray of kk number of sign posts. Then we
        add the edges to the subarray of sign posts. And we are done.

        1199 ms, faster than 37.87%
        """
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
                base = tuple(nums[lo:hi + 1])
                for re in r_edge[lo - 1]:  # add right edges
                    for le in l_edge[hi + 1]:  # add left edges
                        res_set.add(re + base + le)
        return len(res_set)


class Solution2:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """Rabin-Karp rolling hash to achieve O(N^2)

        Two tricks here. First, according to this article:
        https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/

        A typical prime number used for rolling hash is quite big, such as
        11111.

        Second, computing 11111 to a large power is time consuming. And since
        we will encounter 11111 raised to the same power multiple times, we 
        can use a DP table to compute the power only once.

        These two tricks combined allow us to reach a performance of

        464 ms, faster than 90.56%
        """
        powers = [0] * 200
        N = len(nums)
        res_set = set()
        MOD = 10**9 + 7
        for i in range(N):
            cnt = ha = 0
            for j in range(i, N):
                cnt += nums[j] % p == 0
                if cnt > k:
                    break
                if not powers[j - i]:
                    powers[j - i] = 11111**(j - i) % MOD
                ha += (nums[j] * powers[j - i]) % MOD  # hash function
                res_set.add(ha)
        return len(res_set)


class Solution3:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """Use Trie to mark unique subarrays. Honestly, this is not bad at all.
        In fact, I would prefer this solution to rolling hash, because this is
        always deterministic, whereas rolling hash always has a risk of
        collision.

        O(N^2), 579 ms, faster than 83.53%
        """
        trie = lambda: defaultdict(trie)
        res = 0
        root = trie()
        root['c'] = 0
        for i in range(len(nums)):
            node = root
            for j in range(i, len(nums)):
                if node['c'] > k:
                    break
                if nums[j] in node:
                    node = node[nums[j]]
                else:
                    cur_cnt = node['c']
                    node = node[nums[j]]
                    node['c'] = cur_cnt + int(nums[j] % p == 0)
                    if node['c'] <= k:
                        res += 1
        return res


sol = Solution3()
tests = [
    ([2,3,3,2,2], 2, 2, 11),
    ([1,2,3,4], 4, 1, 10),
    ([19,20,3,7,5,7,18], 5, 2, 27),
    ([13,4,14,13,15,4,8,13,4,12], 5, 14, 50),
    ([8,14,5,14,11,19,6,12,6], 9, 17, 43),
    ([95,182,183,115,5,183,164,51,37,138,150,69,95,191,84,96,90,57,146,111,87,95,23,59,168,150,45,16,172,196,87,78,86,77,125,6,102,85,21,172,5,75,170,113,174,189,163,21,123,74], 47, 74, 1267),
    ([173,21,127,154,93,44,130,102,186,200,197,29,85,13,16,179,34,156,128,60,2,1,11,116,174,52,185,154,127,155,24,59,103], 15, 113, 559),
]

for i, (nums, k, p, ans) in enumerate(tests):
    res = sol.countDistinct(nums, k, p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
