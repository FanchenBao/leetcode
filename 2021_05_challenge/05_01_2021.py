# from pudb import set_trace; set_trace()
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()


class WordFilter1:
    """LeetCode 745

    We did check out the hint, but did not use the hint. We did, however,
    check the failed test case to realie that it is crucial to pre-process the
    data to avoid repetition. The way to avoid repetition in the input words is
    to only count the word that appears the first time from back to front. The
    reason we check back to front is that we are required to always return the
    bigger index if more than one indices are available.

    The second part of avoiding repetition is to set up a memo, such that if
    repeats in prefix and suffix happens, we can immediately return the result.

    With these two trickery implemented, this problem can be resolved with
    a simple solution: create two tries, one for prefix, and one for suffix.
    And then we search the given prefix to return a set of indices that satisfy
    the prefix. We do the same thing for the suffix, and then take the inter-
    section of the two result sets. If the set is empty, return -1; otherwise
    return the max in the set.

    O(NM), where N is the total number of words and M is the length of each
    word. 672 ms, 90% ranking.
    """

    def __init__(self, words: List[str]):
        self.pre = TrieNode()
        self.suf = TrieNode()
        self.words = words
        self.make_pre_trie()
        self.make_suf_trie()
        self.memo = {}

    def make_pre_trie(self):
        seen = set()
        for i in range(len(self.words) - 1, -1, -1):
            word = self.words[i]
            if word in seen:
                continue
            seen.add(word)
            node = self.pre
            for le in word:
                if le not in node.children:
                    node.children[le] = TrieNode()
                node = node.children[le]
                node.indices.add(i)

    def make_suf_trie(self):
        seen = set()
        for i in range(len(self.words) - 1, -1, -1):
            word = self.words[i]
            if word in seen:
                continue
            seen.add(word)
            node = self.suf
            for le in word[::-1]:
                if le not in node.children:
                    node.children[le] = TrieNode()
                node = node.children[le]
                node.indices.add(i)

    def f(self, prefix: str, suffix: str) -> int:
        key = prefix + '#' + suffix
        if key not in self.memo:
            node_pre = self.pre
            for le in prefix:
                if le in node_pre.children:
                    node_pre = node_pre.children[le]
                else:
                    break
            node_suf = self.suf
            for le in suffix[::-1]:
                if le in node_suf.children:
                    node_suf = node_suf.children[le]
                else:
                    break
            res = node_pre.indices.intersection(node_suf.indices)
            self.memo[key] = max(res) if res else -1
        return self.memo[key]


class WordFilter2:
    """This is the method I implemented based on the hint. We create new keys to
    build the trie. For example, if the input is 'test', the keys for trie are
    'test#test', 'est#test', 'st#test', 't#test', '#test'. We build trie for
    each key. During search, we produce a new key called suffix + '#' + prefix.
    And then use the new key to search the trie.

    We also include the trickery of not repeating on the input words or the
    prefix suffix pair.
    """

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.words = words
        self.make_trie()
        self.memo = {}

    def make_trie(self):
        seen = set()
        for i in range(len(self.words) - 1, -1, -1):
            word = self.words[i]
            if word in seen:
                continue
            seen.add(word)
            for j in range(len(word) + 1):
                trie_word = word[j:] + '#' + word
                node = self.trie
                for le in trie_word:
                    if le not in node.children:
                        node.children[le] = TrieNode()
                    node = node.children[le]
                    node.indices.add(i)

    def f(self, prefix: str, suffix: str) -> int:
        key = suffix + '#' + prefix
        if key not in self.memo:
            node = self.trie
            for le in key:
                if le in node.children:
                    node = node.children[le]
                else:
                    break
            self.memo[key] = max(node.indices) if node.indices else -1
        return self.memo[key]


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
