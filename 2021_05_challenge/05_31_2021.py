# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.matches = []


class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """LeetCode 1268

        First build a trie. We also need to keep track of each product that
        hits a trie node. If we go through the products in ascending order, then
        the product list in each trie node will also follow ascending order.

        Then we loop through each letter in searchWord, and record the
        associated products at each trie node. The tricky part that got me is
        that once the trie node is exhausted, we should immediately add empty
        lists to the result.

        O(NM + L), where N is the length of products, M the average length of
        product, and L is the length of searchWord.

        296 ms, 44% ranking.
        """
        trie = TrieNode()
        for prod in sorted(products):
            node = trie
            for le in prod:
                if le not in node.children:
                    node.children[le] = TrieNode()
                node = node.children[le]
                node.matches.append(prod)

        res = []
        node = trie
        for i, le in enumerate(searchWord):
            if le in node.children:
                node = node.children[le]
                res.append(node.matches[:3])
            else:
                res.extend([[] for _ in range(len(searchWord) - i)])
                break
        return res


class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """The trie solution from the official solution. Instead of saving all
        the match words at each trie node, we recreate each word by DFS the trie
        and record the letters encountered.
        """
        trie = lambda: defaultdict(trie)
        root = trie()
        for prod in sorted(products):
            node = root
            for le in prod:
                node = node[le]
            node['end']  # sentinel

        res = []

        def dfs(node, match: str, matches: List[str]) -> bool:
            if 'end' in node:
                matches.append(match)
            for le, next_node in node.items():
                if len(matches) == 3:
                    return
                new_match = match + le
                dfs(next_node, new_match, matches)

        node = root
        for i, le in enumerate(searchWord):
            if le not in node:
                res.extend([[] for _ in range(len(searchWord) - i)])
                break
            matches = []
            dfs(node[le], searchWord[:i + 1], matches)
            res.append(matches)
            node = node[le]
        return res


class Solution3:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Binary search

        O(nlog(n) + mlog(n)) where n is the length of products, and m is the
        length of searchWord. 136 ms, 65% ranking.
        """
        products.sort()
        res, i = [], 0
        for p in range(len(searchWord)):
            prefix = searchWord[:p + 1]
            # Note that we do not reinitialize i for each binary search, becasue
            # as the prefix grows, the next match position must be after the
            # previous position.
            j = len(products) - 1
            while i < j:
                mid = (i + j) // 2
                if products[mid][:p + 1] >= prefix:
                    j = mid
                else:
                    i = mid + 1
            res.append(
                [prod for prod in products[i:i + 3] if prod.startswith(prefix)]
            )
        return res


sol = Solution3()
tests = [
    (['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse', [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]),
    (['havana'], 'havana', [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]),
    (['bags', 'baggage', 'banner', 'box', 'cloths'], 'bags', [['baggage', 'bags', 'banner'], ['baggage', 'bags', 'banner'], ['baggage', 'bags'], ['bags']]),
    (['havana'], 'tatiana', [[], [], [], [], [], [], []]),
]

for i, (products, searchWord, ans) in enumerate(tests):
    res = sol.suggestedProducts(products, searchWord)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
