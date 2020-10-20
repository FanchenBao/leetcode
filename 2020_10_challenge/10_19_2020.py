# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """92% ranking.
        
        The core idea is to find the most common element in A and B. Only when
        the most common element appears more than half the times in each list
        can the element have the possibility of being chosen as the letter for
        swap. We only need to check whether the most common letter because if
        a less common letter is eventually chosen, it must appear in the other
        list. Thus, by checking the most common in both lists, we cover all
        situations.
        """
        counter_a, counter_b = Counter(A), Counter(B)
        target_a, count_a = counter_a.most_common(1)[0]
        target_b, count_b = counter_b.most_common(1)[0]
        res_a, res_b = 0, 0
        if count_a >= len(A) // 2:  # use >= to cover edge case
            if count_a + counter_b[target_a] < len(A):  # quick check edge case
                res_a = -1
            else:
                for i, a in enumerate(A):
                    if a != target_a:
                        if B[i] == target_a:
                            res_a += 1
                        else:
                            res_a = -1
                            break
        else:
            res_a = -1
        if count_b > len(B) // 2:
            if count_b + counter_b[target_b] < len(B):
                res_b = -1
            else:
                for i, b in enumerate(B):
                    if b != target_b:
                        if A[i] == target_b:
                            res_b += 1
                        else:
                            res_b = -1
                            break
        else:
            res_b = -1
        if res_a >= 0 and res_b >= 0:
            return min(res_a, res_b)
        return res_a if res_a >= 0 else res_b if res_b >= 0 else -1


class Solution2:

    def count_swaps(self, base_lst: List[int], swap_lst: List[int], target: int) -> int:
        res = 0
        for i, val in enumerate(base_lst):
            if val != target:
                if swap_lst[i] == target:
                    res += 1
                else:
                    res = -1
                    break
        return res

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """Even easier. This solution works because eventually, either A
        or B has to have the same number throughout. So we can just check the
        possibility of using first number of each list.
        """
        res_aa = self.count_swaps(A, B, A[0])
        res_ab = self.count_swaps(A, B, B[0])
        if res_aa >= 0 and res_ab >= 0:
            res_a = min(res_aa, res_ab)
        res_a = res_aa if res_aa >= 0 else res_ab if res_ab >= 0 else -1

        res_ba = self.count_swaps(B, A, A[0])
        res_bb = self.count_swaps(B, A, B[0])
        if res_ba >= 0 and res_bb >= 0:
            res_b = min(res_ba, res_bb)
        res_b = res_ba if res_ba >= 0 else res_bb if res_bb >= 0 else -1

        if res_a >= 0 and res_b >= 0:
            return min(res_a, res_b)
        return res_a if res_a >= 0 else res_b if res_b >= 0 else -1


sol = Solution2()
tests = [
    ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
    ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1),
    ([1, 2, 1, 1, 1, 2, 2, 2], [2, 1, 2, 2, 2, 2, 2, 2], 1),
    ([1, 1, 0, 0], [2, 2, 1, 1], 2),
]

for i, (A, B, ans) in enumerate(tests):
    res = sol.minDominoRotations(A, B)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
