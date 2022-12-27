# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        """We can just split each report and check the words one by one, because
        the total length of the string in report is only 100. Thus, splitting it
        at most gives us 50 elements, which is not that much.

        O(NM), 400 ms, faster than 66.67%
        """

        pf = set(positive_feedback)
        nf = set(negative_feedback)
        l = []
        for r, i in zip(report, student_id):
            words = r.split(' ')
            pos = sum(int(word in pf) for word in words)
            neg = sum(int(word in nf) for word in words)
            l.append((neg - 3 * pos, i))  # use negative score to facilitate sort
        return [i for _, i in sorted(l)[:k]]


# sol = Solution()
# tests = [
    
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
