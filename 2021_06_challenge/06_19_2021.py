# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """LeetCode 629

        This is a typical DP problem. The intuition is that if we have the
        total number of arrays for n - 1 with k ranging from 1 to k, then to
        compute n, we can do this:

        Put n in the last position, then we need the remaining n - 1 numbers to
        produce k pairs. So we have the answer f(n - 1, k)

        Put n in the second to the last position, we need the remaining n - 1
        numbers to produce k - 1 pairs, because we will always have one pair
        between n and whatever number that is placed in the last position. So
        we have answer f(n - 1, k - 1)

        We repeat this process until n is at min(n, k)th to the last position, then we
        need the remaining n - 1 numbers to produce 0 pairs. Thus we have
        f(n - 1, k - min(n, k))

        Therefore f(n, k) = f(n - 1, k) + f(n - 1, k - 1) + ... + f(n - 1, k - min(n, k))

        This can be solved using two arrays, one recording the k values for
        n - 1 (we can call it pre), and the other recording the k values for n
        (we can call it cur), computed from pre.

        We can also observe that the values in pre is symmetrical. Also, once
        we hit 0 value, the rest of the elements in the array will remain 0.

        O(KN), 460 ms, 67% ranking. Space complexity O(K)
        """
        pre = [0] * (k + 1)
        pre[0] = 1  # when k == 0, there is always only one valid array
        for i in range(2, n + 1):
            cur = [0] * (k + 1)
            cur[0] = 1
            for j in range(1, k + 1):
                cur[j] = cur[j - 1] + pre[j] - (pre[j - i] if j >= i else 0)
                if cur[j] == 0:
                    break
            pre = cur
        return pre[k] % 1000000007


sol = Solution()
tests = [
    (1, 0, 1),
    (3, 0, 1),
    (3, 1, 2),
    (4, 4, 5),
    (3, 3, 1),
    (4, 6, 1),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.kInversePairs(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
