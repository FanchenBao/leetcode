# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, deque


class Solution1:
    def partitionLabels(self, S: str) -> List[int]:
        """Pass OJ, with 76 ms runtime"""
        part_ranges = []
        for i, le in enumerate(S):
            for j, [s, e] in enumerate(part_ranges):
                if le in S[s:e]:
                    part_ranges[j][1] = i + 1
                    part_ranges = part_ranges[:j + 1]
                    break
            else:
                part_ranges.append([i, i + 1])
        # print(part_ranges)
        return [e - s for s, e in part_ranges]


class Solution2:
    def partitionLabels(self, S: str) -> List[int]:
        """Faster than Solution1 at 44 ms runtime."""
        occurrences = defaultdict(list)
        for i, le in enumerate(S):
            occurrences[le].append(i)
        partitions = deque()
        for pos in occurrences.values():
            s, e = pos[0], pos[-1]
            for _ in range(len(partitions)):
                ps, pe = partitions.popleft()
                if (ps < s and pe > s) or (s < ps and e > ps):  # overlap
                    partitions.append((min(s, ps), max(e, pe)))
                    break
                else:
                    partitions.append((ps, pe))
            else:
                partitions.append((s, e))
        return [e - s + 1 for s, e in partitions]


class Solution3:
    def partitionLabels(self, S: str) -> List[int]:
        """Find ranges (first and last occurrence of a letter) then merge"""
        ranges = {}
        for i, le in enumerate(S):
            ranges[le] = ranges.get(le, [i, i])
            ranges[le][1] = i
        partitions = []
        for s, e in sorted(ranges.values(), key=lambda x: x[0]):
            if partitions:
                ps, pe = partitions[-1]
                if pe > s:  # overlap
                    partitions[-1][1] = max(e, pe)
                else:
                    partitions.append([s, e])
            else:
                partitions.append([s, e])
        return [e - s + 1 for s, e in partitions]


sol = Solution3()
tests = [
    ('ababcbacadefegdehijhklij', [9, 7, 8]),
]

for i, (s, ans) in enumerate(tests):
    res = sol.partitionLabels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
