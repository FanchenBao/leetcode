# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class WordFilter:

    def __init__(self, words: List[str]):
        """LeetCode 745

        The solution is quite straightforward: two tries, one handling prefix
        and the other suffix. While this is not a difficult concept to start
        with, the implementation could be tricky, because the input can be so
        big that it triggers TLE. The trick here is not to process each word,
        because the words can have duplicate. Since we only return the max idx,
        we can de-duplicate the input words and record the largest index for
        each word.

        839 ms, faster than 97.55%
        """
        self.trie = lambda: defaultdict(self.trie)
        self.ltor_root = self.trie()
        self.rtol_root = self.trie()
        self.build_trie(words)

    def build_trie(self, words):
        max_indices = {}
        for i, word in enumerate(words):
            max_indices[word] = i
        for word, idx in max_indices.items():
            ltor_node = self.ltor_root
            rtol_node = self.rtol_root
            for le in word:
                ltor_node = ltor_node[le]
                if '#' not in ltor_node:
                    ltor_node['#'] = set()
                ltor_node['#'].add(idx)
            for le in word[::-1]:
                rtol_node = rtol_node[le]
                if '#' not in rtol_node:
                    rtol_node['#'] = set()
                rtol_node['#'].add(idx)

    def f(self, prefix: str, suffix: str) -> int:
        ltor_node = self.ltor_root
        rtol_node = self.rtol_root
        lmatch, rmatch = set(), set()
        for le in prefix:
            if le not in ltor_node:
                return -1
            ltor_node = ltor_node[le]
            lmatch = ltor_node['#']
        for le in suffix[::-1]:
            if le not in rtol_node:
                return -1
            rtol_node = rtol_node[le]
            rmatch = rtol_node['#']
        res = lmatch.intersection(rmatch)
        return max(res) if res else -1
        


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie_root = self.build_trie(words)

    def build_trie(self, words):
        word_idx = {word: i for i, word in enumerate(words)}
        trie = lambda: defaultdict(trie)
        root = trie()
        for word, i in word_idx.items():
            W = word + '&' + word
            for p in range(len(word) + 1):
                node = root
                for q in range(p, len(W)):
                    node = node[W[q]]
                    if '#' not in node:
                        node['#'] = []
                    node['#'].append(i)
        return root

    def f(self, prefix: str, suffix: str) -> int:
        """Instead of building two tries, we duplicate the word with a separater
        in the middle. This way, we can produce trie for all possible suffix + 
        '&' + prefix. During the search, we can search directly and there is
        no need to compute intersection.

        This might not seem much faster than the previous solution, but its
        code is much simpler and easier to maintain.

        1510 ms, faster than 67.60%
        """
        node = self.trie_root
        for le in suffix + '&' + prefix:
            node = node[le]
        return -1 if '#' not in node else max(node['#'])
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


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
