# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """LeetCode 421

        This question is not easy. Last time I did it, I spent more than 3
        hours on it. This time, I got lucky and the first method I tried worked

        I create a Trie for all the numbers in nums using their binary format.
        The max XOR is achieved if at each binary position, one number has 0
        and the other has 1. Thus, we need two nodes on the Trie representing
        the split of 0 and 1 from the previous position. Now at the current
        position, each branch can further split into 0 and 1. We shall match
        the left branch's 0 with the right branch's 1, and the left branch's 1
        with the right branch's 0. These two matches must both take place,
        unless the situation is impossible. If one of the two scenarios above
        is satisifed, as are done with these two nodes. However, if none of
        them is realized, we need to settle for a 0-0 match or 1-1 match, which
        ever is possible.

        O(N), 1436 ms, 69% ranking.
        """
        trie = lambda: defaultdict(trie)
        root = trie()
        for n in nums:  # O(N)
            node = root
            for d in f'{n:031b}':
                node = node[d]
            node['#'] = n
        self.res = 0

        def dfs(node1, node2) -> None:
            if '#' in node1:  # must also be in node2
                self.res = max(self.res, node1['#'] ^ node2['#'])
                return
            has_optimal = False
            if '1' in node1 and '0' in node2:
                dfs(node1['1'], node2['0'])
                has_optimal = True
            if '0' in node1 and '1' in node2:
                dfs(node1['0'], node2['1'])
                has_optimal = True
            if not has_optimal:
                if '0' in node1 and '0' in node2:
                    dfs(node1['0'], node2['0'])
                else:
                    dfs(node1['1'], node2['1'])

        dfs(root, root)  # at most O(32)
        return self.res


class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """Prefix solution, learned from my last attempt at this problem back
        in 2020-09-16.

        O(N), 2300 ms.
        """
        res = mask = 0
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefixes = set(n & mask for n in nums)
            pot_res = res | (1 << i)
            if any((pot_res ^ p) in prefixes for p in prefixes):
                res = pot_res
        return res



sol = Solution2()
tests = [
    ([3,10,5,25,2,8], 28),
    ([14,70,53,83,49,91,36,80,92,51,66,70], 127),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findMaximumXOR(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
