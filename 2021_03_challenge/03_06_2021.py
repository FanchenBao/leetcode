# from pudb import set_trace; set_trace()
from typing import List
import pprint
from random import randint
from collections import defaultdict
from functools import reduce


class Solution1:
    def is_tail(self, w1: str, w2: str) -> bool:
        """Check whether w1 is the tail of w2"""
        return all(l1 == l2 for l1, l2 in zip(w1[::-1], w2[::-1]))

    def minimumLengthEncoding(self, words: List[str]) -> int:
        """TLE. O(N^2) not going to work.
        """
        sorted_words = sorted(words, key=lambda w: len(w))
        for i in range(len(sorted_words)):
            for j in range(i + 1, len(sorted_words)):
                if self.is_tail(sorted_words[i], sorted_words[j]):
                    sorted_words[i] = ''
                    break
        return sum(w != '' for w in sorted_words) + len(''.join(sorted_words))


class Solution2:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """This is a Trie solution. It runs O(N), which to be exact is the total
        number of letters in the words list. We always check the longest word
        first, and check it backwards. As we go through it, we create a trie.
        This guarantees that whenever a word can fit in a previously encountered
        word, we will just go through the trie we have already created. We
        increment the result when a branch of the trie terminates. Special
        attention must be paid to duplicated words. For that, we need a flag
        called new_end, which means has a new ending of a trie branch be created
        We only increment result when new_end is true.

        O(N), 252 ms, 22% ranking.
        """
        trie_root = [0, {}]
        res = 0
        for word in sorted(words, key=lambda w: len(w), reverse=True):
            trie_node = trie_root
            new_end = False
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in trie_node[1]:
                    trie_node[1][word[i]] = [trie_node[0] + 1, {}]
                    new_end = True
                trie_node = trie_node[1][word[i]]
            if new_end:
                res += (trie_node[0] + 1)
        return res


class Solution3:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """This is almost exactly the same as solution 2, but with a better
        implementation of the trie. I got this from the Submission Detail.

        O(N), 144 ms, 62% ranking. By simplifying the trie implementation, we
        significantly speed up the algo.
        """
        trie_root = {}
        res = 0
        for word in sorted(words, key=lambda w: len(w), reverse=True):
            trie_node = trie_root
            new_end = False
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in trie_node:
                    trie_node[word[i]] = {}
                    new_end = True
                trie_node = trie_node[word[i]]
            # instead of tracking length of word, we can just call len() on it
            if new_end:
                res += (len(word) + 1)
        return res


class Solution4:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """This is the Trie solution provided by the official solution. It is
        the same idea, but my boy the implementation is impressive. I am leaving
        it here for inspiration on how to create a Trie recursively, and how the
        reduce function can be magically used in a Trie solution.

        Bravo, Bravo, Bravo!
        """
        # Such an elegant way of creating a Trie
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        non_dup_words = list(set(words))
        last_trie_node = [reduce(dict.__getitem__, word[::-1], trie) for word in non_dup_words]
        return sum(len(non_dup_words[i]) + 1 for i, node in enumerate(last_trie_node) if not node)


sol1 = Solution1()
sol = Solution4()

total_num_test_cases = 100
num_words_per_test = 100
tests = []
for _ in range(total_num_test_cases):
    test = []
    for _ in range(num_words_per_test):
        test.append(''.join(chr(randint(97, 122)) for _ in range(randint(1, 7))))
    tests.append(test[:])

# tests = [['e', 'yf', 'dm', 'o', 'e']]

for i, test in enumerate(tests):
    ans = sol1.minimumLengthEncoding(test)
    res = sol.minimumLengthEncoding(test)
    if res == ans:
        # print(f'Test {i}: PASS')
        pass
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {test}')
