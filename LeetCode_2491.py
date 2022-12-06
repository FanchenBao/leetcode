# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def dividePlayers(self, skill: List[int]) -> int:
        """O(NlogN), 1323 ms, faster than 15.38%
        """
        skill.sort()
        res = skill[0] * skill[-1]
        total_skill = skill[0] + skill[-1]
        i, j = 1, len(skill) - 2
        while i < j:
            if skill[i] + skill[j] != total_skill:
                return -1
            res += skill[i] * skill[j]
            i += 1
            j -= 1
        return res


class Solution2:
    def dividePlayers(self, skill: List[int]) -> int:
        """O(N)

        1607 ms, faster than 7.69%
        """
        c = Counter(skill)
        total_skill = sum(skill) // (len(skill) // 2)
        res = 0
        for s in skill:
            if c[s]:
                if not c[total_skill - s]:
                    return -1
                res += s * (total_skill - s)
                c[s] -= 1
                c[total_skill - s] -= 1
        return res


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
