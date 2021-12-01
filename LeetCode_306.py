# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def isAdditiveNumber(self, num: str) -> bool:
        """LeetCode 306

        This one is not particularly difficult, but it does have its tricky
        portion. The general idea is DFS. The tricky part is
        to handle the case where any number with leading zero is not allowed,
        but the number zero itself is allowed. This means '00000' is valid, but
        '00112' is not.

        O(N^3)
        """
        N = len(num)

        @lru_cache(maxsize=None)
        def dfs(pre: int, idx: int) -> bool:
            for j in range(idx, N):
                if j > idx and num[idx] == '0':
                    return False
                cur = int(num[idx:j + 1])
                pot_str = str(pre + cur)
                rem_str = num[j + 1:]
                if len(pot_str) > len(rem_str):
                    break
                if (pot_str == rem_str) or (rem_str.startswith(pot_str) and dfs(cur, j + 1)):
                    return True
            return False

        for i in range(N):
            if i > 0 and num[0] == '0':
                break
            if dfs(int(num[:i + 1]), i + 1):
                return True
        return False


class Solution2:
    def isAdditiveNumber(self, num: str) -> bool:
        """Easier recursion.

        Find all possible pairs of the first two numbers, and run the check for
        the remaining.

        Ref: https://leetcode.com/problems/additive-number/discuss/75567/Java-Recursive-and-Iterative-Solutions

        24 ms, 98% ranking.
        """
        N = len(num)

        def is_valid(pre: int, cur: int, idx: int) -> bool:
            if idx == N:
                return True
            if num[idx:].startswith(str(cur)):
                if is_valid(cur, pre + cur, idx + len(str(cur))):
                    return True
            return False

        for i in range(N // 2):
            if i > 0 and num[0] == '0':
                break
            for j in range(i + 1, N - 1):
                if j > i + 1 and num[i + 1] == '0':
                    break
                pre, cur = int(num[:i + 1]), int(num[i + 1:j + 1])
                if is_valid(cur, pre + cur, j + 1):
                    return True
        return False



sol = Solution2()
tests = [
    ('112358', True),
    ('199100199', True),
    ('1234654356', False),
    ('1023', False),
    ('00112', False),
    ('10101', False),
    ('00000', True),
]

for i, (num, ans) in enumerate(tests):
    res = sol.isAdditiveNumber(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
