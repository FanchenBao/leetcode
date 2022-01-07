# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """Build a graph of all the valid mutations in bank. Then BFS to find
        the shortest path from start to end, if end is in bank.

        O(N), 40 ms, 20% ranking.
        """
        adj = [[] for _ in bank]
        tgt = -1
        N = len(bank)
        for i in range(N):
            if bank[i] == end:
                tgt = i
            for j in range(i + 1, N):
                if sum(a1 != a2 for a1, a2 in zip(bank[i], bank[j])) == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        if tgt < 0:
            return -1
        queue = [i for i, g in enumerate(bank) if sum(a1 != a2 for a1, a2 in zip(start, g)) == 1]
        if not queue:
            return -1
        steps = 1
        visited = set()
        while queue:
            temp = []
            for idx in queue:
                if idx == tgt:
                    return steps
                if idx not in visited:
                    visited.add(idx)
                    temp.extend(adj[idx])
            queue = temp
            steps += 1
        return -1



class Solution2:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """This is a better way to find links between the genes. Instead of
        pre-computing all the links, we find links on-the-go by actually making
        SNPs. Since making SNPs for each gene is O(8), we save on the time
        that would've been needed to prepare the graph before hand, especially
        if bank is huge.

        28 ms, 83% ranking.

        UPDATE: we don't need a visited set, because we can simply remove a
        gene from the bank to indicate that it has been visited.
        """
        queue = [start]
        steps = 0
        bank_set = set(bank)
        while queue:
            temp = []
            for g in queue:
                if g == end:
                    return steps
                for i in range(len(g)):
                    for mut in 'ATCG':
                        ng = g[:i] + mut + g[i + 1:]
                        if ng in bank_set:
                            temp.append(ng)
                            bank_set.remove(ng)
            queue = temp
            steps += 1
        return -1


sol = Solution2()
tests = [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2),
    ("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"], 3),
]

for i, (start, end, bank, ans) in enumerate(tests):
    res = sol.minMutation(start, end, bank)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
