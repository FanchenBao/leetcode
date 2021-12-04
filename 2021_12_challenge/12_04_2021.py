# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, deque


class StreamChecker:
    """LeetCode 1032

    I used two tricks. First, I created a trie from the given array of words.
    However, each word is reversed when pushing into the trie. This is because
    when checking the stream, we go from back to front.

    Second, I used a deque to keep track of the viable letters in the stream.
    The size of the deque is equal to the longest word in words.

    For each letter coming in, I go from the end of the deque backwards to check
    whether each letter can be found in the trie. Whenever a letter is not in
    the trie, we know that it is a no match.

    O(log(M)) for query, where M is the length of words. O(M) for creating the
    trie. 644 ms, 73% ranking.
    """

    def __init__(self, words: List[str]):
        self.trie = self.create_trie(words)
        self.chars = deque([''] * (max(len(w) for w in words)))

    def create_trie(self, words: List[str]):
        trie_node = lambda: defaultdict(trie_node)
        root = trie_node()
        for word in words:
            node = root
            for le in word[::-1]:
                node = node[le]
            node['*']  # indicator for end of word
        return root

    def query(self, letter: str) -> bool:
        self.chars.popleft()
        self.chars.append(letter)
        node = self.trie
        for i in range(len(self.chars) - 1, -1, -1):
            if '*' in node:
                return True
            if self.chars[i] in node:
                node = node[self.chars[i]]
            else:
                break
        return '*' in node



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
