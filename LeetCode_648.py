# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Use Trie. It's not difficult. I did get it wrong the first attempt
        because I forgot to return the shortest prefix. But this was easy to
        fix, because we just need to break the search whenever the sentinel
        is hit in the Trie.

        O((N + M) * D), where N = len(dictionary), M = len(sentence.split(' '))
        D is the average length of word in dictionary.

        99 ms, 89% ranking.
        """
        trie = lambda: defaultdict(trie)
        root = trie()
        for word in dictionary:
            node = root
            for w in word:
                node = node[w]
            node['*'] = word
        res = []
        for word in sentence.split(' '):
            node = root
            for w in word:
                if '*' in node or w not in node:
                    break
                node = node[w]
            res.append(node.get('*', word))
        return ' '.join(res)



sol = Solution()
tests = [
    (["cat","bat","rat"], "the cattle was rattled by the battery", "the cat was rat by the bat"),
    (["a","b","c"], "aadsfasf absbs bbab cadsfafs", "a a b c"),
    (["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa", "a a a a a a a a bbb baba a"),
]

for i, (dictionary, sentence, ans) in enumerate(tests):
    res = sol.replaceWords(dictionary, sentence)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
