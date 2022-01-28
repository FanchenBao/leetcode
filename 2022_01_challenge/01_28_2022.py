# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class WordDictionary:
    """LeetCode 211

    I feel like this is quite a naive solution, where we simply build a trie
    from left to right and search the word accordingly. When we hit a dot, we
    simply search all possible next nodes and see if any one of them will
    succeed.

    848 ms, 5% ranking.
    """

    def __init__(self):
        trie = lambda: defaultdict(trie)
        self.root = trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for le in word:
            node = node[le]
        node['#'] = word

    def search_help(self, word: int, node) -> bool:
        for i, le in enumerate(word):
            if le != '.':
                if le in node:
                    node = node[le]
                else:
                    return False
            else:
                return any(self.search_help(word[i + 1:], node[k]) for k in node if k != '#')
        return '#' in node

    def search(self, word: str) -> bool:
        return self.search_help(word, self.root)



class WordDictionary:
    """Backtracking solution. This one should be faster because we don't have
    to do string splicing.

    It's much faster. 387 ms, 43% ranking.
    """

    def __init__(self):
        trie = lambda: defaultdict(trie)
        self.root = trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for le in word:
            node = node[le]
        node['#'] = word

    def search(self, word: str) -> bool:
        def dfs(node, idx: int) -> bool:
            if len(word) == idx:
                return '#' in node
            if word[idx] == '.':
                if any(dfs(node[k], idx + 1) for k in node if k != '#'):
                    return True
                return False
            if word[idx] in node:
                return dfs(node[word[idx]], idx + 1)
            return False
        
        return dfs(self.root, 0)

        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
