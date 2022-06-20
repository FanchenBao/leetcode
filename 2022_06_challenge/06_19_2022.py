# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """LeetCode 1268

        This is pretty standard problem using Trie as the data structure. We
        just need to record the list of words that appear in each trie node.
        And during search, we return the first three elements in the list of
        words for each matched trie node.

        O(MN), where M is the average length of word in products and N is the
        length of products. 262 ms, faster than 53.97%
        """
        trie = lambda: defaultdict(trie)
        products.sort()
        root = trie()
        for word in products:
            node = root
            for le in word:
                node = node[le]
                if '#' not in node:
                    node['#'] = []
                node['#'].append(word)
        res = []
        node = root
        for le in searchWord:
            if le in node:
                node = node[le]
                res.append(node['#'][:3])
            else:
                break
        res += [[] for _ in range(len(searchWord) - len(res))]
        return res


class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Binary search, using bisect and its key kwarg

        The ingenious part is that prefix can be compared between a word in
        products and the searchWord.

        O(NlogN + MlogN), where N = len(products) and M = len(searchWord)
        137 ms, faster than 72.44%
        """
        products.sort()
        N = len(products)
        res = []
        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]
            idx = bisect_left(products, prefix, key=lambda v: v[:i + 1])
            res.append([products[j] for j in range(idx, min(idx + 3, N)) if products[j].startswith(prefix)])
        return res
        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
