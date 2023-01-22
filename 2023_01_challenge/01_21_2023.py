# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import combinations


class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """LeetCode 93

        Backtracking. But I made a mistake that wasted me a long time. I forgot
        to turn the string into number before maing comparison to 255.

        38 ms, faster than 77.95%
        """
        res = []
        N = len(s)

        def dfs(idx: int, rem: int, ip: List[str]) -> None:
            if idx >= N and rem > 0:
                return
            if rem == 0:
                if idx != N:
                    return
                res.append('.'.join(ip))
            elif s[idx] == '0':
                ip.append('0')
                dfs(idx + 1, rem - 1, ip)
                ip.pop()
            else:
                for i in range(3):
                    pot = s[idx:idx + i + 1]
                    if int(pot) <= 255:
                        ip.append(pot)
                        dfs(idx + i + 1, rem - 1, ip)
                        ip.pop()

        dfs(0, 4, [])
        return res


class Solution2:
    def is_valid(self, s: str) -> bool:
        if len(s) > 3:
            return False
        if s[0] == '0' and len(s) > 1:
            return False
        return int(s) <= 255

    def restoreIpAddresses(self, s: str) -> List[str]:
        """Use combinations to get all possible partitions.

        38 ms, faster than 77.95% 
        """
        N = len(s)
        res = []
        for comb in combinations(range(N - 1), 3):
            ip, pre = [], 0
            for i in sorted(comb) + [N]:
                ip.append(s[pre:i + 1])
                if not self.is_valid(ip[-1]):
                    break
                pre = i + 1
            else:
                res.append('.'.join(ip))
        return res


sol = Solution2()
tests = [
    ("25525511135", ["255.255.11.135","255.255.111.35"]),
    ("0000", ["0.0.0.0"]),
    ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),
    ("1234567", ["1.23.45.67","1.234.5.67","1.234.56.7","12.3.45.67","12.34.5.67","12.34.56.7","123.4.5.67","123.4.56.7","123.45.6.7"]),
    ("0909080", ["0.90.90.80"])
]

for i, (s, ans) in enumerate(tests):
    res = sol.restoreIpAddresses(s)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
