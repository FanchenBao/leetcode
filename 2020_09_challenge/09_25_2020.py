# from pudb import set_trace; set_trace()
from typing import List
from functools import cmp_to_key


class TrieNode:
    def __init__(self):
        self.next = [None] * 10
        self.val = ''


class Solution1:
    def make_trie(self, node: TrieNode, n: int) -> None:
        nstr = str(n)
        for strd in nstr:  # pretty standard Trie construction
            intd = int(strd)
            if node.next[intd] is None:
                node.next[intd] = TrieNode()
            node = node.next[intd]
        node.val += nstr  # this is a tricky part, to handle repeated numbers

    def arange(self, node: TrieNode) -> str:
        if not any(node.next) and node.val:
            return node.val
        res = ''
        for i in range(9, -1, -1):  # go from highest digit down
            if node.next[i] is not None:
                partial = self.arange(node.next[i])
                if node.val and node.val + partial > partial + node.val:
                    # this is a tricky part. If the node currently has a value
                    # attached, and there are more numbers extending from the
                    # current val, for each child value, we need to compare
                    # the outcome of different order: whether to use the node
                    # value before the child, or let child come out first.
                    # e.g. [8247, 824] => let 824 come out first because
                    # 8247824 < 8248247
                    # e.g. [128, 12] => let child come out first because
                    # 12812 > 12128
                    # e.g. [121, 12] => let 12 come out first because
                    # 12112 < 12121
                    res += node.val + partial
                    node.val = ''  # node.val can only be used once
                else:
                    res += partial
        return res + node.val

    def largestNumber(self, nums: List[int]) -> str:
        """Trial and error debugging. Not what I wanted, but it did pass OJ,
        with 85 % ranking
        """
        root = TrieNode()
        for n in nums:
            self.make_trie(root, n)
        res = self.arange(root)
        return res if res[0] != '0' else '0'  # edge case [0, 0] => '0' not '00'


class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        """Standard sorting solution"""

        def comp(x: str, y: str) -> int:
            """This is the key to sort.

            We want to decide how to sort two numbers if they have the same
            prefix. The way is to concatenate them and compare. We sort x ahead
            of y if x concat y is larger than y concat x.
            """
            return 1 if x + y < y + x else -1 if x + y > y + x else 0

        res = ''.join(sorted([str(n) for n in nums], key=cmp_to_key(comp)))
        return res if res[0] != '0' else '0'


sol = Solution2()
tests = [
    ([10, 2], '210'),
    ([3, 30, 34, 5, 9], "9534330"),
    ([3, 33, 31, 32, 34, 35], "35343333231"),
    ([23, 543, 765, 12, 56, 89, 908, 564, 32, 543, 675, 786, 897, 342, 32], "908898977867656755656454354334232322312"),
    ([0, 0], '0'),
    ([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247], "9609938824824769735703560743981399"),
    ([121, 12], '12121'),
    ([128, 12], '12812'),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.largestNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
