# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """92% ranking. This is an easy one"""
        set_a, set_b = set(A), set(B)
        if set_a != set_b or len(A) != len(B):  # some letters do not match
            return False
        if A == B:  # can swap if there are repeated letters
            return len(A) > len(set_a)
        # Swap is only possible if there are exactly two mismatches
        # and the mismatches can swap.
        mismatches = []
        for a, b in zip(A, B):
            if a != b:
                mismatches.append((a, b))
        return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]


sol = Solution()
tests = [
    ('ab', 'ba', True),
    ('ab', 'ab', False),
    ('aa', 'aa', True),
    ('aaaaaaabc', 'aaaaaaacb', True),
    ('', 'aa', False)
]

for i, (A, B, ans) in enumerate(tests):
    res = sol.buddyStrings(A, B)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
