# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """LeetCode 899

        I didn't solve it. Had to check the solution. I was half way there but
        fell short. I was able to figure that when k >= n / 2, we simply sort
        the string. But the real solution is that when k >= 2, we can sort the
        string. Using k = 2 as an example (k > 2 can be solved by k = 2
        condition), we can always move the ith and i + 1th smallest values to
        the front two positions. We then move the ith smallest to the end. Next,
        we look for the i + 2th smallest value to the second position. Once that
        is done, we move the i + 1th smallest to the end. We keep doing this,
        the string goes in round and round, and each round, one more sorted
        value is added to the remaining n - 1 string, and one more unsorted is
        picked out from the remaining n - 1 string. When the last unsorted value
        is picked out, we have sorted the string. Therefore, when k >= 2, we
        simply sort the string.

        Ref: https://leetcode.com/problems/orderly-queue/solution/

        Thinking from another perspective, with the ability to swap the first
        two elements, what we have is the same plaftform as bubble sort.

        O(N^2) for k == 1 and O(NlogN) for k >= 2. Thus overall O(N^2).
        """
        if k == 1:
            res = s
            for i in range(1, len(s)):
                res = min(res, s[i:] + s[:i])
            return res
        return ''.join(sorted(s))


sol = Solution()
tests = [
    ('cba', 1, 'acb'),
    ('baaca', 3, 'aaabc'),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.orderlyQueue(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
