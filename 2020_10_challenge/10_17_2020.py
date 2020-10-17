# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """58% ranking"""
        seq_set = set()
        res = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in seq_set:
                res.add(s[i:i + 10])
            else:
                seq_set.add(s[i:i + 10])
        return list(res)


class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """58% ranking"""
        seq_count = defaultdict(int)
        for i in range(len(s) - 9):
            seq_count[s[i:i + 10]] += 1
        return [k for k, v in seq_count.items() if v > 1]


sol = Solution2()
tests = [
    ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
    ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ("AAAAAAAAAAA", ["AAAAAAAAAA"]),
]

for i, (s, ans) in enumerate(tests):
    res = sol.findRepeatedDnaSequences(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
