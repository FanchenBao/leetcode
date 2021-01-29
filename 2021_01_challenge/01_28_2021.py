# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def getSmallestString(self, n: int, k: int) -> str:
        """First attempt. Very straightforward method. We initialize all letters
        to 'a', and remove from the back one at a time to decide whether we can
        fit a 'z'. We continue this process until we find a non-z letter that
        fits in place. And we are done.

        O(N), 1260 ms, 15% ranking.
        """
        res_lst = [1] * n
        cur_sum, i = n, n - 1
        while i >= 0 and cur_sum < k:
            if k - (cur_sum - 1) <= 26:
                res_lst[i] = k - (cur_sum - 1)
                break
            else:
                res_lst[i] = 26
                i -= 1
                cur_sum = cur_sum - 1 + 26
        return ''.join(chr(ord('a') + r - 1) for r in res_lst)


class Solution2:
    def getSmallestString(self, n: int, k: int) -> str:
        """Same concept as above, but without the need to handle any lists. This
        speeds things up.

        O(N), 796 ms, 41% ranking.
        """
        num_a, num_z, mid_v = n, 0, 0
        while num_a * 1 + mid_v + 26 * num_z < k:
            remain = k - (num_a * 1 + mid_v + 26 * num_z - 1)
            if remain <= 26:
                mid_v = remain
            else:
                num_z += 1
            num_a -= 1
        return 'a' * num_a + chr(ord('a') + mid_v - 1) + 'z' * num_z


class Solution3:
    def getSmallestString(self, n: int, k: int) -> str:
        """Ultimate solution: MATH!

        A bit of trial and error on this. There are two scenarios. First, the
        string is composed of ONLY 'a' and 'z'.

        num_a + num_z = n
        num_a + num_z * 25 = k

        We get num_z = (k - n) // 25 iff (k - n) divides 25.

        Second, the string is compared of 'a', some other letter, and 'z'.

        num_a + num_z + 1 = n
        num_a + num_z * 25 + mid_v = k

        We get mid_v = k - n + 1 - 25 * num_z. Beacuse 1 <= v <= 25, we can get
        mid_v and num_z using divmod(), in which mid_v is the mod and num_z is
        the div. Special case is when mid_v == 0, in which case we have to
        decrement num_z and make mid_v = 25.

        Then we are done.

        O(1), 52 ms, 80% ranking.
        """
        if (k - n) % 25 == 0:
            num_z = (k - n) // 25
            num_a = n - num_z
            return 'a' * num_a + 'z' * num_z
        num_z, mid_v = divmod(k - n + 1, 25)
        if mid_v == 0:
            num_z -= 1
            mid_v = 25
        num_a = n - 1 - num_z
        return 'a' * num_a + chr(ord('a') + mid_v - 1) + 'z' * num_z


class Solution4:
    def getSmallestString(self, n: int, k: int) -> str:
        """Better math. Refer here:

        https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/944594/JavaPython-3-O(n)-and-O(1)-codes-w-brief-explanation-and-analysis.

        The idea is that after filling all positions with 'a', we will have
        k - n remains to fill. Each time we swap an 'a' with a 'z', we put in
        26 - 1 = 25. So we need to use num_z number of 25 to fit k - n. The
        quotient is the number of 'z' and the remainder is the mid value. Here
        the mid value is allowed to be 0, because that just mean the mid value
        is 'a'.

        O(1), 36 ms, 91% ranking.
        """
        num_z, mid_v = divmod(k - n, 25)
        if num_z == n:
            return 'z' * n
        return 'a' * (n - 1 - num_z) + chr(ord('a') + mid_v) + 'z' * num_z


sol = Solution4()
tests = [
    (3, 27, 'aay'),
    (5, 73, 'aaszz'),
    (1, 19, 's'),
    (5, 130, 'zzzzz'),
    (85, 2159, 'aayzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.getSmallestString(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
